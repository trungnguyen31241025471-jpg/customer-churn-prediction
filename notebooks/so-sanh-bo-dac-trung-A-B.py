import json, warnings
import numpy as np, pandas as pd
from scipy.stats import wilcoxon
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, average_precision_score, precision_recall_curve, precision_score, recall_score, f1_score, confusion_matrix
import xgboost as xgb, lightgbm as lgb
warnings.filterwarnings("ignore")

df_raw = pd.read_csv("online_retail_II_raw.csv.gz")
df_raw["InvoiceDate"] = pd.to_datetime(df_raw["InvoiceDate"])
if "CustomerID" in df_raw.columns: df_raw = df_raw.rename(columns={"CustomerID": "Customer ID"})
df_raw["is_cancelled"] = df_raw["Invoice"].astype(str).str.startswith("C")

def lam_sach_du_lieu(df_input):
    df = df_input.copy()
    df["Invoice"] = df["Invoice"].astype(str)
    df = df[~df["Invoice"].str.startswith("C")]
    non_product_codes = ["POST", "D", "M", "BANK CHARGES", "DOT", "ADJUST", "ADJUST2", "CRUK"]
    df = df[~df["StockCode"].astype(str).isin(non_product_codes)]
    df = df.dropna(subset=["Customer ID"])
    df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]
    df = df.drop_duplicates()
    df["Revenue"] = df["Quantity"] * df["Price"]
    return df.reset_index(drop=True)

df_clean = lam_sach_du_lieu(df_raw)
max_date = df_clean["InvoiceDate"].max()
first_cutoff = pd.Timestamp("2010-08-01")
TOP_COUNTRIES = df_clean[df_clean["InvoiceDate"] < first_cutoff]["Country"].value_counts().head(8).index.tolist()

def dac_trung_gop(df_raw_input, df_clean_input, cutoff_date, top_countries=TOP_COUNTRIES):
    """Tinh CA hai bo dac trung trong 1 lan (chung toan bo phan RFM/Trend/Cancel/Repeat)."""
    obs_clean = df_clean_input[df_clean_input["InvoiceDate"] < cutoff_date].copy()
    obs_raw = df_raw_input[df_raw_input["InvoiceDate"] < cutoff_date]

    rfm = obs_clean.groupby("Customer ID").agg(
        Recency=("InvoiceDate", lambda x: (cutoff_date - x.max()).days),
        Frequency=("Invoice", "nunique"), Monetary=("Revenue", "sum"),
        AvgOrderValue=("Revenue", "mean"), NumProducts=("StockCode", "nunique"),
        FirstPurchase=("InvoiceDate", "min"),
        Country=("Country", lambda x: x.mode().iloc[0] if not x.mode().empty else "Unknown"),
    ).reset_index()
    rfm["Tenure"] = (cutoff_date - rfm["FirstPurchase"]).dt.days

    def std_kc(d):
        d = np.sort(d.unique())
        return float(np.std(np.diff(d) / np.timedelta64(1, "D"))) if len(d) >= 3 else np.nan
    def avg_kc(d):
        d = np.sort(d.unique())
        return float(np.mean(np.diff(d) / np.timedelta64(1, "D"))) if len(d) >= 2 else np.nan
    ivs = obs_clean.groupby("Customer ID")["InvoiceDate"].apply(std_kc).rename("IntervalStd").reset_index()
    iva = obs_clean.groupby("Customer ID")["InvoiceDate"].apply(avg_kc).rename("AvgInterval").reset_index()
    rfm = rfm.merge(ivs, on="Customer ID", how="left").merge(iva, on="Customer ID", how="left")
    rfm["IntervalStd"] = rfm["IntervalStd"].fillna(rfm["IntervalStd"].median())
    rfm["AvgInterval"] = rfm["AvgInterval"].fillna(rfm["AvgInterval"].median())

    mid, far = cutoff_date - pd.Timedelta(days=90), cutoff_date - pd.Timedelta(days=180)
    rr = obs_clean[obs_clean["InvoiceDate"] >= mid].groupby("Customer ID")["Revenue"].sum()
    rp = obs_clean[(obs_clean["InvoiceDate"] >= far) & (obs_clean["InvoiceDate"] < mid)].groupby("Customer ID")["Revenue"].sum()
    fr = obs_clean[obs_clean["InvoiceDate"] >= mid].groupby("Customer ID")["Invoice"].nunique()
    fp = obs_clean[(obs_clean["InvoiceDate"] >= far) & (obs_clean["InvoiceDate"] < mid)].groupby("Customer ID")["Invoice"].nunique()
    tr = pd.concat([rr.rename("rr"), rp.rename("rp"), fr.rename("fr"), fp.rename("fp")], axis=1).fillna(0)
    tr["SpendingTrend"] = tr["rr"] - tr["rp"]; tr["FrequencyTrend"] = tr["fr"] - tr["fp"]
    rfm = rfm.merge(tr[["SpendingTrend", "FrequencyTrend"]].reset_index(), on="Customer ID", how="left")
    rfm[["SpendingTrend", "FrequencyTrend"]] = rfm[["SpendingTrend", "FrequencyTrend"]].fillna(0)

    tot = obs_raw.groupby("Customer ID")["Invoice"].nunique().rename("TotalInvoices")
    can = obs_raw[obs_raw["is_cancelled"]].groupby("Customer ID")["Invoice"].nunique().rename("CancelledInvoices")
    c = pd.concat([tot, can], axis=1).fillna(0)
    c["CancelRate"] = (c["CancelledInvoices"] / c["TotalInvoices"].replace(0, np.nan)).fillna(0)
    rfm = rfm.merge(c[["CancelRate"]].reset_index(), on="Customer ID", how="left")
    rfm["CancelRate"] = rfm["CancelRate"].fillna(0)

    tenure_m = (rfm["Tenure"] / 30.44).clip(lower=1)
    am = obs_clean.assign(ym=obs_clean["InvoiceDate"].dt.to_period("M")).groupby("Customer ID")["ym"].nunique().rename("ActiveMonths")
    rfm = rfm.merge(am, on="Customer ID", how="left")
    rfm["ActiveMonths"] = rfm["ActiveMonths"].fillna(1)
    rfm["RepeatPurchaseRatio"] = (rfm["ActiveMonths"] / tenure_m).clip(upper=1.0)

    rfm["Is_UK"] = (rfm["Country"] == "United Kingdom").astype(int)
    cg = rfm["Country"]
    dummies = pd.DataFrame({f"Country_{k}": (cg == k).astype(int) for k in top_countries})
    rfm = pd.concat([rfm.reset_index(drop=True), dummies.reset_index(drop=True)], axis=1)
    return rfm.drop(columns=["FirstPurchase", "Country"])

def kiem_tra_va_gan_nhan(df_clean_input, cutoff_date, W, max_date_input):
    end = cutoff_date + pd.Timedelta(days=W)
    if end > max_date_input: return None, False
    obs = df_clean_input[df_clean_input["InvoiceDate"] < cutoff_date]
    fut = df_clean_input[(df_clean_input["InvoiceDate"] >= cutoff_date) & (df_clean_input["InvoiceDate"] < end)]
    before = obs["Customer ID"].unique()
    if len(before) == 0: return None, False
    active = set(fut["Customer ID"].unique())
    return pd.Series([0 if c in active else 1 for c in before], index=before, name="churn"), True

_cache = {}
def data_at(cutoff, W=90):
    if cutoff not in _cache:
        y, ok = kiem_tra_va_gan_nhan(df_clean, cutoff, W, max_date)
        _cache[cutoff] = None if not ok else dac_trung_gop(df_raw, df_clean, cutoff).merge(y.rename("churn"), left_on="Customer ID", right_index=True)
    return _cache[cutoff]

def tao_cac_fold(W_months, tests):
    return [(t - pd.DateOffset(months=2 * W_months), t - pd.DateOffset(months=W_months), t) for t in tests]

test_cutoffs = [pd.Timestamp("2011-02-01") + pd.DateOffset(months=i) for i in range(8)]
folds = tao_cac_fold(3, test_cutoffs)

model_configs = {
    "LogisticRegression": (lambda p, s: LogisticRegression(random_state=s, class_weight="balanced", max_iter=1000, **p), [{"C": 0.1}, {"C": 1.0}], True, (0,)),
    "RandomForest": (lambda p, s: RandomForestClassifier(random_state=s, class_weight="balanced", n_jobs=-1, **p), [{"n_estimators": 200, "max_depth": 5}, {"n_estimators": 300, "max_depth": 8}], False, (0, 1, 2)),
    "XGBoost": (lambda p, s: xgb.XGBClassifier(random_state=s, eval_metric="logloss", n_jobs=4, **p), [{"n_estimators": 200, "max_depth": 4, "learning_rate": 0.1}, {"n_estimators": 300, "max_depth": 6, "learning_rate": 0.05}], False, (0,)),
    "LightGBM": (lambda p, s: lgb.LGBMClassifier(random_state=s, verbose=-1, n_jobs=4, **p), [{"n_estimators": 200, "max_depth": 4, "learning_rate": 0.1}, {"n_estimators": 300, "max_depth": 6, "learning_rate": 0.05}], False, (0,)),
}

def nguong_toi_uu_f1(y, p):
    pr, rc, th = precision_recall_curve(y, p)
    f1 = 2 * pr[:-1] * rc[:-1] / np.clip(pr[:-1] + rc[:-1], 1e-9, None)
    return float(th[int(np.argmax(f1))])

def chay_1_fold(model_name, cols, tr_c, va_c, te_c, W=90):
    build, grid, scale, seeds = model_configs[model_name]
    tr, va, te = data_at(tr_c, W), data_at(va_c, W), data_at(te_c, W)
    Xtr, Xva, Xte = tr[cols].copy(), va[cols].copy(), te[cols].copy()
    if scale:
        sc = StandardScaler().fit(Xtr); Xtr, Xva, Xte = sc.transform(Xtr), sc.transform(Xva), sc.transform(Xte)
    roc, pr_ = [], []
    for s in seeds:
        best, bp = -1, grid[0]
        for p in grid:
            m = build(p, s).fit(Xtr, tr["churn"])
            a = roc_auc_score(va["churn"], m.predict_proba(Xva)[:, 1])
            if a > best: best, bp = a, p
        m = build(bp, s).fit(Xtr, tr["churn"])
        pt = m.predict_proba(Xte)[:, 1]
        roc.append(roc_auc_score(te["churn"], pt)); pr_.append(average_precision_score(te["churn"], pt))
    return {"roc_auc": float(np.mean(roc)), "pr_auc": float(np.mean(pr_))}

sample = data_at(pd.Timestamp("2010-08-01"))
v1_cols = ["Recency", "Frequency", "Monetary", "AvgOrderValue", "NumProducts", "IntervalStd",
           "SpendingTrend", "FrequencyTrend", "CancelRate", "ActiveMonths", "RepeatPurchaseRatio"] + \
          [c for c in sample.columns if c.startswith("Country_")]
v2_cols = ["Recency", "Frequency", "Monetary", "AvgOrderValue", "NumProducts", "Tenure",
           "IntervalStd", "AvgInterval", "SpendingTrend", "FrequencyTrend", "CancelRate",
           "ActiveMonths", "RepeatPurchaseRatio", "Is_UK"]
print("v1 (cu, co Country one-hot):", len(v1_cols), v1_cols)
print("v2 (moi, co Tenure/AvgInterval/Is_UK):", len(v2_cols), v2_cols)

out = {"v1_cols": v1_cols, "v2_cols": v2_cols, "results": {}}
for name in model_configs:
    r1 = [chay_1_fold(name, v1_cols, *f) for f in folds]
    r2 = [chay_1_fold(name, v2_cols, *f) for f in folds]
    roc1, roc2 = [x["roc_auc"] for x in r1], [x["roc_auc"] for x in r2]
    pr1, pr2 = [x["pr_auc"] for x in r1], [x["pr_auc"] for x in r2]
    stat_r, p_r = wilcoxon(roc1, roc2) if any(a != b for a, b in zip(roc1, roc2)) else (0, 1.0)
    stat_p, p_p = wilcoxon(pr1, pr2) if any(a != b for a, b in zip(pr1, pr2)) else (0, 1.0)
    out["results"][name] = {
        "v1_roc": roc1, "v2_roc": roc2, "v1_pr": pr1, "v2_pr": pr2,
        "roc_mean_v1": float(np.mean(roc1)), "roc_mean_v2": float(np.mean(roc2)),
        "pr_mean_v1": float(np.mean(pr1)), "pr_mean_v2": float(np.mean(pr2)),
        "wilcoxon_p_roc": float(p_r), "wilcoxon_p_pr": float(p_p),
        "v1_wins_roc": int(sum(a > b for a, b in zip(roc1, roc2))),
    }
    print(name, "v1 ROC", round(np.mean(roc1), 4), "v2 ROC", round(np.mean(roc2), 4), "p=", round(p_r, 4))

json.dump(out, open("so_sanh_v1_v2.json", "w"), ensure_ascii=False, indent=1)
print("XONG")

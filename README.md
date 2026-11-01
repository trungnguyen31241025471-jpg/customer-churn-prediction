# Dự đoán rời bỏ khách hàng thương mại điện tử bằng học máy có thể giải thích

Đề tài nghiên cứu khoa học sinh viên (Nhóm 3): xây dựng khung dự đoán churn có thể giải thích cho thương mại điện tử phi hợp đồng, trên bộ dữ liệu **UCI Online Retail II**, từ giao dịch thô đến khung hỗ trợ quyết định kinh doanh.

## Điểm khác biệt của nghiên cứu

- **Tự định nghĩa nhãn churn** từ giao dịch thô bằng cửa sổ quan sát/dự đoán 90 ngày, có kiểm tra right-censoring (không dùng nhãn gán sẵn).
- **Walk-Forward Validation 8 fold** (mốc Test hằng tháng từ 01/02/2011 đến 01/09/2011), thay cho chia ngẫu nhiên; so sánh mô hình bằng kiểm định Wilcoxon signed-rank.
- **SHAP ba mức** (toàn cục, tương tác, cục bộ), rồi chuyển thành bảng quyết định cấp từng khách hàng: Khách hàng → Xác suất churn → Driver chính → Hành động giữ chân.

## Dữ liệu

| Mục | Giá trị |
|---|---|
| Nguồn | UCI Online Retail II (01/12/2009 – 09/12/2011) |
| Dữ liệu thô | 1.067.371 dòng × 8 cột |
| Sau làm sạch | 776.854 dòng, 5.853 khách hàng, 41 quốc gia |

Dữ liệu **không** nằm trong repo. Xem hướng dẫn tải tại [`data/README.md`](data/README.md).

## Kết quả chính

Đánh giá trên 8 fold walk-forward (trung bình ± độ lệch chuẩn):

| Mô hình | ROC-AUC | PR-AUC |
|---|---|---|
| **Random Forest** | **0,797 ± 0,014** | **0,853 ± 0,019** |
| Logistic Regression | 0,790 ± 0,010 | 0,849 ± 0,017 |
| LightGBM | 0,769 ± 0,019 | 0,830 ± 0,028 |
| XGBoost | 0,766 ± 0,021 | 0,827 ± 0,027 |
| Baseline (chỉ Recency) | 0,756 ± 0,021 | — |

- Random Forest vượt cả bốn đối thủ có ý nghĩa thống kê (Wilcoxon, p < 0,05).
- Mã hóa địa lý one-hot 8 quốc gia chỉ cải thiện có ý nghĩa trên Logistic Regression (p = 0,016), không trên các mô hình dạng cây.
- Năm đặc trưng dẫn đầu theo SHAP: `ActiveMonths`, `Frequency`, `Monetary`, `Recency`, `RepeatPurchaseRatio`.
- Tại mốc 01/06/2011, khung hỗ trợ quyết định phân loại 4.909 khách hàng: 3.862 (78,7%) rủi ro cao, chia thành 10 nhãn kinh doanh.
- Hạn chế chính: `churn_prob` là điểm xếp hạng rủi ro, chưa phải xác suất đã hiệu chỉnh (do dùng `class_weight='balanced'`).

## Cấu trúc thư mục

```text
customer-churn-prediction/
├── data/                # dữ liệu thô (bị .gitignore) + hướng dẫn tải
├── notebooks/           # notebook đánh số theo thứ tự chạy
│   └── archive/         # bản cũ, thử nghiệm
├── src/                 # script Python
├── docs/
│   ├── figures/eda/     # biểu đồ EDA
│   ├── 01-tong-quan/    # tổng quan đề tài, research gap, lộ trình
│   ├── 02-ly-thuyet/    # nền tảng kiến thức
│   ├── 04-cong-cu/      # hướng dẫn công cụ và GitHub
│   ├── 06-tai-lieu-tham-khao/   # literature review
│   └── 07-bao-cao-gui-thay/     # báo cáo tiến độ
├── requirements.txt
└── README.md
```

## Cách chạy

1. Clone repo và cài thư viện:
   ```bash
   git clone https://github.com/trungnguyen31241025471-jpg/customer-churn-prediction.git
   cd customer-churn-prediction
   pip install -r requirements.txt
   ```
2. Tải dữ liệu và đặt vào `data/` theo [`data/README.md`](data/README.md).
3. Chạy các notebook trong `notebooks/` theo thứ tự:

| Notebook | Nội dung |
|---|---|
| `01_eda_tien_xu_ly.ipynb` | Khám phá và làm sạch dữ liệu |
| `02_pipeline_bo_A.ipynb` | Pipeline walk-forward với bộ đặc trưng A |
| `03_pipeline_bo_B_walkforward.ipynb` | Pipeline walk-forward với bộ 14 đặc trưng chính (Bộ B) |
| `04_shap_ho_tro_quyet_dinh.ipynb` | Giải thích SHAP và khung hỗ trợ quyết định |

## Công nghệ

Python 3.10; pandas, numpy; scikit-learn, xgboost, lightgbm; shap; scipy, statsmodels; matplotlib, seaborn.

## Hướng phát triển

Hiệu chỉnh xác suất (calibration); counterfactual explanation; thử nghiệm uplift modeling nếu có dữ liệu can thiệp; kiểm chứng trên ít nhất một bộ dữ liệu e-commerce khác.

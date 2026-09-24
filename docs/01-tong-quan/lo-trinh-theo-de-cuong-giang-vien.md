# Lộ Trình Nghiên Cứu Theo Đề Cương Giảng Viên (9 Bước)

> Dựa trên file `Topic\_3.docx` giảng viên gửi. Tài liệu này trình bày chi tiết từng bước, định nghĩa khái niệm kèm trích dẫn, và chỉ rõ phần nào \*\*đã có sẵn\*\* trong project (file/notebook tương ứng) và phần nào \*\*cần bổ sung mới\*\*.
>
> Quan hệ với `tong-quan-de-tai.md`: file đó là phiên bản mở rộng theo hướng học thuật (nested CV, ablation, 2 dataset...) mà nhóm tự xây dựng thêm. File này là \*\*phiên bản bám sát đúng đề cương của thầy\*\* — dùng file này làm khung chính, phần mở rộng học thuật ở file kia có thể áp dụng thêm nếu còn thời gian, không bắt buộc.

\---

## Bước 1 — Xác định bài toán nghiên cứu

**Customer Churn là gì**: hiện tượng khách hàng chấm dứt quan hệ giao dịch với doanh nghiệp — xem định nghĩa đầy đủ tại [Wikipedia — Churn rate](https://en.wikipedia.org/wiki/Churn_rate).

**Tại sao quan trọng trong e-commerce**: theo nghiên cứu được trích dẫn trên Harvard Business Review, chi phí thu hút một khách hàng mới có thể **cao gấp 5-25 lần** so với chi phí giữ chân một khách hàng hiện có — xem [HBR — The Value of Keeping the Right Customers](https://hbr.org/2014/10/the-value-of-keeping-the-right-customers). Đây chính là lý do dự đoán churn sớm mang lại giá trị kinh doanh trực tiếp, không chỉ là bài toán kỹ thuật.

**Biến mục tiêu**: `Churn = 1` (khách rời bỏ) / `Churn = 0` (khách còn hoạt động) — xem cách gán nhãn cụ thể ở Bước 2.

**Research Questions (RQ)** — ✅ **đã phân tích chi tiết kèm minh chứng từ literature** tại `nghien-cuu-gap-va-research-questions.md` (đọc full-text 2 bài quan trọng nhất, không chỉ abstract). Tóm tắt 3 RQ chính thức:

|RQ|Câu hỏi|Trả lời bằng công cụ nào trong đề tài|
|-|-|-|
|RQ1|Dự đoán churn 3/6 tháng chính xác đến mức nào khi TỰ định nghĩa nhãn từ dữ liệu giao dịch thô (khác với các bài dùng nhãn có sẵn)?|ROC-AUC, PR-AUC qua Walk-Forward Validation (Bước 5-6)|
|RQ2|Đặc trưng hành vi theo thời gian có cải thiện AUC có ý nghĩa thống kê so với RFM cơ bản không?|Ablation + Wilcoxon test (đã có trong `nang-cao-sensitivity-feature-nested-cv.ipynb`)|
|RQ3|Có thể tự động hoá việc chuyển XAI thành hành động kinh doanh cụ thể không?|Business Decision Support layer (Bước 8)|

Xem `nghien-cuu-gap-va-research-questions.md` để đọc đầy đủ bảng phân tích khoảng trống, minh chứng cụ thể từng luận điểm, giả thuyết nghiên cứu (H1-H3), và đoạn Contribution Statement có thể dùng thẳng cho Introduction.

\---

## Bước 2 — Thu thập dữ liệu

* Tải **UCI Online Retail II** — chi tiết đầy đủ về nguồn, schema, đặc điểm nghiệp vụ đã có tại `../03-du-lieu/mo-ta-du-lieu-online-retail-ii.md`.
* **Chuyển từ dữ liệu giao dịch sang dữ liệu customer-level**: mỗi dòng gốc là một dòng hóa đơn (invoice line item); cần `groupby('Customer ID')` để tổng hợp thành một dòng/khách hàng — kỹ thuật này đã thực hành ở `../05-thuc-hanh/eda-va-tien-xu-ly-du-lieu.ipynb`.
* **Xác định khoảng thời gian quan sát và quy tắc churn**: dùng kỹ thuật **observation window + prediction window** — quan sát hành vi trước một mốc `cutoff date`, gán nhãn churn dựa trên việc khách có mua trong N tháng sau đó hay không. Khái niệm **censoring** (không đủ dữ liệu tương lai để xác định nhãn) vay mượn từ Survival Analysis — xem [GeeksforGeeks — Kaplan-Meier Estimator](https://www.geeksforgeeks.org/data-science/kaplan-meier-estimator-survival-analysis/). Đã thực hành đầy đủ (nhiều mốc cutoff, có kiểm tra censoring) ở `../05-thuc-hanh/nang-cao-sensitivity-feature-nested-cv.ipynb` (Phần 1).

\---

## Bước 3 — Data Cleaning + EDA

✅ **Đã có đầy đủ** ở `../05-thuc-hanh/eda-va-tien-xu-ly-du-lieu.ipynb`, đúng theo yêu cầu của thầy:

* Xử lý missing values, cancelled orders, duplicate — xem giải thích lý do ở `../05-thuc-hanh/giai-thich-ky-thuat-eda-tien-xu-ly-feature-engineering.md` (mục B1-B5).
* Loại bỏ giao dịch bất thường — xử lý outlier bằng Winsorization/Capping (mục B6 cùng file trên).
* Phân tích số lần mua, tổng chi tiêu, thời gian giữa các lần mua, Recency, tỷ lệ khách churn — đúng các phân tích ở Bước 6 (khách hàng) trong notebook EDA.

\---

## Bước 4 — Feature Engineering

Bảng dưới đây đối chiếu đúng 6 nhóm đặc trưng thầy yêu cầu với trạng thái thực tế trong project:

|Nhóm (theo thầy)|Ví dụ cụ thể|Trạng thái|Định nghĩa \& tham khảo|
|-|-|-|-|
|**RFM**|Recency, Frequency, Monetary|✅ Đã có|Framework kinh điển trong marketing — [Optimove — RFM Segmentation](https://www.optimove.com/resources/learning-center/rfm-segmentation)|
|**Purchase behavior**|Purchase interval, AOV (Average Order Value)|✅ Đã có|`IntervalStd` (độ lệch chuẩn khoảng cách mua) và `AvgOrderValue` đã tính trong `nang-cao-sensitivity-feature-nested-cv.ipynb`|
|**Product**|Product diversity, số SKU|✅ Đã có|`NumProducts` (số StockCode duy nhất đã mua)|
|**Temporal**|Spending trend, **frequency trend**|✅ Đã có cả 2|`SpendingTrend` và `FrequencyTrend` (số đơn 3 tháng gần vs trước) — đã tính trong `nang-cao-sensitivity-feature-nested-cv.ipynb`|
|**Engagement**|Repeat purchase ratio|✅ Đã có|Định nghĩa đã dùng: (số tháng có mua hàng) / (số tháng kể từ lần mua đầu tiên đến cutoff) — đo mức độ đều đặn, khác với Frequency (chỉ đếm tổng số đơn)|
|**Geographic**|Country/region|✅ Đã merge vào model|Top 8 quốc gia (xác định từ dữ liệu trước cutoff sớm nhất để tránh leakage) + One-Hot Encoding, merge trực tiếp vào ma trận đặc trưng trong hàm `tinh\_dac\_trung\_nang\_cao()`|

**Việc cần làm ngay**: ~~bổ sung `FrequencyTrend`, `RepeatPurchaseRatio`, và merge `Country\_grouped`~~ ✅ **Đã hoàn thành** trong bản cập nhật mới nhất của `nang-cao-sensitivity-feature-nested-cv.ipynb`.

\---

## Bước 5 — Xây dựng mô hình Machine Learning

**4 mô hình thầy gợi ý so sánh**:

* **Logistic Regression** (baseline) — [scikit-learn — LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) — ✅ đã có
* **Random Forest** — [scikit-learn — Decision Trees User Guide](https://scikit-learn.org/stable/modules/tree.html) (nền tảng của Random Forest) — ✅ đã có
* **XGBoost** ⭐ (được thầy đánh dấu là mô hình kỳ vọng tốt nhất) — [XGBoost — Official Documentation](https://xgboost.readthedocs.io/) — ✅ đã có
* **LightGBM** — ✅ **Đã bổ sung** làm mô hình thứ 3 trong bản cập nhật mới, dùng song song với Random Forest và XGBoost

**Chia dữ liệu theo thời gian (Time-based Split)** — điểm thầy nhấn mạnh:

> "Dữ liệu được chia thành Training/Validation/Test theo thời gian nếu có thể, để tránh data leakage."

Khái niệm: thay vì chia ngẫu nhiên (random split), với dữ liệu có tính thời gian, cần đảm bảo tập train luôn ở **quá khứ** so với tập test — nếu không, mô hình có thể "nhìn thấy" thông tin tương lai khi huấn luyện, gây đánh giá lạc quan giả tạo. Công cụ chuẩn cho việc này: [scikit-learn — TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html), xem thêm lý do tại [scikit-learn — Cross-validation User Guide, mục Time Series](https://scikit-learn.org/stable/modules/cross_validation.html).

**✅ Đã cập nhật**: `nang-cao-sensitivity-feature-nested-cv.ipynb` giờ dùng **Time-based Walk-Forward Validation** — mỗi fold lấy 3 mốc cutoff liên tiếp: cutoff sớm nhất = Train, cutoff giữa = Validation (chọn hyperparameter), cutoff muộn nhất = Test — đảm bảo Train luôn ở quá khứ so với Test trong mọi fold, đúng yêu cầu của thầy.

\---

## Bước 6 — Đánh giá khả năng dự báo churn

Các chỉ số cần dùng: **ROC-AUC, PR-AUC, Precision, Recall, F1-score, Confusion Matrix** — định nghĩa chi tiết kèm ví dụ số đã có ở `../02-ly-thuyet/nen-tang-kien-thuc-explainable-ml-churn.md` (Phần 8), tham khảo trực quan:

* [StatQuest — Machine Learning Fundamentals: The Confusion Matrix](https://www.youtube.com/watch?v=Kdsp6soqA7o)
* [StatQuest — ROC and AUC, Clearly Explained!](https://www.youtube.com/watch?v=4jRBRDbJemM)
* [scikit-learn — Model evaluation: quantifying prediction quality (bao gồm PR-AUC)](https://scikit-learn.org/stable/modules/model_evaluation.html)

**Vì sao thầy nhấn mạnh Recall và PR-AUC**: churn là bài toán **mất cân bằng lớp** (số khách churn luôn ít hơn số khách không churn) — Accuracy dễ gây hiểu lầm (một mô hình "lười" dự đoán ai cũng không churn vẫn đạt Accuracy cao), trong khi PR-AUC và Recall phản ánh đúng khả năng "bắt được" khách churn thật — đã giải thích chi tiết bằng ví dụ số ở Phần 8.1-8.2 file lý thuyết.

**✅ Đã cập nhật**: `nang-cao-sensitivity-feature-nested-cv.ipynb` giờ tính **cả ROC-AUC và PR-AUC** song song ở mỗi fold Walk-Forward, và dùng cả 2 chỉ số khi kiểm định Wilcoxon giữa các mô hình.

\---

## Bước 7 — Explainable AI (XAI) ⭐

Thầy nhấn mạnh đây là **phần tạo nên điểm khác biệt của đề tài**. Yêu cầu cụ thể:

|Kỹ thuật|Định nghĩa|Trạng thái|
|-|-|-|
|Global feature importance|Đặc trưng nào quan trọng nhất trên toàn bộ tập dữ liệu|✅ Đã có (SHAP summary plot)|
|SHAP summary|Biểu đồ tổng hợp global, thể hiện cả chiều hướng ảnh hưởng|✅ Đã có|
|**SHAP dependence**|Biểu đồ thể hiện quan hệ giữa GIÁ TRỊ của một đặc trưng và SHAP value tương ứng (vd: Recency càng cao thì SHAP value thay đổi thế nào)|🔴 **Chưa có** — cần bổ sung `shap.dependence\_plot()`, xem [SHAP — Official Documentation](https://shap.readthedocs.io/)|
|Individual customer explanation|Giải thích cục bộ cho một khách hàng cụ thể|✅ Đã có (SHAP force plot)|

**Ví dụ pattern thầy đưa ra** (nên tái hiện lại bằng dữ liệu thật khi viết Discussion):

> Recency ↑ + Purchase Frequency ↓ + Spending ↓ → xác suất churn ↑

Đây chính xác là loại insight mà SHAP dependence plot thể hiện rõ nhất — nên ưu tiên bổ sung kỹ thuật này trước khi viết phần Results.

**Lưu ý**: project hiện có thêm LIME, Permutation Importance, và Ablation Study (từ hướng mở rộng học thuật) — thầy không yêu cầu các phần này, nhưng **không mâu thuẫn**, có thể giữ lại như điểm cộng nếu còn thời gian.

\---

## Bước 8 — Chuyển kết quả thành Business Decision Support 🔴 (Hoàn toàn chưa có, cần xây mới)

**Khái niệm nền tảng**: đây chính là tầng cao nhất trong mô hình trưởng thành phân tích dữ liệu (Analytics Maturity Model) — từ Descriptive ("chuyện gì đã xảy ra") → Diagnostic ("tại sao") → Predictive ("chuyện gì sẽ xảy ra" — đây là Bước 5-6) → **Prescriptive ("nên làm gì")** — chính là Bước 8 này. Xem [Dataforest — Analytics Maturity Model](https://dataforest.ai/blog/analytics-maturity-model).

**Công thức thầy đưa ra**:

```
Customer → Churn Probability → Explanation → Recommended Action
```

**Ví dụ cụ thể từ đề cương**:

|Customer|Churn probability|Main drivers|Action|
|-|-|-|-|
|A|0.87|Recency ↑, Frequency ↓|Retention campaign|
|B|0.71|Spending ↓|Personalized promotion|
|C|0.22|High frequency|Loyalty program|

**Cách triển khai cụ thể cho đề tài** (đề xuất xây dựng mới, kết hợp lại toàn bộ pipeline đã có):

1. Lấy xác suất churn từ mô hình tốt nhất (Bước 5-6, khả năng cao là XGBoost).
2. Lấy top 2-3 đặc trưng có SHAP value tuyệt đối lớn nhất cho từng khách hàng (Bước 7 — local explanation) → đây chính là "Main drivers".
3. Xây một **bảng quy tắc** (rule mapping) đơn giản, ví dụ:

   * Nếu driver chính là `Recency cao` → Action = "Gửi email nhắc lại + ưu đãi quay lại"
   * Nếu driver chính là `Monetary/SpendingTrend giảm` → Action = "Ưu đãi cá nhân hóa theo lịch sử mua"
   * Nếu driver chính là `Frequency thấp nhưng Recency vẫn tốt` → Action = "Chương trình khách hàng thân thiết"
4. Xuất ra một bảng/dashboard cuối cùng giống ví dụ trên — đây là sản phẩm cụ thể nên đưa vào phần Results để tăng giá trị Business Analytics của bài, đúng như thầy ghi chú.

**Việc cần làm**: xây một notebook mới (ví dụ `06-business-decision-support.ipynb`) thực hiện đúng 4 bước trên, dùng dữ liệu và mô hình đã có sẵn từ `nang-cao-sensitivity-feature-nested-cv.ipynb`.

\---

## Bước 9 — Đánh giá + viết bài nghiên cứu

* **So sánh các mô hình**: đã có khung ở Bước 5-6, bổ sung PR-AUC và time-based split theo checklist trên.
* **Kiểm định robustness**: đã có Nested CV + Wilcoxon signed-rank test ở `nang-cao-sensitivity-feature-nested-cv.ipynb` (Phần 3).
* **Phân tích yếu tố dẫn đến churn**: dùng kết quả SHAP global + dependence (Bước 7).
* **Giải thích bằng SHAP**: đã có, bổ sung dependence plot.
* **Managerial implications**: chính là nội dung Bước 8 (Business Decision Support) — nên viết thành một mục riêng trong Discussion.
* **Limitations \& future research**: tham khảo cấu trúc IMRAD đầy đủ ở `../02-ly-thuyet/nen-tang-kien-thuc-explainable-ml-churn.md` (Phần 10).

\---

## Tổng hợp việc cần làm 

* \[x] Thêm 3 Research Questions tường minh vào phần mở đầu bài viết (Bước 1) — xem `nghien-cuu-gap-va-research-questions.md`
* \[x] Bổ sung `FrequencyTrend` và `RepeatPurchaseRatio` vào feature engineering (Bước 4) — đã cập nhật trong `nang-cao-sensitivity-feature-nested-cv.ipynb`
* \[x] Merge `Country\_grouped` (đã encode) vào ma trận đặc trưng modeling (Bước 4) — đã merge trực tiếp trong hàm `tinh\_dac\_trung\_nang\_cao()`
* \[x] Thêm LightGBM làm mô hình thứ 4 (Bước 5) — đã thêm cùng Random Forest, XGBoost
* \[x] Chuyển từ StratifiedKFold ngẫu nhiên sang **Time-based Walk-Forward Validation** dựa trên các mốc cutoff (Bước 5) — Train luôn ở quá khứ, Validation ở giữa, Test ở tương lai xa nhất trong mỗi fold
* \[x] Bổ sung PR-AUC vào notebook Nested CV (Bước 6) — tính song song với ROC-AUC ở mỗi fold, dùng cả 2 khi kiểm định Wilcoxon
* \[ ] Thêm SHAP dependence plot (Bước 7)
* \[ ] Xây notebook Business Decision Support mới (Bước 8) — **đây là phần thầy nhấn mạnh nhất nhưng project chưa có gì**




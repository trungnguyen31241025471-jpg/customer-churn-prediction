# Research Gap Analysis \& Research Questions (Bước 1 — Chi Tiết)

> Tài liệu này mở rộng Bước 1 trong `lo-trinh-theo-de-cuong-giang-vien.md`, dựa trên việc đọc \*\*full-text\*\* (không chỉ abstract) 2 bài quan trọng nhất trong `06-tai-lieu-tham-khao/bang-so-sanh-literature-review.xlsx` — dùng làm minh chứng cụ thể cho từng luận điểm.

\---

## 1\. Bối cảnh \& Tầm quan trọng (Business Case)

* Theo Harvard Business Review, chi phí thu hút một khách hàng mới có thể cao gấp **5-25 lần** chi phí giữ chân một khách hàng hiện có — [HBR, 2014](https://hbr.org/2014/10/the-value-of-keeping-the-right-customers).
* Bài arXiv (Ekanayake \& De Alwis, 2025) trích dẫn thêm một nguồn khác (Çelik \& Osmanoğlu, 2019) cho rằng con số này có thể lên đến **10 lần** — cho thấy đây là một nhận định được nhiều nghiên cứu độc lập củng cố, không phải một thống kê đơn lẻ.
* **Churn** được định nghĩa là hiện tượng khách hàng chấm dứt quan hệ giao dịch — [Wikipedia — Churn rate](https://en.wikipedia.org/wiki/Churn_rate).

\---

## 2\. Bảng Phân Tích Khoảng Trống Có Minh Chứng (Gap Analysis Matrix)

So sánh trực tiếp giữa 2 bài đã đọc full-text, tóm tắt 4 bài còn lại (đọc ở mức abstract), và đề tài của bạn:

|Tiêu chí|Bài #1 (Boukrouh \& Azmani, 2024)|Bài #5 (Ekanayake \& De Alwis, 2025)|4 bài còn lại (mức abstract)|**Đề tài của bạn**|
|-|-|-|-|-|
|Nguồn dữ liệu|Kaggle **đã có nhãn sẵn** (2.841 khách, 16 đặc trưng)|**CÙNG** bộ Kaggle đó nhưng báo cáo **5.630 khách/20 đặc trưng** (khác số với bài #1!)|Chủ yếu Online Retail/Olist/Instacart|**Online Retail II** — giao dịch thô, tự tổng hợp customer-level|
|Định nghĩa churn|Nhãn có sẵn, không tự định nghĩa|Nhãn có sẵn, không tự định nghĩa|1 bài có sensitivity analysis ngưỡng (30/60/120 ngày)|**Tự định nghĩa qua observation/prediction window (3/6 tháng)**, có kiểm tra right-censoring|
|Time-based validation|Random 80/20 split|Random stratified 80/20 split|Không đề cập|**Walk-Forward Validation theo mốc cutoff**|
|Số mô hình so sánh|7 (DT, RF, SVM, LR, NB, KNN, ANN)|5 (LR, DT, RF, XGB, CatBoost)|1-3 mô hình mỗi bài|4 (LR, RF, XGBoost, LightGBM)|
|XAI: Global|✅ SHAP|✅ Tree SHAP|Có ở 2/4 bài|✅ SHAP|
|XAI: Dependence plot|❌ Không có|❌ Không có|❌ Không đề cập|🔲 Đang bổ sung (Bước 7)|
|XAI: Local|✅ LIME (chỉ 1 model)|✅ Tree SHAP local|Có ở 1/4 bài|✅ SHAP force plot|
|So sánh SHAP vs LIME cùng 1 model|❌ Không (SHAP cho ANN+RF, LIME chỉ ANN)|❌ Không dùng LIME|❌ Không|🔲 Cơ hội mở rộng|
|Survival Analysis|❌ Không|✅ Kaplan-Meier (trên trục "Tenure" có sẵn)|❌ Không|❌ Chưa làm (cơ hội mở rộng)|
|Kiểm định thống kê giữa models|❌ Không|❌ Không|❌ Không|✅ Wilcoxon signed-rank|
|Nhiều seed / robustness|❌ Không|❌ Không (chỉ 1 lần chạy CV)|❌ Không|✅ Walk-forward × nhiều seed|
|Business Decision Support tự động|❌ Không|🟡 Khuyến nghị định tính theo phân khúc RFM, không tự động hoá|❌ Không|🔲 Đang xây (Bước 8)|

\---

## 3\. Diễn Giải Minh Chứng Cụ Thể

### 3.1. Cả 2 bài quan trọng nhất đều dùng dữ liệu đã dán nhãn sẵn, không phải giao dịch thô

Đây là khác biệt nền tảng nhất. Bài #1 báo cáo bộ dữ liệu Kaggle của Ankit Verma có 2.841 khách hàng, 16 đặc trưng. Bài #5 dùng **đúng bộ dữ liệu đó** (cùng trích dẫn tác giả Ankit Verma) nhưng báo cáo 5.630 bản ghi khách hàng với 20 đặc trưng trước khi làm sạch. Hai con số này **không khớp nhau** dù cùng nguồn — cho thấy dấu hiệu về vấn đề **reproducibility** trong dòng nghiên cứu này (có thể do phiên bản dataset trên Kaggle đã thay đổi theo thời gian, hoặc mỗi nhóm tác giả tự lọc bớt dữ liệu theo tiêu chí riêng mà không công bố đầy đủ).

Quan trọng hơn: **cả hai bài đều không làm việc trên log giao dịch thô** — họ nhận một bảng đặc trưng tĩnh (Tenure, Complain, CashbackAmount...) đã được ai đó tính sẵn, không phải tự tổng hợp từ hàng nghìn dòng hoá đơn như Online Retail II. Điều này có nghĩa là **không bài nào trong 2 bài này thực sự giải quyết bài toán non-contractual churn từ dữ liệu giao dịch** — họ giải quyết một bài toán phân loại nhị phân thông thường trên dữ liệu đã được "đóng gói sẵn".

### 3.2. Chính tác giả bài #5 tự thừa nhận khoảng trống về Survival Analysis trong e-commerce

Bài arXiv viết rõ (paraphrase): mặc dù Kaplan-Meier và Cox proportional hazards đã được dùng trong viễn thông và game online, theo hiểu biết của các tác giả, **chưa có tài liệu survival analysis nào công bố cho lĩnh vực e-commerce** trước nghiên cứu của họ. Đây là tự nhận định của chính tác giả, không phải suy luận của mình — nhưng ngay cả nghiên cứu "đầu tiên" này cũng chỉ áp dụng Kaplan-Meier trên trục **Tenure có sẵn** trong dataset tĩnh, chứ không phải trên chuỗi thời gian giao dịch thực tế như Online Retail II.

### 3.3. Không bài nào dùng Time-based Split

Cả hai bài đều dùng **random (stratified) train/test split 80:20** — đúng loại lỗi phương pháp luận mà giảng viên của bạn đã chỉ ra cần tránh (xem `lo-trinh-theo-de-cuong-giang-vien.md`, Bước 5). Điều thú vị là: đây không chỉ là điểm thầy yêu cầu sửa cho project của bạn, mà còn là **khoảng trống chung của cả dòng nghiên cứu này** — nếu bạn làm đúng Walk-Forward Validation theo thời gian, đây là một điểm mạnh phương pháp luận thực sự so với literature hiện có, không chỉ là "làm theo yêu cầu bài tập".

### 3.4. Business Decision Support: có nhắc đến nhưng chưa ai tự động hoá

Bài #5 có phần khuyến nghị theo phân khúc RFM (ví dụ nhóm "Lost" nên nhận ưu đãi win-back, nhóm "Best" nên nhận loyalty reward) — nhưng đây là khuyến nghị **định tính, viết bằng lời**, không phải một hệ thống tự động ánh xạ `Customer → Xác suất → SHAP driver → Action cụ thể` như đề cương giảng viên yêu cầu ở Bước 8. Đây là khoảng trống rõ ràng bạn có thể lấp đầy.

\---

## 4\. Research Questions Chính Thức

|RQ|Câu hỏi|Minh chứng cho khoảng trống dẫn tới câu hỏi này|
|-|-|-|
|**RQ1**|Có thể dự đoán khách hàng churn trong 3/6 tháng tới với độ chính xác đến mức nào, khi churn được tự định nghĩa trực tiếp từ dữ liệu giao dịch thô (không dùng nhãn có sẵn)?|Cả bài #1 và #5 đều dùng nhãn churn có sẵn từ Kaggle, **không bài nào tự định nghĩa và kiểm định churn qua observation/prediction window trên dữ liệu giao dịch thô** như Online Retail II|
|**RQ2**|Yếu tố hành vi nào (RFM mở rộng, xu hướng chi tiêu/tần suất, tỷ lệ huỷ đơn) ảnh hưởng mạnh nhất đến churn, và liệu các đặc trưng hành vi theo thời gian này có bổ sung giá trị dự báo so với RFM cơ bản?|Cả 2 bài dùng đặc trưng tĩnh có sẵn (Tenure, Complain...), **không có bài nào kiểm định định lượng việc thêm đặc trưng hành vi theo thời gian (trend, độ đều đặn) có cải thiện AUC có ý nghĩa thống kê hay không** — đây chính là phép so sánh Ablation đã làm ở `nang-cao-sensitivity-feature-nested-cv.ipynb`|
|**RQ3**|Có thể chuyển kết quả dự đoán + giải thích XAI thành một hệ thống hỗ trợ quyết định kinh doanh (Customer → Probability → Driver → Action) một cách có hệ thống, tự động hay không?|Bài #5 có đề xuất khuyến nghị theo phân khúc nhưng **chỉ ở mức định tính**, chưa có bài nào trong 6 bài xây dựng bảng ánh xạ tự động từ SHAP driver sang hành động cụ thể cho từng khách hàng|

\---

## 5\. Giả thuyết Nghiên Cứu (Hypotheses) Liên Kết Với RQ

* **H1** (liên kết RQ1): Mô hình XGBoost/LightGBM huấn luyện trên đặc trưng tự tổng hợp từ Online Retail II đạt ROC-AUC/PR-AUC ổn định (độ lệch chuẩn thấp) qua nhiều fold Walk-Forward, chứng tỏ định nghĩa churn theo observation/prediction window là khả thi và đáng tin cậy dù không có nhãn "chính thức" như các bộ dữ liệu Kaggle đã gán sẵn.
* **H2** (liên kết RQ2): Bộ đặc trưng RFM mở rộng (thêm IntervalStd, SpendingTrend, FrequencyTrend, RepeatPurchaseRatio, CancelRate) cho AUC cao hơn **có ý nghĩa thống kê** (kiểm định Wilcoxon, p<0.05) so với chỉ dùng RFM cơ bản.
* **H3** (liên kết RQ3): Một khung quy tắc đơn giản ánh xạ từ SHAP driver chính sang hành động retention cụ thể có thể xây dựng được ngay từ kết quả mô hình hiện có, không cần thêm dữ liệu mới.

\---

## 6\. Tuyên Bố Đóng Góp (Contribution Statement)

Đoạn văn sau có thể dùng gần như trực tiếp trong phần Introduction của bài viết:

> Khác với các nghiên cứu trước đây về dự đoán churn e-commerce có XAI — vốn chủ yếu áp dụng trên các bộ dữ liệu đã được dán nhãn sẵn và chia tách ngẫu nhiên — nghiên cứu này (1) tự định nghĩa và kiểm định độ nhạy của nhãn churn trực tiếp từ dữ liệu giao dịch thô (Online Retail II) qua nhiều mốc quan sát, (2) áp dụng Time-based Walk-Forward Validation để đánh giá mô hình đúng với bối cảnh triển khai thực tế theo thời gian, (3) định lượng bằng kiểm định thống kê giá trị gia tăng của các đặc trưng hành vi theo thời gian so với RFM cơ bản, và (4) chuyển hoá kết quả XAI thành một khung hỗ trợ quyết định kinh doanh cụ thể, có thể hành động được ngay ở cấp độ từng khách hàng.

\---

## 


> 📚 [Mục lục](README.md) · ← [Phần 07: Data Preprocessing](phan-07-data-preprocessing.md) · [Phần 11: Toán học & Thống kê nền tảng](phan-11-toan-thong-ke.md) →

## Phần 8: Model Evaluation (Đánh giá mô hình)

> 🔑 **Hiểu nhanh trong 1 câu**: Chấm điểm xem mô hình dự đoán tốt đến đâu — nhưng "tốt" phải đo đúng cách, vì có nhiều kiểu "tốt" khác nhau tùy vào cái gì quan trọng hơn với bài toán.
> 🌍 **Ví dụ đời thường**: Giống như chấm một bài thi — không chỉ đếm "đúng bao nhiêu câu trên tổng số" (Accuracy), mà còn phải xem thí sinh đúng nhiều ở câu dễ hay câu khó, có bỏ sót câu quan trọng nào không (Recall) — hai học sinh cùng đúng 85% câu hỏi nhưng một người bỏ sót toàn câu khó thì đáng lo hơn nhiều.
> 📌 **Xem thực hành đầy đủ (Nested CV, nhiều seed)**: `../05-thuc-hanh/nang-cao-sensitivity-feature-nested-cv.ipynb` (Phần 3)

### 8.1 Confusion Matrix — ví dụ số cụ thể

Giả sử trên 1000 khách hàng test, trong đó 200 người thực sự churn:

| | Dự đoán: Churn | Dự đoán: Không churn |
|---|---|---|
| **Thực tế: Churn** (200 người) | 150 (True Positive) | 50 (False Negative) |
| **Thực tế: Không churn** (800 người) | 100 (False Positive) | 700 (True Negative) |

Từ bảng này: **Precision** = 150/(150+100) = **60%**, **Recall** = 150/(150+50) = **75%**, **Accuracy** = (150+700)/1000 = **85%**. Chú ý: dù Accuracy trông "cao" (85%), Precision chỉ 60% nghĩa là gần 40% khách hàng bạn nhắm retention thực ra không hề có ý định rời bỏ — đây là lý do không nên chỉ nhìn Accuracy.

### 8.2 Các chỉ số đánh giá

| Chỉ số | Công thức | Ý nghĩa với ví dụ trên |
|---|---|---|
| **Accuracy** | (TP+TN)/Tổng | 85% — dễ gây hiểu lầm khi mất cân bằng lớp |
| **Precision** | TP/(TP+FP) | 60% — trong số dự đoán churn, 60% đúng |
| **Recall** | TP/(TP+FN) | 75% — bắt được 75% khách thực sự churn |
| **F1-score** | Trung bình điều hòa Precision & Recall | 2×(0.6×0.75)/(0.6+0.75) ≈ **67%** |
| **ROC-AUC** | Diện tích dưới đường cong ROC | Đo khả năng phân biệt tổng thể ở mọi ngưỡng, không chỉ ngưỡng 0.5 |
| **PR-AUC** | Diện tích dưới đường cong Precision-Recall | Phù hợp hơn ROC-AUC khi lớp churn hiếm (như ví dụ 16% ở trên) |
| **Precision@Top-K%** | Precision khi chỉ xét K% xác suất churn cao nhất | Gắn với thực tế: ngân sách retention có hạn, chỉ nhắm 10-20% rủi ro cao nhất |

### 8.3 Cross-validation và Nested Cross-validation

**K-fold Cross-validation** (ví dụ K=5): chia 1000 khách hàng thành 5 phần bằng nhau (200 người/phần), luân phiên dùng 4 phần (800 người) để train và 1 phần (200 người) để test, lặp lại 5 lần rồi lấy trung bình kết quả — đáng tin cậy hơn nhiều so với chỉ chia 1 lần.

**Nested Cross-validation**: dùng vòng lặp ngoài để đánh giá hiệu năng thật, vòng lặp trong (chỉ trên phần train của vòng ngoài) để tìm hyperparameter tối ưu — tránh rò rỉ thông tin từ tập test vào quá trình chọn mô hình.

### 8.4 Kiểm định ý nghĩa thống kê

Ví dụ: chạy Random Forest và XGBoost mỗi loại 10 lần (10 seed khác nhau), thu được AUC trung bình: Random Forest = 0.82 ± 0.02, XGBoost = 0.85 ± 0.015. Dùng **Wilcoxon signed-rank test** trên 10 cặp AUC để kiểm tra: XGBoost có thực sự tốt hơn có ý nghĩa thống kê, hay chênh lệch 0.03 chỉ là ngẫu nhiên? Nếu p-value < 0.05 → khác biệt đáng tin cậy.

📎 **Tìm hiểu thêm:**
- [StatQuest — Machine Learning Fundamentals: The Confusion Matrix](https://www.youtube.com/watch?v=Kdsp6soqA7o)
- [StatQuest — ROC and AUC, Clearly Explained!](https://www.youtube.com/watch?v=4jRBRDbJemM)

---


> 📚 [Mục lục](README.md) · ← [Phần 07: Data Preprocessing](phan-07-data-preprocessing.md) · [Phần 11: Toán học & Thống kê nền tảng](phan-11-toan-thong-ke.md) →

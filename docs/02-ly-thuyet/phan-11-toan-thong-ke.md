> 📚 [Mục lục](README.md) · ← [Phần 08: Model Evaluation](phan-08-model-evaluation.md) · [Phần 12: Python & Công cụ lập trình](phan-12-python-cong-cu.md) →

## Phần 11: Toán học & Thống kê nền tảng

> 🔑 **Hiểu nhanh trong 1 câu**: Đây là "ngôn ngữ" ẩn phía sau mọi thuật toán ML — không cần giỏi toán hàn lâm, nhưng cần hiểu trực giác để không dùng công cụ như một "hộp đen" mù quáng.
> 🌍 **Ví dụ đời thường**: Giống như lái xe không cần hiểu hết cơ khí động cơ, nhưng biết đạp ga thì xe tăng tốc, đạp phanh thì xe chậm lại — hiểu đủ để lái an toàn và biết khi nào xe có vấn đề bất thường.

### 11.1 Đại số tuyến tính (Linear Algebra) cơ bản

Dữ liệu ML biểu diễn dưới dạng **ma trận** (mỗi hàng = một khách hàng, mỗi cột = một đặc trưng) và **vector**. Logistic Regression về bản chất tính `z = X · w` (nhân ma trận dữ liệu X với vector trọng số w), trước khi đưa qua hàm sigmoid.

### 11.2 Giải tích cơ bản & Gradient Descent (ví dụ số từng bước)

Giả sử ta có 1 tham số w và loss function đơn giản `Loss(w) = (w - 5)²` (giá trị tối ưu thực sự là w=5, nhưng máy không biết trước). Gradient Descent bắt đầu đoán ngẫu nhiên w=0:

| Bước | w hiện tại | Đạo hàm (2×(w−5)) | w mới = w − learning_rate×đạo_hàm (learning_rate=0.1) |
|---|---|---|---|
| 1 | 0 | −10 | 0 − 0.1×(−10) = 1.0 |
| 2 | 1.0 | −8 | 1.0 − 0.1×(−8) = 1.8 |
| 3 | 1.8 | −6.4 | 1.8 − 0.1×(−6.4) = 2.44 |
| ... | ... | ... | dần tiến về 5.0 |

Đây chính là cách hầu hết mô hình ML "học" — lặp đi lặp lại điều chỉnh nhỏ theo hướng ngược gradient cho đến khi hội tụ.

### 11.3 Xác suất & Thống kê

- **p-value**: xác suất quan sát được kết quả cực đoan như đã thấy (hoặc hơn) *nếu giả thuyết H0 đúng*. Ví dụ: nếu bạn kiểm định "Recency của nhóm churn khác nhóm không churn" và p-value = 0.002, nghĩa là chỉ có 0.2% khả năng chênh lệch này xảy ra do ngẫu nhiên nếu thực ra không có khác biệt gì — rất đáng tin để kết luận có khác biệt thật.
- **Khoảng tin cậy 95%**: nếu ROC-AUC trung bình qua 10 lần chạy là 0.85 với khoảng tin cậy 95% là [0.82, 0.88], nghĩa là bạn tin tưởng 95% rằng AUC thực sự nằm trong khoảng đó, không chỉ báo một con số 0.85 đơn lẻ có thể gây hiểu lầm về độ chắc chắn.
- **Lỗi loại I/II**: Lỗi loại I = kết luận "XGBoost tốt hơn Random Forest" trong khi thực ra chúng ngang nhau (báo động giả). Lỗi loại II = kết luận "không có khác biệt" trong khi thực ra XGBoost tốt hơn thật (bỏ lỡ phát hiện thật).

📎 **Tìm hiểu thêm:**
- [3Blue1Brown — Essence of Linear Algebra (playlist đầy đủ, trực quan bằng hình ảnh)](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [StatQuest — Stochastic Gradient Descent, Clearly Explained](https://statquest.org/stochastic-gradient-descent-clearly-explained/)

---


> 📚 [Mục lục](README.md) · ← [Phần 08: Model Evaluation](phan-08-model-evaluation.md) · [Phần 12: Python & Công cụ lập trình](phan-12-python-cong-cu.md) →

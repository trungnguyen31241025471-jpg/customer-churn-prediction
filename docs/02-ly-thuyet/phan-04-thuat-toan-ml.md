> 📚 [Mục lục](README.md) · ← [Phần 03: Customer Churn Prediction](phan-03-customer-churn.md) · [Phần 05: Feature Engineering](phan-05-feature-engineering.md) →

## Phần 4: Các họ thuật toán Machine Learning (phân loại theo nguyên lý)

> 🔑 **Hiểu nhanh trong 1 câu**: Có nhiều "cách suy luận" khác nhau để đi từ dữ liệu đến dự đoán — không có cách nào luôn luôn tốt nhất, mỗi cách có điểm mạnh/yếu riêng.
> 🌍 **Ví dụ đời thường**: Giống như có nhiều kiểu bác sĩ chẩn đoán bệnh — một người áp dụng một quy tắc rõ ràng duy nhất (Decision Tree: "nếu sốt trên 39 độ thì..."), một người triệu tập 300 đồng nghiệp cho ý kiến rồi lấy biểu quyết đa số (Random Forest), một người dựa vào việc so sánh với các ca bệnh tương tự từng gặp (KNN).

### 4.1 Linear Models — Logistic Regression

M� hình hóa xác suất churn bằng hàm sigmoid áp lên tổ hợp tuyến tính của đặc trưng. Ví dụ cụ thể: giả sử mô hình học được công thức `z = 0.02 × Recency − 0.15 × Frequency − 0.0001 × Monetary`. Với khách hàng B ở trên (Recency=150, Frequency=2, Monetary=300.000): `z = 0.02×150 − 0.15×2 − 0.0001×300000 = 3 − 0.3 − 30 = -27.3` → qua hàm sigmoid ra xác suất gần 0 hoặc gần 1 tùy hệ số thực tế đã học được. Hệ số dương/âm cho biết ngay chiều ảnh hưởng — đây là lý do mô hình này **intrinsic interpretable**.

### 4.2 Tree-based Models — Decision Tree

Xây cấu trúc cây gồm các nút "nếu đặc trưng > ngưỡng thì rẽ nhánh". Ví dụ luật cây đơn giản học được từ dữ liệu:
```
NẾU Recency > 90 ngày:
    NẾU Frequency <= 2:  → Dự đoán: CHURN (xác suất 82%)
    NGƯỢC LẠI:           → Dự đoán: KHÔNG CHURN (xác suất 65%)
NGƯỢC LẠI:
    → Dự đoán: KHÔNG CHURN (xác suất 90%)
```
Tiêu chí chọn điểm chia dựa trên **Gini impurity** hoặc **Information Gain**. Dễ giải thích khi cây nông, dễ overfitting khi cây quá sâu.

### 4.3 Ensemble Methods — Học kết hợp

- **Bagging**: huấn luyện nhiều cây độc lập trên các tập con dữ liệu lấy mẫu ngẫu nhiên có hoàn lại (bootstrap), rồi lấy trung bình/biểu quyết. **Random Forest** — ví dụ 300 cây, mỗi cây "vote" churn hay không, kết quả cuối là tỷ lệ phiếu (vd 210/300 cây vote churn → xác suất 70%).
- **Boosting**: huấn luyện tuần tự, mỗi mô hình sau sửa lỗi (residual) của mô hình trước. **XGBoost/LightGBM** — thường đạt độ chính xác cao nhất trong các mô hình cổ điển.

### 4.4 Instance-based Learning — K-Nearest Neighbors (KNN)

"Lazy learning" — khi dự đoán một khách hàng mới, tìm K khách hàng huấn luyện **gần nhất** (theo khoảng cách Euclidean giữa các vector RFM) và lấy biểu quyết đa số. Ví dụ K=5: tìm 5 khách hàng có RFM gần giống khách hàng mới nhất, nếu 4/5 người đó đã churn → dự đoán khách mới cũng churn.

### 4.5 Probabilistic Models — Naive Bayes

Dựa trên định lý Bayes, giả định các đặc trưng độc lập có điều kiện khi biết nhãn. Giả định "ngây thơ" này hiếm khi đúng hoàn toàn nhưng vẫn hoạt động tốt khi dữ liệu ít.

### 4.6 Kernel-based Methods — Support Vector Machine (SVM)

Tìm siêu phẳng phân chia hai lớp sao cho **lề (margin)** lớn nhất. Với dữ liệu không phân chia tuyến tính được, dùng **kernel trick** ánh xạ sang không gian nhiều chiều hơn.

### 4.7 Neural Networks — ANN và các biến thể chuỗi thời gian

**ANN** mô phỏng cấu trúc nơ-ron sinh học qua nhiều lớp kết nối, trọng số học qua backpropagation (xem chi tiết ở Phần 13). Với dữ liệu chuỗi thời gian (chuỗi giao dịch theo thời gian của một khách hàng), **LSTM/GRU** phù hợp hơn để nắm bắt hành vi biến đổi theo thời gian thay vì chỉ dùng RFM tĩnh.

📎 **Tìm hiểu thêm:**
- [scikit-learn — Decision Trees User Guide](https://scikit-learn.org/stable/modules/tree.html)
- [scikit-learn — Tài liệu LogisticRegression đầy đủ tham số](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [3Blue1Brown — But what is a neural network? (video, cực kỳ trực quan)](https://www.youtube.com/watch?v=aircAruvnKk)

---


> 📚 [Mục lục](README.md) · ← [Phần 03: Customer Churn Prediction](phan-03-customer-churn.md) · [Phần 05: Feature Engineering](phan-05-feature-engineering.md) →

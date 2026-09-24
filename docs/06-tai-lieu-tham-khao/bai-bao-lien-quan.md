# Các Bài Báo Liên Quan Đến Đề Tài

Danh sách các bài báo gần với đề tài "Explainable Machine Learning for Predicting Customer Churn in E-commerce", dùng để tham khảo khi viết phần Related Work.

## Sát nhất về đề tài (Explainable ML + churn + e-commerce)

### 1. Explainable machine learning models applied to predicting customer churn for e-commerce
- **Nguồn**: [IAES International Journal of Artificial Intelligence (IJ-AI), 2024](https://ijai.iaescore.com/index.php/IJAI/article/view/25293)
- **Phương pháp**: 7 mô hình ML (Decision Tree, Random Forest, SVM, Logistic Regression, Naive Bayes, KNN, ANN) kết hợp SHAP và LIME.
- **Ghi chú**: Gần như cùng tiêu đề với đề tài của bạn — cần đọc kỹ để định vị rõ điểm khác biệt. Gợi ý điểm khác biệt: (1) tập trung cụ thể vào cửa sổ dự đoán 3/6 tháng thay vì churn chung chung, (2) áp dụng riêng trên Online Retail II, (3) so sánh sâu nhiều phương pháp XAI thay vì chỉ SHAP+LIME.

### 2. Customer Churn Prediction in E-Commerce Using ML Models for Digital Marketing Trends
- **Nguồn**: [ACM ICBDEIM 2025](https://dl.acm.org/doi/10.1145/3800000.3800153)
- **Phương pháp**: Đặc trưng mới "Tenure Per Device" (hành vi đa thiết bị), XGBoost kết hợp SMOTE, giải thích bằng SHAP và Partial Dependence Plot.
- **Ghi chú**: Tham khảo cách trình bày phần feature engineering + explainability.

## Cùng dùng bộ dữ liệu Online Retail (đáng tham khảo về phương pháp)

### 3. A novel hybrid deep learning framework for customer churn prediction using RFM and embedding clustering
- **Nguồn**: [Scientific Reports, 2026](https://www.nature.com/articles/s41598-026-53220-0)
- **Phương pháp**: RFM + Deep Embedded Clustering + GRU/LSTM, đánh giá trên Online Retail và một bộ dữ liệu Events khác.
- **Ghi chú**: Có phân tích độ nhạy ngưỡng churn (30/60/120 ngày) — kỹ thuật sensitivity analysis nên áp dụng ở bước gán nhãn churn.

### 4. Enhancing customer retention in Online Retail through churn prediction: A hybrid RFM, K-means, and deep neural network approach
- **Nguồn**: [ScienceDirect / Expert Systems with Applications, 2025](https://www.sciencedirect.com/science/article/abs/pii/S0957417425020846)
- **Phương pháp**: RFM + K-means + LSTM/GRU, kiểm chứng trên Olist, Instacart và Online Retail.
- **Ghi chú**: Hướng dùng nhiều bộ dữ liệu để tăng tính tổng quát — nên tham khảo nếu bổ sung bộ dữ liệu thứ 2.

## Hướng phương pháp bổ sung có thể tạo điểm khác biệt cho đóng góp mới

### 5. Explainability, risk modeling, and segmentation based customer churn analytics for personalized retention in e-commerce
- **Nguồn**: [arXiv, 2025](https://arxiv.org/abs/2510.11604)
- **Phương pháp**: Khung 3 thành phần — XAI để định lượng đóng góp đặc trưng, Survival Analysis để mô hình hóa rủi ro churn theo thời gian, RFM profiling để phân khúc khách hàng.
- **Ghi chú**: Nếu muốn tạo điểm khác biệt rõ ràng, cân nhắc bổ sung góc nhìn survival analysis (time-to-churn) bên cạnh bài toán phân loại nhị phân 3/6 tháng — hướng khá mới, ít bài kết hợp đầy đủ.

### 6. A Fuzzy-XAI Framework for Customer Segmentation and Risk Detection: Integrating RFM, 2-Tuple Modeling, and Strategic Scoring
- **Nguồn**: [MDPI Mathematics, 2025](https://doi.org/10.3390/math13132141)
- **Phương pháp**: Fuzzy C-Means trên RFM chuẩn hóa, ánh xạ sang thang ngôn ngữ 2-tuple, XGBoost để kiểm chứng tính nhất quán phân khúc mờ, SHAP/LIME để giải thích.
- **Ghi chú**: Hướng mở rộng explainability ngoài SHAP/LIME thông thường nếu muốn làm phong phú phần XAI.

## Ghi chú tổng hợp

- Vì đã có ít nhất 2 bài (Scientific Reports, ScienceDirect) cũng dùng chính bộ Online Retail cho churn, nên nêu rõ trong phần Related Work là baseline/kết quả của họ để so sánh, hoặc chọn hướng đóng góp không trùng.
- Khoảng trống đáng cân nhắc: so sánh tính ổn định của nhiều phương pháp XAI với nhau (SHAP vs LIME vs permutation importance) trên bài toán churn 3/6 tháng cụ thể — chưa bài nào ở trên làm sâu điểm này.
- Ngoài các bài báo học thuật, có nhiều repo GitHub thực hành RFM + churn trên Online Retail II — không dùng để trích dẫn học thuật, nhưng có thể tham khảo cách xử lý dữ liệu và định nghĩa cửa sổ churn.

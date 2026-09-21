# 🛒 Customer Churn Prediction: Ứng dụng Machine Learning trong Bán lẻ

## 📌 Tổng quan dự án (Project Overview)
Dự án này ứng dụng các thuật toán Học máy (Machine Learning) để dự đoán xác suất rời bỏ (Churn) của khách hàng dựa trên lịch sử giao dịch. Khác với các bài toán phân loại thông thường, dự án tập trung vào phân tích chuỗi thời gian của hành vi mua sắm, từ đó cung cấp các **Insight có thể hành động (Actionable Insights)** giúp bộ phận kinh doanh tối ưu hóa chi phí giữ chân khách hàng (Customer Retention Cost).

## 🎯 Mục tiêu Nghiệp vụ (Business Objectives)
* **Nhận diện rủi ro:** Phát hiện sớm các khách hàng có dấu hiệu giảm dần tương tác hoặc thay đổi tính chu kỳ mua sắm.
* **Tối ưu ngân sách:** Cung cấp điểm xác suất (Probability Score) để phòng Marketing phân bổ chính xác ngân sách khuyến mãi, tránh tặng voucher lãng phí cho khách hàng không có nguy cơ rời đi.
* **Phân tích hành vi:** Giải thích nguyên nhân rời bỏ thông qua phân rã các đặc trưng nâng cao (Explainable AI).

## 🗂️ Cấu trúc Kho lưu trữ (Repository Structure)
```text
customer-churn-prediction/
├── data/               # Thư mục chứa dữ liệu thô (đã ẩn qua .gitignore để bảo mật)
├── docs/               # Các biểu đồ phân tích EDA, ma trận tương quan và báo cáo giải thích
├── notebooks/          # File Jupyter Notebook (01_eda_and_cleaning.ipynb) dùng để trực quan hóa
├── src/                # Mã nguồn Python xử lý tính năng RFM và huấn luyện mô hình
├── .gitignore          # Cấu hình bỏ qua các file rác và dữ liệu nhạy cảm
└── README.md           # Tài liệu tổng quan dự án
```

## 🧠 Phương pháp tiếp cận (Methodology)
1. **Tiền xử lý (Data Cleaning):** Làm sạch dòng tiền, loại bỏ các hóa đơn hủy và các mã dịch vụ phi sản phẩm (POST, BANK CHARGES) để bảo toàn tính nguyên bản của vòng đời khách hàng.
2. **Feature Engineering:**
   * Trích xuất mô hình **RFM** (Recency, Frequency, Monetary).
   * Lượng hóa "sự thất thường" thông qua **Độ lệch chuẩn khoảng cách mua (IntervalStd)**.
   * Tính toán **Gia tốc chi tiêu (Spending Trends)** so sánh 3 tháng gần nhất với 3 tháng trước đó.
3. **Time-based Walk-Forward Validation:** Sử dụng kỹ thuật cuộn mốc thời gian để huấn luyện và kiểm thử, ngăn chặn tuyệt đối hiện tượng rò rỉ dữ liệu (Data Leakage) thường gặp trong bài toán chuỗi sự kiện.

## 🛠️ Công nghệ & Thư viện (Tech Stack)
* **Ngôn ngữ:** Python 3.10
* **Xử lý dữ liệu:** `pandas`, `numpy`
* **Trực quan hóa:** `matplotlib`, `seaborn`
* **Mô hình Máy học:** `scikit-learn` (Logistic Regression, Random Forest), `xgboost`, `lightgbm`
* **Đánh giá thống kê:** `scipy` (Kiểm định Wilcoxon)

## 📊 Kết quả nổi bật (Key Results)
* Giải quyết thành công bài toán **Mất cân bằng dữ liệu (Imbalanced Data)** bằng cách sử dụng thang đo PR-AUC (Precision-Recall Area Under Curve) thay vì Accuracy.
* Mô hình Tree-based (Random Forest / LightGBM) vượt trội trong việc nắm bắt các quy tắc phi tuyến tính của khách lẻ B2C và khách sỉ B2B.
* Khẳng định tính hiệu quả của các biến xu hướng (Trend) bằng phương pháp Ablation Study với mức ý nghĩa thống kê p-value < 0.05.

## 🚀 Hướng dẫn cài đặt (How to Run)
1. Clone dự án về máy:
   ```bash
   git clone https://github.com/your-username/customer-churn-prediction.git
   cd customer-churn-prediction
   ```
2. Cài đặt các thư viện yêu cầu:
   ```bash
   pip install pandas numpy scikit-learn xgboost lightgbm matplotlib seaborn scipy
   ```
3. Đặt file dữ liệu `online_retail_II.csv` vào thư mục `data/` và chạy file notebook trong thư mục `notebooks/`.

---
*Dự án được thực hiện nhằm mục đích nghiên cứu ứng dụng Khoa học dữ liệu vào Phân tích Nghiệp vụ.*


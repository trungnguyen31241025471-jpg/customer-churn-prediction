> 📚 [Mục lục](README.md) · ← [Phần 05: Feature Engineering](phan-05-feature-engineering.md) · [Phần 07: Data Preprocessing](phan-07-data-preprocessing.md) →

## Phần 6: EDA (Exploratory Data Analysis) chi tiết

> 🔑 **Hiểu nhanh trong 1 câu**: "Nhìn" và "cảm nhận" dữ liệu bằng biểu đồ và số liệu thống kê TRƯỚC KHI làm bất cứ điều gì với nó — không nhảy thẳng vào xây mô hình.
> 🌍 **Ví dụ đời thường**: Giống như một thám tử quan sát kỹ hiện trường (dấu vân tay, đồ vật bị xáo trộn) trước khi đưa ra kết luận, thay vì đoán mò ngay từ đầu. Bỏ qua EDA giống như một bác sĩ kê đơn mà chưa khám bệnh.
> 📌 **Xem thực hành đầy đủ (10 bước, có biểu đồ thật)**: `../05-thuc-hanh/eda-va-tien-xu-ly-du-lieu.ipynb`

### 6.1 Phân tích đơn biến (Univariate)

Ví dụ cụ thể: vẽ histogram của Monetary trên toàn bộ khách hàng — thường thấy phân phối lệch phải mạnh (right-skewed): đa số khách hàng chi tiêu thấp (dưới 1 triệu), nhưng một số ít khách bán buôn chi tiêu cực lớn (trên 50 triệu) kéo dài đuôi phân phối. Boxplot giúp nhìn ngay outlier: các điểm nằm ngoài "râu" (whisker) của boxplot.

### 6.2 Phân tích song biến (Bivariate)

Ví dụ: so sánh phân phối Recency giữa nhóm churn và không churn bằng 2 boxplot cạnh nhau — nếu nhóm churn có Recency trung vị 95 ngày còn nhóm không churn chỉ 12 ngày, đây là tín hiệu Recency rất mạnh để phân biệt hai nhóm.

### 6.3 Phân tích đa biến (Multivariate)

Ma trận tương quan (correlation heatmap): ví dụ nếu Frequency và Monetary có hệ số tương quan 0.85 (rất cao) — đây là dấu hiệu **đa cộng tuyến (multicollinearity)**, có thể cần loại bớt một trong hai hoặc kết hợp thành một đặc trưng (AvgOrderValue = Monetary/Frequency).

### 6.4 Kiểm định thống kê trong EDA

Dùng t-test để kiểm tra: "Recency trung bình của nhóm churn (95 ngày) có thực sự khác biệt có ý nghĩa thống kê so với nhóm không churn (12 ngày), hay chỉ là ngẫu nhiên?" — nếu p-value < 0.05 thì khác biệt này đáng tin cậy (xem thêm Phần 11.3 về p-value).

📎 **Tìm hiểu thêm:**
- [seaborn — Tài liệu chính thức (histplot, boxplot, heatmap...)](https://seaborn.pydata.org/)
- [Real Python — Hướng dẫn pandas GroupBy chi tiết](https://realpython.com/pandas-groupby/)

---


> 📚 [Mục lục](README.md) · ← [Phần 05: Feature Engineering](phan-05-feature-engineering.md) · [Phần 07: Data Preprocessing](phan-07-data-preprocessing.md) →

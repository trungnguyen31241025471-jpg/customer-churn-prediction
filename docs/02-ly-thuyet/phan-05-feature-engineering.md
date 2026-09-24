> 📚 [Mục lục](README.md) · ← [Phần 04: Các họ thuật toán Machine Learning](phan-04-thuat-toan-ml.md) · [Phần 06: EDA (Exploratory Data Analysis)](phan-06-eda.md) →

## Phần 5: Feature Engineering chi tiết

> 🔑 **Hiểu nhanh trong 1 câu**: Biến dữ liệu giao dịch thô (từng dòng mua hàng) thành các "chỉ số tổng hợp" có ý nghĩa mà mô hình học được, thay vì đưa dữ liệu thô vào thẳng.
> 🌍 **Ví dụ đời thường**: Giống như đầu bếp không ném nguyên con cá lên bàn ăn — phải sơ chế (làm sạch, thái lát, ướp gia vị) trước. Feature Engineering chính là bước "sơ chế" dữ liệu: từ hàng nghìn dòng giao dịch của một khách hàng, "cô đặc" lại thành vài con số như Recency, Frequency, Monetary dễ tiêu hoá hơn cho mô hình.
> 📌 **Xem thêm thực hành chi tiết**: `../05-thuc-hanh/giai-thich-ky-thuat-eda-tien-xu-ly-feature-engineering.md` áp dụng các kỹ thuật dưới đây trực tiếp lên Online Retail II, kèm code và lý do cụ thể.

### 5.1 Mở rộng RFM (ví dụ số)

Ngoài R-F-M gốc, có thể tính thêm: độ lệch chuẩn khoảng cách giữa các lần mua (ví dụ khách A mua đều đặn mỗi 10±2 ngày → độ lệch chuẩn nhỏ = hành vi ổn định; khách B mua lúc thì cách 5 ngày lúc thì cách 100 ngày → độ lệch chuẩn lớn = hành vi thất thường, rủi ro cao hơn), xu hướng chi tiêu (so sánh chi tiêu 3 tháng gần nhất với 3 tháng trước đó — nếu giảm liên tục là tín hiệu cảnh báo sớm), tỷ lệ đơn hàng bị huỷ/trả lại, số danh mục sản phẩm khác nhau đã mua (đo mức độ đa dạng hành vi).

### 5.2 Encoding biến phân loại (ví dụ cụ thể)

Với cột Country có giá trị "United Kingdom", "France", "Germany":
- **One-Hot Encoding**: tạo 3 cột nhị phân `Country_UK`, `Country_France`, `Country_Germany` (giá trị 0/1).
- **Label Encoding**: gán UK=0, France=1, Germany=2 — chỉ nên dùng khi có thứ tự tự nhiên (không phù hợp cho Country vì không có thứ tự).
- **Target Encoding**: thay Country bằng tỷ lệ churn trung bình của quốc gia đó (ví dụ UK có churn rate trung bình 15%, thay toàn bộ dòng UK bằng 0.15) — cần cẩn thận tránh rò rỉ dữ liệu (data leakage) khi tính tỷ lệ này chỉ trên tập train.

### 5.3 Feature Selection

- **Filter methods**: tương quan Pearson, Mutual Information, Chi-square test — chọn dựa trên thống kê độc lập với mô hình.
- **Wrapper methods**: Recursive Feature Elimination — thử nghiệm tổ hợp đặc trưng bằng cách huấn luyện mô hình thật nhiều lần.
- **Embedded methods**: regularization L1/Lasso, feature importance của tree-based models — tích hợp ngay trong lúc huấn luyện.

📎 **Tìm hiểu thêm:**
- [Mailchimp — RFM Analysis: Definition, Purpose, and Examples](https://mailchimp.com/resources/rfm-analysis/)
- [pandas — Tài liệu chính thức DataFrame.groupby (dùng để tính RFM)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)

---


> 📚 [Mục lục](README.md) · ← [Phần 04: Các họ thuật toán Machine Learning](phan-04-thuat-toan-ml.md) · [Phần 06: EDA (Exploratory Data Analysis)](phan-06-eda.md) →

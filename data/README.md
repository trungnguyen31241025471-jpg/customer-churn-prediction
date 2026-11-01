# Thư mục dữ liệu

Dữ liệu thô **không được đưa lên GitHub** (đã cấu hình trong `.gitignore`).

## Cách lấy dữ liệu

1. Tải bộ **Online Retail II** từ UCI Machine Learning Repository (hoặc bản mirror trên Kaggle).
2. Lưu thành `data/online_retail_II.csv` (nếu tải về dạng Excel gồm hai sheet 2009–2010 và 2010–2011, gộp lại thành một bảng).
3. Các notebook trong `notebooks/` đọc file này bằng đường dẫn tương đối `../data/online_retail_II.csv`.

## Thông tin bộ dữ liệu

- Giao dịch của một doanh nghiệp bán lẻ trực tuyến tại Vương quốc Anh, 01/12/2009 – 09/12/2011.
- 1.067.371 dòng × 8 cột: `Invoice`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `Price`, `Customer ID`, `Country`.
- Bộ dữ liệu này có tên cột `Customer ID` (có dấu cách); một số script cũ dùng `CustomerID`.

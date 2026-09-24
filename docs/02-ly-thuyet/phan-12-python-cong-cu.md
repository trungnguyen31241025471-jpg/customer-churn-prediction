> 📚 [Mục lục](README.md) · ← [Phần 11: Toán học & Thống kê nền tảng](phan-11-toan-thong-ke.md) · [Phần 13: Deep Learning cơ bản](phan-13-deep-learning.md) →

## Phần 12: Python & Công cụ lập trình thực hành

> 🔑 **Hiểu nhanh trong 1 câu**: Đây là bộ "đồ nghề tay chân" biến toàn bộ lý thuyết ở các phần trên thành kết quả chạy được thật, trên dữ liệu thật.
> 🌍 **Ví dụ đời thường**: Giống như biết công thức nấu ăn (lý thuyết ML) là chưa đủ — còn cần biết cách cầm dao, dùng bếp, đọc công tắc lò nướng (Python, pandas, Git) thì mới thực sự nấu ra được món ăn.
> 📌 **Xem cài đặt môi trường từng bước**: `../04-cong-cu/huong-dan-cai-dat-cong-cu.md`

### 12.1 Cú pháp Python cơ bản cần nắm

Kiểu dữ liệu (int, float, str, bool, list, dict, tuple, set), cấu trúc điều khiển (`if/elif/else`, `for`/`while`), hàm (`def`... `return`), list comprehension (viết gọn để tạo danh sách mới trong một dòng), import thư viện (`import pandas as pd`).

### 12.2 Thao tác pandas cốt lõi (ví dụ cụ thể đã dùng trong notebook thực hành)

```python
# groupby + agg để tính RFM — ví dụ thực tế đã dùng
rfm = obs_df.groupby('Customer ID').agg(
    Recency=('InvoiceDate', lambda x: (cutoff_date - x.max()).days),
    Frequency=('Invoice', 'nunique'),
    Monetary=('Revenue', 'sum'),
)
```
Dòng code trên nhóm toàn bộ giao dịch theo từng khách hàng, rồi tính 3 chỉ số RFM cùng lúc — đây chính là "phép màu" của `groupby`: biến hàng triệu dòng giao dịch thành một dòng tổng hợp cho mỗi khách hàng.

### 12.3 Trực quan hóa dữ liệu

**matplotlib** — nền tảng, linh hoạt nhưng cú pháp dài dòng. **seaborn** — xây trên matplotlib, cú pháp gọn hơn, có sẵn heatmap tương quan, boxplot phát hiện outlier — rất phù hợp cho EDA (xem Phần 6).

### 12.4 Quản lý môi trường lập trình

**Virtual environment** (venv/conda) cô lập thư viện riêng cho từng dự án. **requirements.txt** ghi lại đúng phiên bản thư viện — ví dụ `pandas==2.1.4`, `scikit-learn==1.4.0` — giúp đồng đội hoặc reviewer cài lại đúng môi trường (liên hệ Phần 9.4 về reproducibility).

### 12.5 Git cơ bản

`git init`, `git add`, `git commit -m "..."`, `git push`, `git pull` — các lệnh nền tảng. **Branch** cho phép 3 thành viên làm việc song song mà không đè code lên nhau — ví dụ nhánh `feature/data-cleaning`, `feature/modeling`, `feature/writing`, sau đó **merge** lại vào nhánh `main` sau khi review chéo.

📎 **Tìm hiểu thêm:**
- [Learn Git Branching — công cụ tương tác trực quan, học Git ngay trên trình duyệt](https://learngitbranching.js.org/)
- [pandas — Tài liệu chính thức DataFrame.groupby](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)

---


> 📚 [Mục lục](README.md) · ← [Phần 11: Toán học & Thống kê nền tảng](phan-11-toan-thong-ke.md) · [Phần 13: Deep Learning cơ bản](phan-13-deep-learning.md) →

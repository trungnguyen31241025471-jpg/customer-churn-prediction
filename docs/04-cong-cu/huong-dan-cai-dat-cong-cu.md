# Hướng Dẫn Cài Đặt Toàn Bộ Công Cụ

> Làm theo đúng thứ tự các bước dưới đây. Sau khi hoàn tất, mở file `thuc-hanh-churn-prediction.ipynb` để bắt đầu thực hành song song với file lý thuyết.

---

## Bước 1 — Cài đặt Python

**Cách 1 (khuyến nghị cho người mới): Anaconda** — bộ cài đặt đã tích hợp sẵn Python, Jupyter Notebook, và phần lớn thư viện khoa học dữ liệu phổ biến.
- Tải tại: https://www.anaconda.com/download
- Cài đặt như phần mềm thông thường (Next → Next → Install).

**Cách 2: Python thuần**
- Tải Python 3.10 trở lên tại: https://www.python.org/downloads
- Khi cài trên Windows, nhớ tick chọn **"Add Python to PATH"**.

**Kiểm tra đã cài thành công:** mở Terminal (macOS/Linux) hoặc Command Prompt/PowerShell (Windows), gõ:
```
python --version
```
Nếu hiện ra số phiên bản (ví dụ `Python 3.10.12`) là thành công.

---

## Bước 2 — Tạo môi trường ảo (virtual environment)

Môi trường ảo giúp cô lập các thư viện của đề tài này, không ảnh hưởng đến các dự án Python khác trên máy.

**Nếu dùng Anaconda:**
```
conda create -n churn_env python=3.10
conda activate churn_env
```

**Nếu dùng Python thuần (venv):**
```
python -m venv churn_env

# Kích hoạt trên Windows:
churn_env\Scripts\activate

# Kích hoạt trên macOS/Linux:
source churn_env/bin/activate
```
Sau khi kích hoạt, bạn sẽ thấy `(churn_env)` xuất hiện ở đầu dòng lệnh — nghĩa là đang ở trong môi trường ảo.

---

## Bước 3 — Cài đặt các thư viện Python cần thiết

Với môi trường ảo đã kích hoạt, chạy lệnh sau (cài một lần duy nhất tất cả thư viện cần dùng):
```
pip install pandas numpy scikit-learn xgboost lightgbm shap lime matplotlib seaborn scipy statsmodels jupyter openpyxl
```

| Thư viện | Dùng để làm gì |
|---|---|
| pandas, numpy | Xử lý, biến đổi dữ liệu dạng bảng |
| scikit-learn | Các mô hình ML cổ điển, chia train/test, đánh giá mô hình |
| xgboost, lightgbm | Mô hình Gradient Boosting |
| shap, lime | Giải thích mô hình (XAI) |
| matplotlib, seaborn | Vẽ biểu đồ |
| scipy, statsmodels | Kiểm định thống kê |
| jupyter | Chạy Jupyter Notebook |
| openpyxl | Đọc file Excel (.xlsx) bằng pandas |

Chạy lệnh sau để lưu lại đúng phiên bản đã cài (phục vụ reproducibility, dùng khi viết bài báo và khi đồng đội cần cài lại giống hệt):
```
pip freeze > requirements.txt
```

---

## Bước 4 — Mở Jupyter Notebook để thực hành

**Cách 1: Chạy Jupyter trên máy**
```
jupyter notebook
```
Lệnh này sẽ tự mở trình duyệt, hiển thị danh sách file — bấm vào `thuc-hanh-churn-prediction.ipynb` để mở.

**Cách 2: Không cần cài gì — dùng Google Colab**
- Truy cập: https://colab.research.google.com
- Chọn "Upload" và tải lên file `thuc-hanh-churn-prediction.ipynb`
- Ở Colab, cần chạy thêm lệnh cài thư viện ở cell đầu tiên (vì Colab không có sẵn xgboost/shap):
```
!pip install shap lime xgboost lightgbm
```

---

## Bước 5 — Cài đặt Git và tạo tài khoản GitHub

1. Tải Git tại: https://git-scm.com/downloads
2. Sau khi cài, mở Terminal/Command Prompt, cấu hình tên và email (dùng để đánh dấu ai commit gì):
```
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"
```
3. Tạo tài khoản tại https://github.com nếu chưa có.
4. Tạo một repository mới trên GitHub (ví dụ tên `churn-prediction-project` — trùng tên với thư mục dự án ở `README.md`), sau đó clone về máy:
```
git clone https://github.com/<ten-tai-khoan>/churn-prediction-project.git
```
5. Copy toàn bộ cấu trúc thư mục (01-tong-quan, 02-ly-thuyet, ... 06-tai-lieu-tham-khao) vào thư mục vừa clone. File dữ liệu trong `05-thuc-hanh/data/` nên thêm vào `.gitignore`, không đẩy lên Git vì dung lượng lớn. Sau đó:
```
git add .
git commit -m "Khởi tạo project churn prediction"
git push
```

---

## Bước 6 — Cài đặt công cụ quản lý tài liệu tham khảo (Zotero)

1. Tải Zotero tại: https://www.zotero.org/download
2. Cài thêm tiện ích mở rộng trình duyệt **Zotero Connector** (link có ngay trên trang tải) — cho phép lưu bài báo trực tiếp từ Google Scholar, IEEE Xplore, ScienceDirect... chỉ bằng một cú nhấp chuột.
3. Trong Word hoặc Overleaf, cài plugin Zotero tương ứng để chèn trích dẫn tự động đúng định dạng.

---

## Bước 7 — Tạo tài khoản Overleaf (viết bài báo bằng LaTeX)

1. Truy cập https://www.overleaf.com và đăng ký tài khoản miễn phí (có thể đăng nhập bằng Google/GitHub).
2. Không cần cài gì trên máy — mọi thứ chạy trên trình duyệt.
3. Khi đã chọn được venue cụ thể, tìm template LaTeX chính thức của venue đó (thường có sẵn trên Overleaf Gallery hoặc trang web venue) và bắt đầu từ đó thay vì viết từ đầu.

---

## Bước 8 — Tải bộ dữ liệu Online Retail II

1. Truy cập: https://www.kaggle.com/datasets/jillwang87/online-retail-ii (cần tài khoản Kaggle, miễn phí)
2. Bấm "Download" để tải file `.csv` hoặc `.xlsx`.
3. Trong thư mục `05-thuc-hanh/` (nơi chứa notebook — xem cấu trúc tổng thể ở file `README.md` tại thư mục gốc), tạo một thư mục con tên `data`, và đặt file dữ liệu vừa tải vào đó:
```
churn-prediction-project/
├── README.md
├── 01-tong-quan/
├── 02-ly-thuyet/
├── 03-du-lieu/
├── 04-cong-cu/
├── 05-thuc-hanh/
│   ├── data/
│   │   └── online_retail_II.csv
│   ├── thuc-hanh-churn-prediction.ipynb
│   └── requirements.txt
└── 06-tai-lieu-tham-khao/
```

---

## Bước 9 — Kiểm tra toàn bộ cài đặt

Mở Jupyter Notebook, tạo một cell mới, chạy đoạn code sau — nếu không có lỗi nghĩa là mọi thứ đã sẵn sàng:
```python
import pandas, numpy, sklearn, xgboost, lightgbm, shap, lime, matplotlib, seaborn, scipy, statsmodels
print("Tất cả thư viện đã sẵn sàng!")
```

---

## Xử lý sự cố thường gặp

| Vấn đề | Cách xử lý |
|---|---|
| `pip install` báo lỗi quyền truy cập (permission denied) | Đảm bảo đã kích hoạt môi trường ảo (Bước 2) trước khi cài, không cài vào Python hệ thống |
| Chạy `jupyter notebook` báo "command not found" | Kiểm tra đã cài `jupyter` ở Bước 3 và đang ở đúng môi trường ảo đã kích hoạt |
| Đọc file `.xlsx` báo lỗi thiếu engine | Cài thêm `openpyxl` (đã có trong lệnh ở Bước 3); nếu vẫn lỗi, chạy `pip install openpyxl --upgrade` |
| SHAP `summary_plot` không hiện biểu đồ trong Jupyter | Thêm `%matplotlib inline` vào đầu notebook, hoặc chạy `plt.show()` ngay sau lệnh SHAP |
| File dữ liệu quá lớn không đẩy lên GitHub được | Thêm dòng `data/` vào file `.gitignore` để Git bỏ qua thư mục dữ liệu, chỉ đẩy code |

# Tổ Chức Nhóm Trên GitHub — Hướng Dẫn Từng Bước


## Bước 1 — Quyết định ai là chủ repository

Chọn 1 người (thường là trưởng nhóm hoặc người phụ trách viết bài) đứng tên tạo repository chính. Hai người còn lại sẽ được thêm làm **collaborator**, không cần mỗi người tạo một bản riêng.

Nếu nhóm muốn chuyên nghiệp hơn (và miễn phí): tạo một **GitHub Organization** (Settings → "Your organizations" → New organization) đứng tên chung, ví dụ `churn-prediction-team`, rồi tạo repo bên trong tổ chức đó thay vì tài khoản cá nhân. Cách này giúp không phụ thuộc vào một cá nhân nếu sau này đổi trưởng nhóm.

## Bước 2 — Tạo repository & đẩy cấu trúc project đã có lên

1. Trên GitHub, bấm **New repository** → đặt tên `churn-prediction-project` (khớp với thư mục đã có) → chọn **Private** (khuyến nghị, vì dữ liệu/bài viết chưa công bố) → **không** tick "Add a README" (vì đã có sẵn README.md).
2. Trên máy, tại thư mục cha chứa `churn-prediction-project/`:
```bash
cd churn-prediction-project
git init
git remote add origin https://github.com/<ten-to-chuc-hoac-tai-khoan>/churn-prediction-project.git
git add .
git commit -m "chore: khoi tao cau truc thu muc du an"
git branch -M main
git push -u origin main
```

## Bước 3 — Thêm 2 thành viên còn lại

Vào repo trên GitHub → **Settings → Collaborators and teams** (nếu dùng Organization thì vào **Settings → Manage access**) → **Add people** → nhập username hoặc email của 2 thành viên còn lại → chọn quyền **Write** (đủ để họ push branch và tạo Pull Request, không cần Admin). Họ sẽ nhận email mời và cần bấm chấp nhận.

## Bước 4 — Thiết lập `.gitignore`

Tạo file `.gitignore` ở thư mục gốc để tránh đẩy nhầm file không nên có trên Git:
```
# Dữ liệu (dung lượng lớn, không nên đẩy lên Git)
05-thuc-hanh/data/

# Môi trường ảo Python
churn_env/
venv/
.venv/

# Cache Python & Jupyter
__pycache__/
*.pyc
.ipynb_checkpoints/

# File hệ điều hành
.DS_Store
Thumbs.db
```
Commit ngay file này trước khi ai đó lỡ đẩy file dữ liệu nặng lên:
```bash
git add .gitignore
git commit -m "chore: them gitignore"
git push
```

## Bước 5 — Bảo vệ nhánh `main` (branch protection)

Vào **Settings → Branches → Add branch protection rule** → nhập `main` vào ô pattern → tick các mục:
- **Require a pull request before merging** (không ai được push thẳng vào `main`)
- **Require approvals** → đặt số lượng approval tối thiểu là **1** (nghĩa là phải có ít nhất 1 người khác review trước khi merge)

Việc này bắt buộc mọi thay đổi phải qua Pull Request + review chéo, tránh trường hợp một người vô tình ghi đè công việc của người khác.

## Bước 6 — Quy ước đặt tên nhánh (branch)

Mỗi người luôn làm việc trên nhánh riêng, không code trực tiếp trên `main`. Đặt tên theo mẫu `<mang>/<mo-ta-ngan>`:

| Người | Mảng | Ví dụ tên nhánh |
|---|---|---|
| A | data | `data/lam-sach-online-retail`, `data/rfm-features` |
| B | model | `model/baseline-logistic`, `model/shap-explainability` |
| C | writing | `writing/related-work`, `writing/abstract` |

## Bước 7 — Quy trình làm việc hàng ngày (mỗi người lặp lại quy trình này)

```bash
# 1. Luôn cập nhật main mới nhất trước khi bắt đầu
git checkout main
git pull

# 2. Tạo nhánh mới cho việc đang làm
git checkout -b data/lam-sach-online-retail

# 3. Code, chỉnh sửa file như bình thường...

# 4. Commit theo từng phần việc nhỏ, không dồn hết vào 1 commit cuối ngày
git add ten-file-da-sua.md
git commit -m "feat: them buoc loai bo hoa don huy"

# 5. Đẩy nhánh lên GitHub
git push -u origin data/lam-sach-online-retail
```
Sau đó vào GitHub, bấm **Compare & pull request** → viết mô tả ngắn đã làm gì → gắn tag 1 trong 2 người còn lại vào phần **Reviewers** → chờ họ review và approve → bấm **Merge pull request** → **xóa nhánh đó sau khi merge** (GitHub có nút xóa ngay sau khi merge).

## Bước 8 — Chuẩn hóa commit message

Dùng tiền tố ngắn để dễ tra cứu lịch sử sau này (không bắt buộc quá nghiêm ngặt, nhưng nên thống nhất trong nhóm):

| Tiền tố | Dùng khi |
|---|---|
| `feat:` | Thêm tính năng/xử lý mới (vd: thêm bước gán nhãn churn) |
| `fix:` | Sửa lỗi |
| `docs:` | Chỉ sửa tài liệu/markdown, không đổi code |
| `refactor:` | Viết lại code cho gọn hơn, không đổi kết quả |
| `chore:` | Việc lặt vặt (cập nhật .gitignore, đổi tên file...) |

## Bước 9 — Dùng GitHub Issues để giao việc theo lộ trình

Vào tab **Issues → New issue**, tạo 1 issue cho mỗi việc trong bảng lộ trình ở `01-tong-quan/tong-quan-de-tai.md`, ví dụ:
- Tiêu đề: `[Data] Làm sạch Online Retail II + loại hóa đơn huỷ`
- Gán **Assignee** = Người A
- Gắn **Label** theo giai đoạn: `giai-doan-2`, `giai-doan-3`...

Khi tạo Pull Request ở Bước 7, ghi `Closes #<số-issue>` trong mô tả PR — GitHub sẽ tự động đóng issue đó khi PR được merge.

## Bước 10 — Dùng GitHub Projects (bảng Kanban) để theo dõi tiến độ

Vào tab **Projects → New project → Board**. Tạo 3 cột: **To do**, **In progress**, **Done**. Kéo các Issues đã tạo ở Bước 9 vào cột tương ứng. Mỗi buổi họp sync hàng tuần (đã nói ở `01-tong-quan/`), cả nhóm cùng nhìn vào bảng này để biết ai đang vướng ở đâu — thay thế việc phải hỏi nhau qua tin nhắn.

## Bước 11 — Lưu ý riêng khi đồng bộ Jupyter Notebook (`.ipynb`) qua Git

File `.ipynb` chứa cả code lẫn output (hình ảnh, số liệu đã chạy) dưới dạng JSON — mỗi lần chạy lại, output thay đổi dù code không đổi, gây ra conflict Git rất khó đọc. Hai cách xử lý:

- **Cách đơn giản**: trước khi commit, vào Jupyter → **Kernel → Restart & Clear Output** để xóa hết output rồi mới lưu và commit — người khác kéo về sẽ tự chạy lại để xem output.
- **Cách tự động hoá** (khuyến nghị nếu nhóm quen thuộc hơn với công cụ): cài `nbstripout` (`pip install nbstripout` rồi chạy `nbstripout --install` trong thư mục repo) — công cụ này tự động xóa output mỗi lần commit mà không cần nhớ làm thủ công.

## Bước 12 — Checklist trước khi merge Pull Request vào `main`

- [ ] Code chạy được từ đầu đến cuối, không lỗi.
- [ ] Đã xóa output notebook (hoặc đã cài `nbstripout`) trước khi commit.
- [ ] Không có file dữ liệu lớn bị lỡ add (`git status` kiểm tra lại trước khi commit).
- [ ] Đã có ít nhất 1 người khác review và approve.
- [ ] Mô tả Pull Request có nhắc rõ đã làm gì và liên kết đúng Issue liên quan.

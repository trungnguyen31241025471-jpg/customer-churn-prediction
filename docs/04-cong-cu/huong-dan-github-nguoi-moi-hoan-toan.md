# Hướng Dẫn GitHub Cầm Tay Chỉ Việc (Dành Cho Người Dùng Lần Đầu)

> Bạn đã có sẵn repo `customer-churn-prediction` (như trong ảnh chụp màn hình) — tài liệu này giải thích từ con số 0: GitHub là gì, từng nút bấm trong màn hình bạn đang thấy có nghĩa gì, và cách thao tác từng việc cụ thể. Đọc tuần tự, đừng bỏ qua Phần 0.

---

## Phần 0 — Khái Niệm Cơ Bản Cần Biết Trước

### Git là gì? GitHub là gì? Khác nhau thế nào?

- **Git**: một phần mềm chạy trên máy tính của bạn, dùng để "ghi nhớ lịch sử thay đổi" của các file (giống như tính năng "Version History" trong Google Docs, nhưng mạnh hơn nhiều và dùng cho code).
- **GitHub**: một trang WEB (github.com) lưu trữ các "kho chứa Git" đó trên mạng, để nhiều người có thể cùng xem, tải về, và đóng góp vào cùng một dự án.
- Ví dụ dễ hình dung: Git giống như "Track Changes" trong Word trên máy bạn; GitHub giống như Google Drive — nơi lưu trữ và chia sẻ file đó cho người khác cùng xem/sửa.

### Repository (Repo) là gì?

Một "kho chứa" — giống như MỘT thư mục dự án duy nhất chứa toàn bộ file liên quan (code, tài liệu, ảnh...). Repo `customer-churn-prediction` trong ảnh của bạn chính là kho chứa cho toàn bộ đề tài này.

### Commit là gì?

Mỗi lần bạn lưu một thay đổi (thêm file, sửa nội dung...) và xác nhận lưu lại, đó gọi là một "commit" — giống như một "điểm lưu" (save point) trong lịch sử dự án, kèm một dòng ghi chú ngắn mô tả bạn vừa làm gì. Trong ảnh, bạn đã có "5 Commits" nghĩa là đã lưu 5 lần thay đổi.

### Branch (nhánh) là gì?

Một "phiên bản song song" của toàn bộ dự án, để thử nghiệm mà không ảnh hưởng đến bản chính. Trong ảnh, bạn đang có **1 Branch** tên `main` — đây là nhánh CHÍNH, mặc định của mọi repo. Ở giai đoạn đầu làm việc một mình, bạn có thể làm việc thẳng trên `main` — khái niệm tạo nhánh riêng sẽ cần khi làm việc nhóm (đã có hướng dẫn riêng ở `to-chuc-nhom-tren-github.md`).

### Public là gì?

Nhãn "Public" trong ảnh nghĩa là bất kỳ ai trên mạng cũng xem được repo này (nhưng không sửa được nếu bạn không cấp quyền). Ngược lại là "Private" — chỉ người được mời mới xem được.

---

## Phần 1 — Giải Nghĩa Màn Hình Bạn Đang Thấy

Đối chiếu với ảnh chụp bạn đã gửi, mỗi phần có ý nghĩa như sau:

| Vị trí trong ảnh | Ý nghĩa |
|---|---|
| `customer-churn-prediction` (tiêu đề lớn) | Tên repo của bạn |
| Nhãn `Public` | Ai cũng xem được repo này |
| `main ▾` (góc trái, có biểu tượng nhánh) | Bạn đang xem nhánh `main` — nhánh chính |
| `1 Branch` | Hiện có 1 nhánh duy nhất (main) |
| `0 Tags` | "Tag" dùng để đánh dấu các mốc phiên bản quan trọng (ví dụ v1.0) — bạn chưa dùng đến, không sao cả |
| Ô `Go to file` | Gõ tên file để tìm nhanh trong repo, thay vì click từng thư mục |
| Nút `Add file ▾` | Dùng để THÊM file mới (tạo mới hoặc tải lên từ máy) — sẽ dùng nhiều ở Phần 3-4 |
| Nút xanh `Code` | Bấm vào để lấy đường link clone repo về máy (chỉ cần khi dùng Git dòng lệnh — nếu chỉ thao tác qua web thì không cần bấm nút này) |
| Dòng `trungnguyen31241025471-jpg ... Update README.md ... ca34596 · 17 hours ago · 5 Commits` | Thông tin LẦN COMMIT GẦN NHẤT: ai commit, nội dung gì, mã số commit, thời gian, và tổng số commit |
| Danh sách `docs`, `notebooks`, `src`, `.gitignore`, `README.md` | Nội dung bên trong repo — 3 thư mục và 2 file bạn đã tạo |
| Cột phải mỗi dòng (`feat: bo sung...`, `17 hours ago`) | Commit message (ghi chú) và thời gian của lần thay đổi GẦN NHẤT liên quan đến đúng file/thư mục đó |
| Khung `README` phía dưới cùng | Nội dung file `README.md` được GitHub tự động hiển thị đẹp ngay trên trang — đây là "trang giới thiệu" đầu tiên ai cũng thấy khi vào repo |

---

## Phần 2 — Cách Tạo Một File Mới Trực Tiếp Trên Web

Dùng khi bạn muốn viết nội dung mới (ví dụ thêm file `requirements.txt`) mà không cần soạn sẵn trên máy.

1. Vào đúng thư mục muốn đặt file (ví dụ bấm vào thư mục gốc của repo nếu muốn tạo ở ngoài cùng).
2. Bấm nút **Add file** (đã thấy trong ảnh) → chọn **Create new file**.
3. Ô đầu tiên hiện ra để bạn gõ TÊN file — gõ ví dụ `requirements.txt`. (Mẹo: nếu muốn tạo file NẰM TRONG một thư mục, gõ luôn đường dẫn, ví dụ `src/data_cleaning.py` — GitHub sẽ tự tạo thư mục `src` nếu chưa có).
4. Bên dưới là khung lớn để gõ/dán NỘI DUNG file.
5. Cuộn xuống cuối trang, thấy khung **"Commit new file"** — gõ một dòng mô tả ngắn (ví dụ: `feat: them requirements.txt`) vào ô **Commit message**.
6. Đảm bảo đang chọn **"Commit directly to the main branch"** (tuỳ chọn mặc định, phù hợp khi làm việc một mình).
7. Bấm nút xanh **Commit changes**.

✅ **Kết quả mong đợi**: quay lại trang chính của repo, sẽ thấy file mới xuất hiện trong danh sách, kèm số Commit tăng thêm 1.

---

## Phần 3 — Cách Tải Nhiều File/Thư Mục Lên Cùng Lúc

Dùng khi bạn đã có sẵn file trên máy tính (ví dụ toàn bộ nội dung trong `churn-prediction-project.zip` đã tải trước đó) và muốn đưa lên GitHub.

1. Giải nén file `churn-prediction-project.zip` trên máy tính trước (chuột phải → Extract All trên Windows).
2. Trên GitHub, vào đúng thư mục đích (ví dụ bấm vào `docs` để vào bên trong).
3. Bấm **Add file** → chọn **Upload files**.
4. Một khung lớn hiện ra với dòng chữ "Drag files here to add them to your repository" — **kéo-thả** các file/thư mục từ cửa sổ Explorer (Windows) hoặc Finder (Mac) vào đúng khung đó. Bạn có thể kéo nhiều file cùng lúc, hoặc cả một thư mục con.
5. Đợi thanh tiến trình upload chạy xong (tuỳ số lượng/dung lượng file, có thể mất vài giây đến vài phút).
6. Cuộn xuống, gõ Commit message (ví dụ: `docs: bo sung tai lieu ly thuyet va nghien cuu`).
7. Bấm **Commit changes**.

⚠️ **Lỗi thường gặp**: nếu upload báo lỗi hoặc bị treo lâu — khả năng cao là có FILE QUÁ LỚN (GitHub giới hạn mỗi file dưới 100MB, khuyến nghị dưới 50MB). File dữ liệu CSV (hàng chục MB) **không nên** tải lên GitHub — xem lại phần `.gitignore` trong `nang-cap-github-chuyen-nghiep.md` để biết cách loại trừ.

---

## Phần 4 — Cách Sửa Một File Đã Có (Ví Dụ Sửa README.md)

1. Từ trang chính repo, bấm vào tên file muốn sửa (ví dụ `README.md`).
2. Ở góc trên bên phải của nội dung file, bấm biểu tượng **cây bút chì** (Edit this file).
3. Nội dung file hiện ra dưới dạng có thể gõ chữ trực tiếp — xoá/sửa/thêm theo ý muốn.
4. Cuộn xuống cuối trang, gõ Commit message, bấm **Commit changes** (giống Phần 2, bước 5-7).

---

## Phần 5 — Cách Xem Lại Lịch Sử Thay Đổi

1. Từ trang chính repo, bấm vào dòng chữ có biểu tượng đồng hồ, ví dụ **"5 Commits"** (đã thấy trong ảnh, góc trên bên phải danh sách file).
2. Một trang mới hiện ra, liệt kê TỪNG lần commit theo thứ tự thời gian (mới nhất trên cùng), kèm ai đã commit và commit message của lần đó.
3. Bấm vào một commit cụ thể để xem CHÍNH XÁC dòng nào đã được thêm (nền xanh lá) hoặc xoá (nền đỏ) trong lần đó.

**Nghiệp vụ**: đây chính là công cụ giúp bạn (hoặc giảng viên) kiểm tra lại được ai đã đóng góp gì, vào lúc nào — rất hữu ích khi làm việc nhóm hoặc khi cần giải trình quá trình thực hiện đề tài.

---

## Phần 6 — Cách Thêm Thành Viên Vào Dự Án

1. Trên trang repo, nhìn thanh menu ngang phía trên (cùng hàng với "Code", "Issues", "Pull requests"...) — bấm vào **Settings** (thường là mục cuối cùng, có biểu tượng bánh răng).
2. Cột bên trái trang Settings, tìm và bấm **Collaborators** (nằm trong nhóm "Access").
3. GitHub có thể yêu cầu nhập lại mật khẩu tài khoản để xác nhận danh tính — nhập vào và xác nhận.
4. Bấm nút xanh **Add people**.
5. Gõ username hoặc email GitHub của thành viên muốn thêm vào ô tìm kiếm — danh sách gợi ý sẽ hiện ra, bấm chọn đúng người.
6. Ở bước chọn quyền, chọn **Write** — cho phép họ đẩy code lên, tạo Pull Request, nhưng KHÔNG cho phép họ đổi cài đặt repo hay xoá repo (quyền đó chỉ dành cho Admin/chủ repo).
7. Bấm **Add [tên người đó] to this repository**.

✅ **Kết quả mong đợi**: thành viên đó sẽ nhận được một email mời từ GitHub — họ cần bấm **View invitation** trong email rồi bấm **Accept invitation** thì mới chính thức có quyền truy cập và thao tác trên repo.

---

## Phần 7 — Vài Khái Niệm Nên Biết Thêm (Chưa Cần Dùng Ngay)

- **Pull Request (PR)**: một "đề xuất" gộp thay đổi từ một nhánh vào nhánh `main`, kèm cơ chế cho người khác REVIEW (xem xét) trước khi đồng ý gộp. Cần dùng khi làm việc nhóm nhiều người cùng sửa code — xem hướng dẫn chi tiết ở `to-chuc-nhom-tren-github.md` khi nhóm bắt đầu phối hợp.
- **Issues**: một "danh sách việc cần làm" ngay trong GitHub, có thể giao việc cho từng người, đánh dấu hoàn thành — hữu ích khi nhóm 3 người cần theo dõi tiến độ chung.
- **Clone về máy bằng Git**: nếu sau này bạn muốn code trực tiếp trên máy tính (dùng Anaconda/Jupyter như các hướng dẫn khác) thay vì chỉnh sửa trên web, cần "clone" (tải cả repo về máy) bằng lệnh `git clone <link>` — xem chi tiết ở `to-chuc-nhom-tren-github.md` Bước 2.

---

## Checklist Tổng Kết

- [ ] Đã hiểu được ý nghĩa từng phần trong màn hình repo (Phần 1)
- [ ] Đã thử tạo được 1 file mới trực tiếp trên web (Phần 2)
- [ ] Đã thử upload thành công ít nhất 1 thư mục con (Phần 3)
- [ ] Đã thử sửa nội dung README.md (Phần 4)
- [ ] Đã biết cách xem lại lịch sử Commits (Phần 5)
- [ ] Đã thêm thành công ít nhất 1 thành viên (Phần 6)

Hoàn thành xong checklist này, bạn đã có đủ kỹ năng GitHub cơ bản để tiếp tục làm theo `nang-cap-github-chuyen-nghiep.md` — đưa toàn bộ nội dung dự án lên đúng cấu trúc chuyên nghiệp.

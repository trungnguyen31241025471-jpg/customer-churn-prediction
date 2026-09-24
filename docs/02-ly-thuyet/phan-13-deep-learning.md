> 📚 [Mục lục](README.md) · ← [Phần 12: Python & Công cụ lập trình](phan-12-python-cong-cu.md) · [Phần 16: Bảng thuật ngữ (Glossary)](phan-16-glossary.md) →

## Phần 13: Deep Learning cơ bản (mở rộng phần Neural Network)

> 🔑 **Hiểu nhanh trong 1 câu**: Mạng nơ-ron là nhiều lớp "công thức toán đơn giản" xếp chồng lên nhau, mỗi lớp học một mức độ trừu tượng cao hơn lớp trước.
> 🌍 **Ví dụ đời thường**: Giống như dây chuyền sản xuất — lớp đầu tiên chỉ nhận diện các nét đơn giản (giống công nhân đầu chỉ lắp ốc vít), lớp giữa ghép các nét đó thành hình dạng phức tạp hơn, lớp cuối mới đưa ra sản phẩm hoàn chỉnh (dự đoán cuối cùng).

### 13.1 Từ nơ-ron đến mạng (ví dụ số đơn giản)

M��t nơ-ron nhân tạo tính: `output = activation(w1×x1 + w2×x2 + ... + bias)`. Ví dụ với 2 đặc trưng đầu vào x1=Recency(chuẩn hóa)=0.8, x2=Frequency(chuẩn hóa)=0.2, trọng số w1=0.6, w2=-0.3, bias=0.1: `z = 0.6×0.8 + (-0.3)×0.2 + 0.1 = 0.48 - 0.06 + 0.1 = 0.52` → qua hàm activation Sigmoid: `output ≈ 0.627`.

### 13.2 Activation Function, Loss Function

**Activation Function**: Sigmoid (đưa về khoảng 0-1, phù hợp bài toán churn nhị phân), ReLU (phổ biến ở lớp ẩn), Tanh. **Loss Function** cho bài toán churn: **Binary Cross-Entropy** — phạt nặng khi mô hình tự tin sai (ví dụ dự đoán 0.95 xác suất không churn nhưng khách lại churn thật, loss sẽ rất lớn).

### 13.3 Backpropagation, Epoch, Batch size

**Backpropagation**: tính gradient của loss theo từng trọng số bằng quy tắc chuỗi (chain rule), rồi cập nhật bằng Gradient Descent (xem Phần 11.2 — cùng một nguyên lý, chỉ áp dụng cho hàng nghìn trọng số cùng lúc thay vì 1 tham số). **Epoch**: một lượt duyệt hết toàn bộ dữ liệu huấn luyện. **Batch size**: ví dụ batch_size=32 nghĩa là cập nhật trọng số sau mỗi 32 khách hàng thay vì đợi hết toàn bộ dữ liệu.

### 13.4 Regularization và RNN/LSTM/GRU

**Dropout**: ngẫu nhiên "tắt" một số nơ-ron mỗi lần huấn luyện (ví dụ tắt 20% nơ-ron ngẫu nhiên) để mạng không phụ thuộc quá mức vào vài nơ-ron cụ thể — chống overfitting. **LSTM/GRU** có cơ chế "cổng" quyết định giữ/quên thông tin qua các bước thời gian, giải quyết vấn đề **vanishing gradient** của RNN thông thường — phù hợp khi mô hình hóa chuỗi giao dịch theo thời gian của một khách hàng thay vì chỉ dùng RFM tĩnh.

📎 **Tìm hiểu thêm:**
- [3Blue1Brown — But what is a neural network? (Deep Learning chapter 1)](https://www.youtube.com/watch?v=aircAruvnKk)
- [3Blue1Brown — Essence of Linear Algebra (nền tảng toán cho neural network)](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

---


> 📚 [Mục lục](README.md) · ← [Phần 12: Python & Công cụ lập trình](phan-12-python-cong-cu.md) · [Phần 16: Bảng thuật ngữ (Glossary)](phan-16-glossary.md) →

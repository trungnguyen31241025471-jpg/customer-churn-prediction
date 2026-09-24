> 📚 [Mục lục](README.md) · ← [Phần 06: EDA (Exploratory Data Analysis)](phan-06-eda.md) · [Phần 08: Model Evaluation](phan-08-model-evaluation.md) →

## Phần 7: Data Preprocessing

> 🔑 **Hiểu nhanh trong 1 câu**: Dọn dẹp "rác" trong dữ liệu (thiếu, sai, trùng, lệch quá mức) trước khi đưa vào mô hình — "rác vào thì rác ra" (garbage in, garbage out).
> 🌍 **Ví dụ đời thường**: Giống như rửa và nhặt sạn gạo trước khi nấu cơm — dù nồi cơm điện (mô hình ML) có xịn đến đâu, gạo còn lẫn sạn (dữ liệu bẩn) thì cơm vẫn không ngon được.
> 📌 **Xem thực hành đầy đủ (pipeline làm sạch + capping outlier)**: `../05-thuc-hanh/eda-va-tien-xu-ly-du-lieu.ipynb` (Phần B) và lý do chi tiết ở `../05-thuc-hanh/giai-thich-ky-thuat-eda-tien-xu-ly-feature-engineering.md`

### 7.1 Xử lý dữ liệu thiếu (Missing Data)

Phân biệt: **MCAR** (Missing Completely At Random — thiếu hoàn toàn ngẫu nhiên), **MAR** (Missing At Random — thiếu có liên quan đến biến khác đã biết), **MNAR** (Missing Not At Random — thiếu liên quan đến chính giá trị bị thiếu). Với CustomerID thiếu trong Online Retail II (không rõ nguyên nhân, không suy luận được), phổ biến là loại bỏ khỏi phân tích theo khách hàng.

### 7.2 Xử lý giá trị ngoại lai (Outlier)

Ví dụ: một dòng có Quantity = 80.995 (đơn bán buôn cực lớn có thật) khác với Quantity = -9999 (rõ ràng là lỗi nhập liệu hoặc mã điều chỉnh kế toán). Cần phân biệt outlier "thật" (giữ lại) và outlier "lỗi" (loại bỏ).

### 7.3 Xử lý mất cân bằng lớp (Class Imbalance)

Ví dụ cụ thể: nếu trong 5000 khách hàng chỉ có 800 người churn (16%) và 4200 không churn (84%) — mô hình có thể "lười biếng" dự đoán tất cả là "không churn" và vẫn đạt Accuracy 84%, nhưng vô dụng vì không bắt được ai churn cả. Giải pháp:
- **SMOTE**: tạo thêm mẫu tổng hợp cho lớp thiểu số bằng nội suy giữa các điểm gần nhau.
- **Class weighting**: gán trọng số cao hơn cho lớp churn trong hàm mất mát (ví dụ `class_weight='balanced'` trong scikit-learn tự động tính trọng số nghịch đảo theo tỷ lệ lớp).
- **Undersampling**: giảm bớt mẫu lớp đa số (ví dụ chỉ lấy ngẫu nhiên 800 trong 4200 khách không churn để cân bằng với 800 khách churn).

📎 **Tìm hiểu thêm:**
- [scikit-learn — User Guide đầy đủ (bao gồm preprocessing, imbalanced data)](https://scikit-learn.org/stable/user_guide.html)

---


> 📚 [Mục lục](README.md) · ← [Phần 06: EDA (Exploratory Data Analysis)](phan-06-eda.md) · [Phần 08: Model Evaluation](phan-08-model-evaluation.md) →

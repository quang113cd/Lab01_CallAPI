# Hệ Thống API VinAI - Dịch Thuật Anh-Việt

## 1. Thông tin sinh viên
* **Họ và tên:** Trần Công Quang
* **Mã sinh viên:** 24120221
* **Trường:** University of Science, VNU-HCM
* **Môn học:** Tư duy tính toán (Computational Thinking) - Lab 1

## 2. Mô hình sử dụng
* **Tên mô hình:** `vinai-translate-en2vi`
* **Liên kết Hugging Face:** [https://huggingface.co/vinai/vinai-translate-en2vi](https://huggingface.co/vinai/vinai-translate-en2vi)

## 3. Mô tả chức năng hệ thống
Chức năng chính là tiếp nhận văn bản Tiếng Anh, xử lý thông qua mô hình học sâu (Deep Learning) và trả về kết quả dịch thuật Tiếng Việt dưới định dạng JSON để hỗ trợ giao tiếp cho khách du lịch nước ngoài.

## 4. Hướng dẫn cài đặt thư viện
Để cấu hình môi trường chạy code và kiểm thử, vui lòng cài đặt các thư viện phụ thuộc thông qua file `requirements.txt`:
```bash
pip install -r requirements.txt
```

## 5. Hướng dẫn chạy chương trình
Hệ thống được thiết kế để chạy trên môi trường Google Colab nhằm tận dụng cấu hình máy chủ mạnh:
1. Upload file `VinAI_API.ipynb` lên Google Colab và đảm bảo đã bật Runtime là **T4 GPU**.
2. Thực thi (Run) toàn bộ các ô code từ trên xuống dưới để cài đặt, nạp mô hình và khởi chạy FastAPI server tại cổng `8000`.
3. Mở cửa sổ **Terminal** trên Colab và chạy lệnh sau để lấy đường dẫn Public thông qua Pinggy:
   ```bash
   ssh -o StrictHostKeyChecking=no -p 443 -R0:localhost:8000 qr@a.pinggy.io
   ```
4. Hệ thống sẽ cấp một đường link (ví dụ: `https://<random-id>.run.pinggy-free.link`). Link này có hiệu lực trong 60 phút và được dùng để gọi API từ bên ngoài.

## 6. Hướng dẫn gọi API và Ví dụ Request/Response
Sử dụng đường link Pinggy ở bước trên để gọi API. (Đảm bảo thay thế biến `<link-pinggy-duoc-cap>` bằng URL thực tế).

* **Endpoint:** `POST /predict`
* **Headers:** `Content-Type: application/json`

**Ví dụ Request (Sử dụng Python):**
```python
import requests

API_URL = "https://<link-pinggy-duoc-cap>.run.pinggy-free.link/predict"
payload = {
    "message": "I want to find a traditional museum in Da Nang"
}

response = requests.post(API_URL, json=payload)
print(response.json())
```

**Ví dụ Response (Kết quả nhận được):**
```json
{
    "original_text": "I want to find a traditional museum in Da Nang",
    "translated_text": "Tôi muốn tìm một bảo tàng truyền thống ở Đà Nẵng."
}
```

## 7. Liên kết Video Demo
* **Video Demo toàn bộ quá trình chạy hệ thống:** [https://youtu.be/scP3ZYsDl8k](https://youtu.be/scP3ZYsDl8k)

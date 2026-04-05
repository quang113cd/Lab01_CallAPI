import requests

# Đường dẫn đến server FastAPI(đang chạy local)
BASE_URL = "http://smxir-136-109-107-52.run.pinggy-free.link"

def test_health_check():
    print("[1] Đang kiểm tra trạng thái API (/health)...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"    -> Status Code: {response.status_code}")
        print(f"    -> Response: {response.json()}\n")
    except Exception as e:
        print(f"    -> [LỖI] Không thể kết nối. Hãy chắc chắn server đang chạy ở cổng 8000. Chi tiết: {e}\n")

def test_predict():
    print("[2] Đang kiểm tra chức năng Dịch thuật (/predict)...")
    url = f"{BASE_URL}/predict"
    
    # Hai câu test liên quan đến bối cảnh Smart Tourism
    test_cases = [
        # "The seafood here is very fresh and delicious.",
        # "I want to find atraditional museum in Da Nang.",
        # "Banh mi doesn't appeal to me",
        "Cao lau is really delicious",
        "I tried Cao Lau 2 hours ago"
    ]

    for i, text in enumerate(test_cases, 1):
        print(f"   --- Test case {i} ---")
        payload = {"message": text}
        try:
            response = requests.post(url, json=payload)
            print(f"    -> Câu tiếng Anh: '{text}'")
            print(f"    -> Status Code: {response.status_code}")
            print(f"    -> JSON trả về: {response.json()}\n")
        except Exception as e:
            print(f"    -> [LỖI] Xảy ra lỗi khi gọi API: {e}\n")

if __name__ == "__main__":
    print("=====================================================")
    print("     KIỂM THỬ API VinModel   ")
    print("     Sinh viên: Công Quang")
    print("=====================================================\n")
    
    test_health_check()
    test_predict()
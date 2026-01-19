# Backend Order Notification System

## Mục tiêu
Xây dựng backend gửi thông báo đơn hàng đến Kitchen Dashboard bằng:
- WebSocket
- Redis Pub/Sub


## Chức năng
- Nhận order qua REST API
- Gửi order realtime đến kitchen qua WebSocket
- Publish order qua Redis channel

##  Cấu trúc thư mục
Backend/
│
├─ src/
│  ├─ app.py
│  ├─ api/
│  │  └─ order_controller.py
│  ├─ services/
│  │  └─ order_service.py
│  ├─ realtime/
│  │  ├─ redis_pubsub.py
│  │  └─ socket_manager.py
│  └─ __init__.py
│
├─ test_client.py
├─ requirements.txt
├─ README.md
├─ .gitignore
└─ venv/




## 3. Tạo môi trường ảo

Chạy trong thư mục Backend:
python -m venv venv
venv\Scripts\activate

Kiểm tra Python:
python --version

## 4. Cài đặt thư viện
pip install -r requirements.txt

## 5. Chạy Redis bằng Docker

Kiểm tra Docker:
docker ps

Chạy Redis:
docker run -d -p 6379:6379 --name redis redis
Nếu Redis đã tồn tại:
docker start redis
Redis chạy tại localhost:6379

## 6. Chạy Backend Flask

Trong thư mục Backend (đã activate venv):
python -m src.app

Kết quả đúng:
Redis connected
Running on http://127.0.0.1:5000

## 7. Chạy WebSocket client (Kitchen)
Mở terminal mới:
python test_client.py

Kết quả đúng:
Connected to backend

## 8. Test API tạo Order
Mở terminal mới:
Invoke-RestMethod `
  -Uri http://127.0.0.1:5000/orders `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"id":1,"item":"Pizza","quantity":2}'


## 9. Kết quả mong đợi
Backend terminal hiển thị:
Received order
Sent order to kitchen

Terminal test_client hiển thị:
New order received: {'id': 1, 'item': 'Pizza', 'quantity': 2}




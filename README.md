# Backend Order Notification System

## Mục tiêu
Xây dựng backend gửi thông báo đơn hàng đến Kitchen Dashboard bằng:
- WebSocket
- Redis Pub/Sub

## Công nghệ sử dụng
- Python
- Flask
- Flask-SocketIO
- Redis

## Chức năng
- Nhận order qua REST API
- Gửi order realtime đến kitchen qua WebSocket
- Publish order qua Redis channel

## Cấu trúc thư mục
Backend/
├── src/
│   ├── api/
│   │   └── order_controller.py
│   ├── services/
│   │   └── order_service.py
│   ├── realtime/
│   │   ├── socket_manager.py
│   │   └── redis_pubsub.py
│   ├── app.py
│   └── test_client.py
├── requirements.txt
└── README.md

## Cách chạy

### 1. Tạo môi trường ảo
python -m venv venv  
venv\Scripts\activate

### 2. Cài thư viện
pip install -r requirements.txt

### 3. Chạy Redis
Redis phải chạy tại localhost:6379

### 4. Chạy backend
python -m src.app

### 5. Chạy Redis subscriber
python src/realtime/redis_pubsub.py

### 6. Test gửi order
Gửi POST request tới:
http://127.0.0.1:5000/orders

Body ví dụ:
{
  "id": 1,
  "item": "Pizza",
  "quantity": 2
}

## Kết quả
- Kitchen Dashboard nhận order qua WebSocket
- Redis subscriber nhận order qua Pub/Sub

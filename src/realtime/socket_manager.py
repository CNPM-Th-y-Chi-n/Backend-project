from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="*")


def send_order_to_kitchen(order_data: dict):

    socketio.emit("new_order", order_data)
    print("📡 Sent order to kitchen via WebSocket:", order_data)

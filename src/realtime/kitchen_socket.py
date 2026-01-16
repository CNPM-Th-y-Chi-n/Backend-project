from realtime.socket_manager import socketio

def send_order_to_kitchen(order_data):
    print(" Sending order to kitchen:", order_data)
    socketio.emit("new_order", order_data)



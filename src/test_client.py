import socketio

sio = socketio.Client()


@sio.event
def connect():
    print(" Kitchen connected to backend")


@sio.on("new_order")
def on_new_order(data):
    print(" New order received in kitchen:")
    print(data)


@sio.event
def disconnect():
    print(" Kitchen disconnected")


sio.connect("http://127.0.0.1:5000")
sio.wait()

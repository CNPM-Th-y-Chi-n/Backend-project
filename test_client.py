import socketio

sio = socketio.Client()

@sio.event
def connect():
    print(" Connected to backend")

@sio.event
def disconnect():
    print(" Disconnected from backend")

@sio.on("new_order")
def on_new_order(data):
    print(" New order received:", data)

if __name__ == "__main__":
    sio.connect("http://127.0.0.1:5000")
    sio.wait()

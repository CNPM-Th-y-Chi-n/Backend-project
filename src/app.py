from flask import Flask
from src.realtime.socket_manager import socketio
from src.api.order_controller import order_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'

    socketio.init_app(app)
    app.register_blueprint(order_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    socketio.run(app, debug=True)

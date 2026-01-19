from flask import Blueprint, request, jsonify
from src.realtime.socket_manager import send_order_to_kitchen

order_bp = Blueprint("order", __name__)

@order_bp.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data"}), 400

    send_order_to_kitchen(data)

    return jsonify({
        "message": "Order received",
        "order": data
    }), 201

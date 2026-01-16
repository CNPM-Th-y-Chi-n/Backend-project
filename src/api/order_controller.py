from flask import request, jsonify
from src.services.order_service import process_order


from flask import Blueprint, request, jsonify
from src.services.order_service import process_order

order_bp = Blueprint("orders", __name__)

@order_bp.route("/orders", methods=["POST"])
def create_order():
    order_data = request.json

    result = process_order(order_data)

    return jsonify({
        "message": "Order sent to kitchen",
        "order": result
    }), 201


from src.realtime.socket_manager import send_order_to_kitchen
from src.realtime.redis_pubsub import publish_order


def process_order(order_data):
    print(" Processing order:", order_data)

    send_order_to_kitchen(order_data)

    publish_order(order_data)

    return order_data

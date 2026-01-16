import json

try:
    import redis
    redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)
    redis_client.ping()
    REDIS_AVAILABLE = True
    print(" Redis connected")
except Exception as e:
    REDIS_AVAILABLE = False
    redis_client = None
    print("⚠️ Redis not available:", e)

CHANNEL = "orders"


def publish_order(order_data: dict):
    if not REDIS_AVAILABLE:
        print(" Redis disabled, skip publish")
        return

    redis_client.publish(CHANNEL, json.dumps(order_data))
    print(" Published order to Redis:", order_data)


def subscribe_orders():
    if not REDIS_AVAILABLE:
        print(" Redis not available, cannot subscribe")
        return

    pubsub = redis_client.pubsub()
    pubsub.subscribe(CHANNEL)

    print(" Kitchen Redis Subscriber started...")
    print(f" Listening on channel: {CHANNEL}")

    for message in pubsub.listen():
        if message["type"] == "message":
            data = json.loads(message["data"])
            print(" New order from Redis:", data)


if __name__ == "__main__":
    subscribe_orders()

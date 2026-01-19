try:
    import redis
except ImportError:
    redis = None

REDIS_CHANNEL = "orders"

def get_redis_client():
    if redis is None:
        return None
    try:
        return redis.Redis(host="localhost", port=6379, decode_responses=True)
    except Exception as e:
        print("Redis not available:", e)
        return None

def publish_order(order_data: dict):
    client = get_redis_client()
    if client:
        client.publish(REDIS_CHANNEL, str(order_data))
        print("Published order to Redis:", order_data)

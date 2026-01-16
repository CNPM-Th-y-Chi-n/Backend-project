class Order:
    def __init__(self, order_id: int, item: str, quantity: int):
        self.id = order_id
        self.item = item
        self.quantity = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "item": self.item,
            "quantity": self.quantity
        }

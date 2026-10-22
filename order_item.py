class OrderItem:
    _used_ids = set()

    def __init__(self, item_id: int, name: str, price: float):
        if item_id in OrderItem._used_ids:
            raise ValueError(f"Item ID {item_id} already exists")

        if not name.strip():
            raise ValueError("Item name cannot be empty")

        if price < 0:
            raise ValueError("Item price cannot be negative")

        OrderItem._used_ids.add(item_id)

        self._id = item_id
        self.name = name
        self.price = float(price)

    @property
    def id(self):
        return self._id

    def __str__(self):
        return f"{self.name} (ID={self.id}, price={self.price:.2f})"

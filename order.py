from abc import ABC, abstractmethod
from datetime import date

from enums import CustomerType, PaymentType
from order_item import OrderItem


class Order(ABC):
    _used_ids = set()

    def __init__(
        self,
        order_id: int,
        name: str,
        delivery_address: str,
        items: list,
        customer,
        payment_type: PaymentType,
        order_date=None
    ):
        if order_id in Order._used_ids:
            raise ValueError(
                f"Order ID {order_id} already exists"
            )

        if not items:
            raise ValueError("Order must contain at least one item")

        if not all(isinstance(item, OrderItem) for item in items):
            raise TypeError("All items must be OrderItem objects")

        self._id = order_id
        self.name = name
        self.delivery_address = delivery_address
        self.items = list(items)
        self.customer = customer
        self.payment_type = payment_type
        self.order_date = order_date or date.today()

        # Validate the order type and calculate the price.
        self.total_price = self.calculate_total_price()

        # Register the ID only after successful initialization.
        Order._used_ids.add(order_id)

        # Every ordered item becomes a customer favorite.
        for item in self.items:
            self.customer.add_favorite_item(item)

    @property
    def id(self):
        return self._id

    @abstractmethod
    def calculate_total_price(self) -> float:
        pass

    def __str__(self):
        item_names = ", ".join(item.name for item in self.items)

        return (
            f"{type(self).__name__}(id={self.id}, "
            f"customer={self.customer.full_name}, "
            f"items=[{item_names}], "
            f"total={self.total_price:.2f}, "
            f"payment={self.payment_type.value})"
        )


class RegularOrder(Order):
    def calculate_total_price(self) -> float:
        return sum(item.price for item in self.items)


class VIPOrder(Order):
    def calculate_total_price(self) -> float:
        if self.customer.customer_type != CustomerType.VIP:
            raise ValueError(
                "VIP order requires a VIP customer"
            )

        discount = self.customer.discount or 0
        subtotal = sum(item.price for item in self.items)

        return subtotal * (1 - discount)

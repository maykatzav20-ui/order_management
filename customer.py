from enums import CustomerType
from order_item import OrderItem


class Customer:
    _used_ids = set()

    def __init__(
        self,
        customer_id: int,
        first_name: str,
        last_name: str,
        email: str,
        delivery_address: str,
        customer_type: CustomerType,
        discount=None
    ):
        if customer_id in Customer._used_ids:
            raise ValueError(
                f"Customer ID {customer_id} already exists"
            )

        if discount is not None and not 0 <= discount <= 1:
            raise ValueError(
                "Discount must be between 0 and 1"
            )

        if customer_type != CustomerType.VIP and discount is not None:
            raise ValueError(
                "Only VIP customers can have a discount"
            )

        Customer._used_ids.add(customer_id)

        self._id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.discount = discount

        self.favorite_items = []
        self.gift = None

    @property
    def id(self):
        return self._id

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def add_favorite_item(self, item: OrderItem):
        # Items with the same name are considered identical.
        for favorite in self.favorite_items:
            if favorite.name.casefold() == item.name.casefold():
                return

        self.favorite_items.append(item)

    def remove_favorite_item(self, item_name: str):
        self.favorite_items = [
            item for item in self.favorite_items
            if item.name.casefold() != item_name.casefold()
        ]

    def update_favorite_items(self, add=None, remove=None):
        for item in add or []:
            self.add_favorite_item(item)

        for item_name in remove or []:
            self.remove_favorite_item(item_name)

    def take_gift(self, gift):
        if not callable(getattr(gift, "open_gift", None)):
            raise TypeError(
                "Gift must implement open_gift()"
            )

        self.gift = gift

    def open_gift(self):
        if self.gift is None:
            print("You don't have a gift yet.")
            return

        self.gift.open_gift()

    def __str__(self):
        return (
            f"Customer(id={self.id}, name={self.full_name}, "
            f"type={self.customer_type.value})"
        )

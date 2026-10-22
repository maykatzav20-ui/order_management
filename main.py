from enums import CustomerType, PaymentType
from order_item import OrderItem
from customer import Customer
from gift import SurpriseGift
from order import RegularOrder, VIPOrder
from animals import Spider, Cat, Fish


def main():
    print("=== Customer Order Management ===")

    # Create order items
    laptop = OrderItem(1, "Laptop", 3000)
    mouse = OrderItem(2, "Mouse", 100)
    keyboard = OrderItem(3, "Keyboard", 200)

    # Create customers
    regular_customer = Customer(
        1,
        "David",
        "Cohen",
        "david@example.com",
        "Tel Aviv",
        CustomerType.REGULAR
    )

    vip_customer = Customer(
        2,
        "Dana",
        "Levi",
        "dana@example.com",
        "Jerusalem",
        CustomerType.VIP,
        discount=0.20
    )

    # Create a regular order
    regular_order = RegularOrder(
        1,
        "Regular purchase",
        regular_customer.delivery_address,
        [mouse, keyboard],
        regular_customer,
        PaymentType.CREDIT_CARD
    )

    # Create a VIP order
    vip_order = VIPOrder(
        2,
        "VIP purchase",
        vip_customer.delivery_address,
        [laptop, mouse],
        vip_customer,
        PaymentType.CASH
    )

    print("\n--- Orders ---")
    print(regular_order)
    print(vip_order)

    # Automatic favorite items
    print("\n--- Favorite items ---")
    for item in regular_customer.favorite_items:
        print(item.name)

    # Same name, different ID: should not be added twice
    another_mouse = OrderItem(4, "Mouse", 120)
    regular_customer.add_favorite_item(another_mouse)

    print(
        "Favorites after duplicate name:",
        [item.name for item in regular_customer.favorite_items]
    )

    # Update favorites: add and remove
    regular_customer.update_favorite_items(
        add=[laptop],
        remove=["Keyboard"]
    )

    print(
        "Favorites after update:",
        [item.name for item in regular_customer.favorite_items]
    )

    # Give and open a gift
    print("\n--- Gift ---")
    vip_customer.take_gift(SurpriseGift())
    vip_customer.open_gift()

    # Verify that a regular customer cannot create a VIP order
    print("\n--- Invalid VIP order ---")
    try:
        VIPOrder(
            3,
            "Invalid purchase",
            regular_customer.delivery_address,
            [mouse],
            regular_customer,
            PaymentType.CHECK
        )
    except ValueError as error:
        print("Error:", error)

    # UML bonus
    print("\n--- Animal UML Bonus ---")
    spider = Spider()
    cat = Cat("Milo")
    fish = Fish("Nemo")

    spider.walk()
    spider.eat()

    print("Cat name:", cat.getName())
    cat.play()
    cat.walk()
    cat.eat()

    print("Fish name:", fish.getName())
    fish.setName("Goldie")
    fish.play()
    fish.walk()
    fish.eat()


if __name__ == "__main__":
    main()


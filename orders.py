class Order:
    def __init__(self) -> None:
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity # if cart is already available
        else:
            self.items[item] = quantity #if the cart dont have any item

    def remove(self, item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def clear(self):
        self.items = {}

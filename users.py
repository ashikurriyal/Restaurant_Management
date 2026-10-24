# Customer
# Employee
# Admin

from abc import ABC, abstractmethod
from orders import Order

class User(ABC):
    @abstractmethod
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item is None:
            print("Item not found")
        elif quantity <= 0:
            print("Quantity must be at least 1")
        elif self.cart.items.get(item, 0) + quantity > item.quantity:
            print("Item Quantity Exceeded!!")
        else:
            self.cart.add_item(item, quantity)
            print("Item Added")

    def view_cart(self):
        print("***** View Cart *****")
        if not self.cart.items:
            print("Your cart is empty")
            return
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price:.2f}\t{quantity}")
        print(f"Total Price: {self.cart.total_price:.2f}")

    def pay_bill(self):
        if not self.cart.items:
            print("Your cart is empty")
            return
        for item, quantity in self.cart.items.items():
            item.quantity -= quantity # reduce stock only after payment
        print(f"Total {self.cart.total_price:.2f} paid successfully!!")
        self.cart.clear()


class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)

    def view_employee(self, restaurent):
        restaurent.view_employee()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

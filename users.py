# Customer
# Employee
# Admin

from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item Quantity Exceeded!!")
            else: 
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item Added")
        else:
            print("Item not found")

    def view_cart(self):
        print("***** View Cart *****")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price}")

    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid successfully!!")
        self.cart.clear()


class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary            

# emp = Employee("Rahim", "rahim@gmail.com", 12567443, "Dhaka", 23, "Chef", 12000)
# print(emp.name)

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)


    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)

    def view_employee(self, restaurent):
        restaurent.view_employee()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self, restaurent, item):
            restaurent.remove_item(item)





res = Restaurent("Khanas")
mn = Menu()
item = FoodItem("Burger", 50.35, 10)
item2 = FoodItem("Pizza", 20.55, 7)
admin = Admin("Ali", "ali@gmail.com", 2342342, "Dhaka")
admin.add_new_item(res, item)
admin.add_new_item(res, item2)

customer1 = Customer("Samir", "samir@gmail.com", 2342342, "Dhaka")
customer1.view_menu(res)


item_name = input("Enter item name: ")
item_quantity = int(input("Enter Item Quantity: "))

customer1.add_to_cart(res, item_name, item_quantity)
customer1.view_cart()
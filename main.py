from food_item import FoodItem
from users import Customer, Admin, Employee
from restaurent import Restaurent


res = Restaurent("Bhai Bhai Restaurent")
res.menu.add_menu_item(FoodItem("Burger", 50.35, 10))
res.menu.add_menu_item(FoodItem("Pizza", 20.55, 7))


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number")


def customer_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")
    customer = Customer(name = name, email = email, phone = phone, address = address)

    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice = read_int("Enter Your Choice: ")
        if choice == 1:
            customer.view_menu(res)
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = read_int("Enter item quantity: ")
            customer.add_to_cart(res, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Input")


def admin_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")
    admin = Admin(name = name, email = email, phone = phone, address = address)

    while True:
        print(f"Welcome {admin.name}!!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")

        choice = read_int("Enter Your Choice: ")
        if choice == 1:
            item_name = input("Enter item name: ")
            if res.menu.find_item(item_name):
                print("Item already exists")
                continue
            item_price = read_float("Enter item price: ")
            item_quantity = read_int("Enter item quantity: ")
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(res, item)
        elif choice == 2:
            name = input("Enter employee name: ")
            email = input("Enter employee email: ")
            phone = input("Enter employee phone: ")
            address = input("Enter employee address: ")
            age = read_int("Enter employee age: ")
            designation = input("Enter employee designation: ")
            salary = read_int("Enter employee salary: ")
            employee = Employee(name, email, phone, address, age, designation, salary)
            admin.add_employee(res, employee)
        elif choice == 3:
            admin.view_employee(res)
        elif choice == 4:
            admin.view_menu(res)
        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(res, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    while True:
        print("Welcome!!")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")

        choice = read_int("Enter Your Choice: ")
        if choice == 1:
            customer_menu()
        elif choice == 2:
            admin_menu()
        elif choice == 3:
            break
        else:
            print("Invalid Input")

from food_item import FoodItem
from menu import Menu
from users import Customer, Admin, Employee
from restaurent import Restaurent
from orders import Order


res = Restaurent("Bhai Bhai Restaurent")


def customer_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")
    customer = Customer (name = name, email = email, phone = phone, address = address)

    while True:
        print(f"Welcome {customer.name}!!")
        print ("1. View Menu")
        print ("2. Add item to cart")
        print ("3. View Cart")
        print ("4. PayBill")
        print ("5. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            customer.view_menu(res)
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity : "))
            customer.add_to_cart(res, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Input")

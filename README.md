# Restaurant Management System

A command-line restaurant management system written in Python, built to practice Object-Oriented Programming (inheritance, abstraction, encapsulation and composition).

## Features

**Customer**
- View the menu
- Add items to the cart (checked against available stock)
- View the cart with the total price
- Pay the bill (stock is reduced after payment)

**Admin**
- Add new food items to the menu
- Delete items from the menu
- View all menu items
- Add new employees
- View the employee list

## Project Structure

| File | Description |
|------|-------------|
| `main.py` | Entry point with the customer and admin menus |
| `users.py` | `User` (abstract base class), `Customer`, `Employee` and `Admin` |
| `restaurent.py` | `Restaurent` class that holds the menu and the employees |
| `menu.py` | `Menu` class to add, find, remove and show food items |
| `food_item.py` | `FoodItem` class (name, price, quantity) |
| `orders.py` | `Order` class used as the customer's cart |

## How to Run

Requires Python 3. No external packages are needed.

```bash
python3 main.py
```

Choose **1** for Customer or **2** for Admin, then follow the on-screen menu. The menu starts with Burger and Pizza so a customer can order right away.

# Customer
# Employee
# Admin

from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

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
        self.employees = [] # This is the databse

    def add_employee(self, name, email, phone, address, age, designation, salary):
        employee = Employee(name, email, phone, address, age, designation, salary) #object of an employee class
        self.employees.append(employee)
        print(f"{name} is added!!")

    def view_employee(self):
        print("Employee List!!")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)

ad = Admin("Riyad", "2346762374", "riyad@gmail.com", "Dhaka")
ad.add_employee("Sagor", "sagor@gmail.com", "123123123", "Kushtia", 32, "Chef", 12000)

ad.view_employee()
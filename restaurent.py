from menu import Menu

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = [] # This is the databse
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List!!")
        if not self.employees:
            print("No employees yet")
            return
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address, emp.age, emp.designation, emp.salary)

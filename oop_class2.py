# Create Multiple Objects of Python Class
class Employee:
    employee_id = 0
    name = ""


employee1 = Employee()
employee2 = Employee()

employee1.employeeID = 10001
employee1.name='Caren'
print(f"Name:{employee1.name}, Employee ID:{employee1.employeeID}")

employee2.employeeID = 10002
employee2.name='Suchi'
print(f"Name:{employee2.name}, Employee ID:{employee2.employeeID}")

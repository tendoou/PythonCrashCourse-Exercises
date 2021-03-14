class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount


new_employee = Employee("Diego", "Beltrán", 100000)
new_employee.give_raise()


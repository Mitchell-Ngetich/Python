class Employee:
    def __init__(self, first, last, salary):
        self.first =  first
        self.last =  last
        self.salary =  salary
        self.email = first + "." + last + "@company.com"
    
emp_1 = Employee("Mitchell", "Ngetich", 5000)
print(emp_1.email)
print(emp_1.first)
print(emp_1.last)


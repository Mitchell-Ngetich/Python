class Employee:
    def __init__(self, first, last, salary):
        self.first =  first
        self.last =  last
        self.salary =  salary
        self.email = first + "." + last + "@company.com"
    
    def __str__(self):
        return f'Employee({self.first}, {self.last}, {self.salary}, {self.email})'
    
emp_1 = Employee(Mitchell, Ngetich, 5000)
print(emp_1)


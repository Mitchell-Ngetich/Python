class Employee:
    def __init__(self, first, last, salary):
        self.first =  first
        self.last =  last
        self.salary =  salary
        self.email = first + "." + last + "@company.com"
    
    def fullname(self):
        return f"{self.first} {self.last}" #always use two braces
    
emp_1 = Employee("Mitchell", "Ngetich", 5000)
print(Employee.fullname(emp_1))

print(emp_1.fullname())


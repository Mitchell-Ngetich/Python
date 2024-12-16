class Employee:
    def __init__(self, first, last, salary):
        self.first =  first
        self.last =  last
        self.salary =  salary
        self.email = first + "." + last + "@company.com"
    
    def fullname(self):
        return f"{self.first} {self.last}" #always use two braces
    
"""below will print the same thing. when we call the method on a class we have to pass in the instance as
an argument, but we can call the instance by itself then add self as an argument to the class method"""
emp_1 = Employee("Mitchell", "Ngetich", 5000)
# print(Employee.fullname(emp_1)) """this is calling a method on the class. Less common as you have to pass in 
# instance as a variable"""

print(emp_1.fullname())


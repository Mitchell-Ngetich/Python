# class Employee:
#     def __init__(self, first, last, salary):
#         self.first =  first
#         self.last =  last
#         self.salary =  salary
#         self.email = first + "." + last + "@company.com"
    
#     def fullname(self):
#         return f"{self.first} {self.last}" #always use two braces
    
# """below will print the same thing. when we call the method on a class we have to pass in the instance as
# an argument, but we can call the instance by itself then add self as an argument to the class method"""
# emp_1 = Employee("Mitchell", "Ngetich", 5000)
# print(Employee.fullname(emp_1)) """this is calling a method on the class. Less common as you have to pass in 
# instance as a variable"""

# print(emp_1.fullname())

# class Salary:
#     def __init__(self, base_salary,bonus):
#         self.base_salary = base_salary
#         self.bonus = bonus

#     def Total_salary(self):
#         return f"{self.base_salary + self.bonus}"

# emp_salary = Salary(50000, 20000)
# print(emp_salary.Total_salary())

#NUMPY

import random

salary_list = [random.randint(1000, 500000) for int in range(100000)]
import statistics
print(statistics.mean(salary_list))

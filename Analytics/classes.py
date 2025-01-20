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

# import timeit
# print(statistics.mean(salary_list))

import numpy as np
# a = np.array([1,2,3])
# print(a.mean())

# job_titles = np.array([6000, 80000, 75000])

# EXCERCISE
# You are given the scores of students in three subjects: Math, Science, and English.
# Your task is to perform the following operations using NumPy:
# a) Create a NumPy array with the scores of 5 students in each subject.
# b) Calculate the average score for each subject.
# c) Determine which student has the highest score in each subject.
# d) Calculate the overall average score for all students across all subjects.
# e) Create a new array that contains only the scores of students who scored above the overall average in all subjects


# a) Create a NumPy array with the scores of 5 students in each subject.
scores = np.array([
    [80, 60, 70],
    [50, 60, 56],
    [58, 67, 90],
    [88, 89, 78],
    [90, 80, 60]
])

subjects = ["Math", "Science", "English"]

# b) Calculate the average score for each subject.
subjects_mean = np.mean(scores, axis = 0)
print(subjects_mean)

# c) Determine which student has the highest score in each subject.
highest_score = scores.max(axis = 0) #calculates max in each column

for i, subject in enumerate(subjects):
    print(f"{subject} : {highest_score[i]}")

#  d) Calculate the overall average score for all students across all subjects
overall_mean = np.mean(scores)
print(overall_mean)

#  e) Create a new array that contains only the scores of students who scored above the overall average in all subjects

new_array = []

for score in scores:
    if np.all(score > overall_mean):
        new_array.append(score)

new_array = np.array(new_array)
print(new_array)
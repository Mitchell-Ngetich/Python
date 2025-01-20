# print("hello world")

# numbers1 = []
# for number in range(100):
#     numbers1 += [number] # this is same as using append method, although not recommended
# print(numbers1)

# number = []
# for x in range(100):
#     number.append(x)
# print(number)

# lambda_1 = lambda x,y: x * y
# print(lambda_1(5,9))

# def lambda_2():
#     return lambda x,y: x * y
# my_lambda = lambda_2()
# print(my_lambda(5,9))

# Salary = [10000, 20000, 30000, 40000, 50000]
# total_salary = [(lambda x: x * 1.2)(salary) for salary in Salary]
# print(total_salary)

# total_salary = [salary * 1.2 for salary in Salary]
# print(total_salary)

# def calculate_salary(salary, bonus = 1.2):
#     return salary * bonus

# Salary = [10000, 20000, 30000, 40000, 50000]
# total_salary = list(map(calculate_salary, Salary))
# print(total_salary)

import numpy as np

# zeros_array = np.zeros((2, 3)) 
# print(zeros_array)

# ones_array = np.ones((3, 4)) #prints an array of 1(3 rows, 4 colums)
# print(ones_array)

# random_array = np.random.random((2, 2))  # Creates a 2x2 array with random values
# print(random_array)
# np.random is a module, not a direct function. It contains various functions for generating random numbers, such as:
# np.random.random(): For random floats between 0 and 1.
# np.random.randint(): For random integers.
# np.random.normal(): For random numbers from a normal (Gaussian) distribution.
# np.random.rand(): For uniformly distributed random numbers, with simpler syntax for arrays.

# PANDAS
# import pandas as pd

from datasets import load_dataset

dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
print(df.info())


# DATA CLEANING


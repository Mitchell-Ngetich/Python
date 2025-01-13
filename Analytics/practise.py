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

random_array = np.random.randint((2, 2))  # Creates a 2x2 array with random values
print(random_array)

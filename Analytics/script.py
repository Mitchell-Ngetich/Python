# print(2+2)
# print(3 * 3)

# salary = 10000
# print(salary)

# company_name = "Hapag-Lloyd shipping company"
# print(company_name)
# job_wfh = True
# print(job_wfh)
# print(type(salary))
# print(type(company_name))
# print(type(job_wfh))

#functions
# def greetings():
#     return "how are you Ser?"
# print(greetings()) */

# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!")
#     print(f"How old are you!, {age}")
#     print(f"Happy birthday dear {name}!")
# happy_birthday("Ser", 25)
# happy_birthday("Joy", 9)
# happy_birthday("Pepe", 9)

# def add(a,b):
#     return a * b
# print(add(5,9))

# def full_name(first_name, last_name):
#     first = first_name.capitalize()
#     last = last_name.capitalize()
#     final_name = first + " " + last
#     return final_name
# print(full_name("ser","mitch"))

# job = "Data Analyst"
# print(job.replace("a", "o"))

# skills = ["rpa", "salesforce","odex", "Qlikview", "Tableau"]
# # print(type(skills))
# print(",".join(skills)) 

# x = 10
# if x > 5:
#     pass # pass is a keyword that does nothing
# else: print("x is equal or less than 5")
#loops
# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# for fruit in fruits:
#     print(fruit)

# numbers =[x for x in range(100)]
# print(numbers)

# numbers1 = []
# for number in range(100):
#     numbers1 =+ 1
# print(numbers1)

# MODULES
# import my_module as mine

# print(mine.greetings("Sophie"))

from datetime import datetime, date

time = datetime.now()
# print(time)

data_science_jobs = [
    {"job_title": "Data Scientist", "job_skills": "['python','SQL','Machine Learning']", "job_date": "2024-12-04"},
    {"job_title": "Data Analyst", "job_skills": "['Excel','SQL','Power BI']", "job_date": "2024-12-01"},
    {"job_title": "Machine Learning Engineer", "job_skills": "['python','TensorFlow','Keras']", "job_date": "2024-11-30"},
    {"job_title": "Business Intelligence Analyst", "job_skills": "['Tableau','Power BI','SQL']", "job_date": "2024-11-28"},
    {"job_title": "Big Data Engineer", "job_skills": "['Hadoop','Spark','Kafka']", "job_date": "2024-11-25"},
    {"job_title": "Data Engineer", "job_skills": "['python','SQL','ETL']", "job_date": "2024-11-23"},
    {"job_title": "AI Researcher", "job_skills": "['Deep Learning','NLP','PyTorch']", "job_date": "2024-11-22"},
    {"job_title": "Statistician", "job_skills": "['R','Mathematics','Data Analysis']", "job_date": "2024-11-20"},
    {"job_title": "Data Architect", "job_skills": "['Database Design','NoSQL','Cloud']", "job_date": "2024-11-18"},
    {"job_title": "Quantitative Analyst", "job_skills": "['Matlab','Statistics','Python']", "job_date": "2024-11-15"},
    {"job_title": "ETL Developer", "job_skills": "['ETL','SQL','Informatica']", "job_date": "2024-11-12"},
    {"job_title": "Data Visualization Specialist", "job_skills": "['D3.js','JavaScript','Tableau']", "job_date": "2024-11-10"},
    {"job_title": "Database Administrator", "job_skills": "['MySQL','PostgreSQL','Oracle']", "job_date": "2024-11-08"},
    {"job_title": "Data Governance Analyst", "job_skills": "['Data Quality','Compliance','Policy Management']", "job_date": "2024-11-06"},
    {"job_title": "Operations Research Analyst", "job_skills": "['Optimization','Simulation','R']", "job_date": "2024-11-04"},
]

# my_time = data_science_jobs[2]["job_date"]

# format_time = datetime.strptime(my_time, "%Y-%m-%d") #convert string to datetime object

# formatted_time = format_time.strftime("%Y-%m-%d") #removes the zeros in the time to remain only with Y,M,D.

# print(formatted_time)

# # NOW LOOP IN AND REPLACE THE DATE WITH THE FORMATTED DATE
# for job in data_science_jobs:
#     job["job_date"] = formatted_time
# print(data_science_jobs)

#FILTER JOBS THAT HAVE PYTHON IN JOB SKILLS


for job in data_science_jobs:
    if "python" in job["job_skills"]:
        print(job)
    else:
        print("No python in job skills")
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

job_data = [
    {
        "job_title": "Data Scientist",
        "job_skills": ["Python", "Machine Learning", "SQL", "Data Visualization", "Deep Learning"],
        "remote": True
    },
    {
        "job_title": "Data Analyst",
        "job_skills": ["Excel", "Power BI", "SQL", "Communication", "Data Cleaning"],
        "remote": False
    },
    {
        "job_title": "Machine Learning Engineer",
        "job_skills": ["Python", "TensorFlow", "PyTorch", "AWS", "Big Data"],
        "remote": True
    },
    {
        "job_title": "Business Intelligence Analyst",
        "job_skills": ["SQL", "Tableau", "Power BI", "Storytelling", "ETL"],
        "remote": False
    },
    {
        "job_title": "Data Engineer",
        "job_skills": ["Spark", "Hadoop", "SQL", "Python", "Data Warehousing"],
        "remote": True
    },
    {
        "job_title": "AI Researcher",
        "job_skills": ["Artificial Intelligence", "Python", "NLP", "Deep Learning", "Computer Vision"],
        "remote": False
    },
    {
        "job_title": "Statistician",
        "job_skills": ["Statistics", "R", "Mathematics", "Data Analysis", "SPSS"],
        "remote": True
    },
    {
        "job_title": "Big Data Analyst",
        "job_skills": ["Hadoop", "Spark", "SQL", "Scala", "Data Processing"],
        "remote": True
    },
    {
        "job_title": "Product Data Analyst",
        "job_skills": ["Excel", "SQL", "A/B Testing", "Python", "Statistics"],
        "remote": False
    },
    {
        "job_title": "Financial Data Analyst",
        "job_skills": ["Excel", "Finance", "Python", "Financial Modeling", "SQL"],
        "remote": False
    },
    {
        "job_title": "Data Architect",
        "job_skills": ["Data Modeling", "ETL", "SQL", "Cloud Computing", "Python"],
        "remote": True
    },
    {
        "job_title": "Quantitative Analyst",
        "job_skills": ["Mathematics", "Statistics", "R", "Python", "Risk Analysis"],
        "remote": False
    },
    {
        "job_title": "Healthcare Data Scientist",
        "job_skills": ["Python", "R", "Healthcare Analytics", "Statistics", "Data Visualization"],
        "remote": True
    },
    {
        "job_title": "Marketing Data Analyst",
        "job_skills": ["Google Analytics", "Excel", "SQL", "Marketing Metrics", "Python"],
        "remote": False
    },
    {
        "job_title": "Operations Research Analyst",
        "job_skills": ["Operations Research", "Linear Programming", "Optimization", "Python", "R"],
        "remote": True
    },
    {
        "job_title": "Fraud Detection Specialist",
        "job_skills": ["Machine Learning", "Python", "SQL", "Data Mining", "Cybersecurity"],
        "remote": True
    },
    {
        "job_title": "Energy Data Analyst",
        "job_skills": ["Energy Models", "R", "Python", "Data Cleaning", "Data Visualization"],
        "remote": False
    },
    {
        "job_title": "E-commerce Data Scientist",
        "job_skills": ["A/B Testing", "Python", "SQL", "Customer Analytics", "Machine Learning"],
        "remote": True
    },
    {
        "job_title": "Logistics Data Analyst",
        "job_skills": ["Supply Chain", "Optimization", "SQL", "Python", "Tableau"],
        "remote": False
    },
    {
        "job_title": "Natural Language Processing Engineer",
        "job_skills": ["NLP", "Python", "SpaCy", "Hugging Face", "Machine Learning"],
        "remote": True
    }
]


my_jobs = lambda job: job["remote"] and "Python" in job["job_skills"]

remote_jobs = list(filter(my_jobs, job_data))

print(remote_jobs)

# my_jobs = [job for job in job_data if job["remote"] == True]
# print(my_jobs)

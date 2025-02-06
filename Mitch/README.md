# The Analysis

## 1. What are the most demanded skills for the top 3 most popular data roles?

To find the most demanded skills for the top 3 most popular data roles. I filtered out those positions by the most popular, and got the top 5 skills for these 3 roles. This query highlights the most popular job titles and their top skills, showing which skills we should pay attention to depending on the role we're targeting.

View my notebook with detailed steps here:
[2_Skill_Demand.ipynb](3_Project/2_Skill_Demand.ipynb)

### Visualize Data

```python
fig, ax = plt.subplots(len(job_titles), 1)
sns.set_theme(style="ticks")

for i, job_title in enumerate(job_titles):
    df_plot = df_skills_perc[df_skills_perc["job_title_short"] == job_title].head(5)
    sns.barplot(data=df_plot, x="skill_percent", y="job_skills",ax=ax[i], hue="skill_count", palette="dark:b_r" , legend=False)
    ax[i].set_title(job_title)
    ax[i].set_ylabel("")
    ax[i].set_xlabel("")
    ax[i].set_xlim(0, 78)
    
    for n, v in enumerate(df_plot["skill_percent"]):
        ax[i].text(v + 1,n, f"{v:.0f}%", va="center")

    if i != len(job_titles) - 1:
        ax[i].set_xticks([])

fig.suptitle("Likelihood of Top Skills in US  Job Postings", fontsize=15)
fig.tight_layout()
plt.show()
```

### Results

[Visualization of Top Skills](3_Project/Images/top_skills.png)

### Insights

- Python is a versatile skill, highly demanded across all the 3 roles, but mostly prominently for DS(72%) and DE(65%).
- SQL is the most requested skill for DA and DS, with it in over half the job posting for both roles. For DE, Python is the most sought skill with a percentage of 68%.
-  Data Engineers require more specialized technical skills(AWS, Azure, Spark) compared to Data Analysts and Data Scientists who are expected to be proficient in more general data management and analysis tools(Excel, Tableau).
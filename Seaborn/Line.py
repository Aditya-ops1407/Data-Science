import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

stu = {
    "Student": ["Aditya","Rohan","Priya","Kunal","Sneha","Aryan","Neha"],
    "Roll no": [1,2,3,4,5,6,7],
    "Course": ["BCA","BCA","BBA","BCA","BBA","BCA","BBA"],
    "Marks": [85,72,90,60,78,95,88],
    "City": ["Lucknow","Delhi","Mumbai","Delhi","Lucknow","Mumbai","Delhi"]
}

df = pd.DataFrame(stu)

sns.lineplot(x = "Roll no", y = "Marks", data=df)
plt.title("Student Marks")
plt.show()


df1 = pd.read_csv("hr_data.csv")
print(df1.head())

plt.style.use("dark_background")
plt.figure(figsize=(12,6))
sns.lineplot(x="number_project", y="average_montly_hours", data=df1,hue="left") #Hue is used for differentiating data between Left and working
plt.show()

plt.style.use("dark_background")
sns.lineplot(x="promotion_last_5years", y="left", style="salary", data=df1) #Style is used for differentiating data between different salaries
plt.show()

plt.style.use("dark_background")
plt.figure(figsize=(12,6))
sns.lineplot(x="department", y="left", data=df1)
plt.show()
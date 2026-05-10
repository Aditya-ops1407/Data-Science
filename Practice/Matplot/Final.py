import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Department": ["IT","HR","Finance","IT","HR","Finance","IT","HR"],
    
    "Employee": ["Aman","Priya","Rohit","Sneha","Kunal","Neha","Aryan","Pooja"],
    
    "Salary": [60000,45000,70000,65000,48000,72000,75000,50000],
    
    "Experience": [2,1,5,3,2,6,4,2]
}

df = pd.DataFrame(data)

print(df.groupby("Department")["Salary"].mean())

avg = pd.DataFrame(df.groupby("Department")["Salary"].mean())
print(avg)

plt.style.use("dark_background")
color = ['red','green','blue']

plt.bar(avg.index,avg["Salary"],color=color,edgecolor="white")
plt.title("Department vs Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

print(avg[avg["Salary"]==avg["Salary"].max()])

contribution = pd.DataFrame(df.groupby("Department")["Salary"].sum())

plt.pie(contribution["Salary"],labels=contribution.index,autopct="%0.2f%%", colors= color)
plt.title("Salary Contribution of Departments")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student":['Aditya','Abhay','Nitin','Ansh','Anand'],
    "Marks":[88,89,75,98,84]
}

df = pd.DataFrame(data)
print(df)

plt.style.use("dark_background")
color = ['red','green','blue','orange','cyan']

plt.bar(df["Student"],df["Marks"], color=color, edgecolor="white")
plt.title("Student Marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()
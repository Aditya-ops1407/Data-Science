import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Study_Hours": [1,2,3,4,5,6,7,8,9,10],
    
    "Marks": [35,40,50,55,65,70,75,85,90,95],
    
    "Gender": ["Male","Female","Male","Female","Male",
               "Female","Male","Female","Male","Female"]
}

df = pd.DataFrame(data)

plt.style.use("dark_background")
sns.scatterplot(x = "Study_Hours", y="Marks",data=df, hue="Gender", palette="inferno", style="Gender", size="Marks")
plt.title("Study Hours vs Marks")
plt.grid()
for i in range(len(df["Gender"])):
    plt.text(df["Study_Hours"][i],df["Marks"][i],df["Gender"][i])
plt.show()

# Mixing Line and Scatter

df1 = pd.read_csv("titanic.csv")
plt.style.use("dark_background")
plt.figure(figsize=(14,8))
sns.scatterplot(x = "age", y="fare",data=df1, hue="sex", palette="inferno", style="sex", size="fare", alpha=0.5)
sns.lineplot(x = "age", y="fare",data=df1, color="yellow")
plt.title("Age vs Fare")
plt.show()
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Department": ["IT","HR","Finance","Marketing","Sales"],
    
    "Average_Salary": [75000, 50000, 82000, 60000, 68000]
}

df = pd.DataFrame(data)

plt.style.use("dark_background")
sns.barplot(x="Department", y = "Average_Salary", data=df,hue="Department", palette="flare")
plt.title("Department vs average salary")
plt.grid()
plt.show()

df1 = pd.read_csv("titanic.csv")

plt.style.use("dark_background")
sns.barplot(x="class", y = "fare", data=df1,hue="sex", palette="inferno", saturation=0.9)
plt.title("Fare of different classes according to gender")
plt.show()

#Orient
plt.style.use("dark_background")
sns.barplot(y="class", x = "fare", data=df1,hue="sex", palette="icefire", orient='h')
plt.title("Same graph in horizontal")
plt.show()
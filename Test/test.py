import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data.csv")

fruit_quan = df.groupby("Fruit_Type")["Quantity"].sum()

plt.style.use("dark_background")
color = ['red','lime','green','orange']

plt.bar(fruit_quan.index, fruit_quan.values, color = color)
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.show()

explode = [0.1,0.2,0.1,0.1]
plt.pie(fruit_quan.values , labels= fruit_quan.index , colors= color , autopct= '%0.2f%%', explode=explode)
plt.show()
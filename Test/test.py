import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data.csv")

fruit_quan = df.groupby('Fruit_Type')['Quantity'].sum() #Using group by and then sum function to calculate quantity of each fruit
print(fruit_quan)

colour = ['red','green','lime','orange']
plt.style.use('dark_background')
plt.bar(fruit_quan.index, fruit_quan.values, color = colour)
plt.xlabel("Fruits")
plt.ylabel("Quantities")
plt.title("Fruit Quantities")
plt.show()

plt.pie(fruit_quan.values, labels = fruit_quan.index, colors = colour, autopct='%f.1%%')
plt.show()
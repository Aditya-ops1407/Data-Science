#Create a data frame of temperature vs humididty of 5 cities and visualize it

import pandas as pd
import matplotlib.pyplot as plt

dict = {
    'City':['Delhi','Jaipur','Mumbai','Patna','Kolkata'],
    'Temperature': [42,44,33,40,41],
    'Humidity': [60,45,84,74,79]
}

df = pd.DataFrame(dict)

plt.scatter(df["Temperature"], df["Humidity"])
for i in range(len(df)):
    plt.text(df["Temperature"][i],
             df["Humidity"][i],
             df["City"][i])

plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Temperature vs Humidity")

plt.show()
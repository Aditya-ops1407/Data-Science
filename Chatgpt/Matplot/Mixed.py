import pandas as pd
import matplotlib.pyplot as plt
data = {
    "City":["Delhi","Mumbai","Lucknow","Chennai","Kolkata"],
    "Sales":[200,350,180,250,300]
}

df = pd.DataFrame(data)

plt.style.use("dark_background")
color = ['red','blue','lime','yellow','purple']

plt.bar(df["City"],df["Sales"],color=color, edgecolor="white")
plt.title("City wise sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.show()

plt.pie(df["Sales"],labels=df["City"],autopct="%0.2f%%",colors=color, explode=[0.1,0.1,0.1,0.1,0.1])
plt.title("City wise sales comparison")
plt.show()

#Finding city with max sales
print(df[df["Sales"]==df["Sales"].max()])
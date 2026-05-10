import pandas as pd
import matplotlib.pyplot as plt

data = {"Brands":["Apple","Samsung","Xiaomi","Motorola","Realme"],
        "Users":[984567,876514,1154668,456276,1348527]}

df = pd.DataFrame(data)

plt.style.use("dark_background")
explode = [0,0,0.1,0,0]
color = ['red','blue','orange','green','gold']

plt.pie(df["Users"], labels= df["Brands"], autopct="%0.2f%%", colors= color, explode= explode)
plt.title("Users of different mobile brands")
plt.show()
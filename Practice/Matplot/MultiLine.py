import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Months":['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    "Product A":[12,15,10,55,44,32,5,4,3,7,6,9],
    "Product B":[31,41,1,3,5,7,61,45,25,31,74,84]
}

df = pd.DataFrame(data)

plt.style.use("dark_background")
plt.figure(figsize=(8,5))
plt.plot(df["Months"],df["Product A"],'-y', label="Product A")
plt.plot(df["Months"],df["Product A"],'wo')
plt.plot(df["Months"],df["Product B"],'-r', label="Product B")
plt.plot(df["Months"],df["Product B"],'bo')
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Comparison of product sales")
plt.legend()
plt.show()
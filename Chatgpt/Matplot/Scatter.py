import pandas as pd
import matplotlib.pyplot as plt

data = {'Study Hours': [2,3,4,4, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12],
'Marks' : [6, 10, 15, 20, 34, 44, 55, 60, 55, 67, 70, 80, 90, 99, 100]
}

df = pd.DataFrame(data)

plt.style.use("dark_background")
plt.scatter(df["Study Hours"],df["Marks"], alpha=0.7, color='yellow')
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.grid()
plt.show()
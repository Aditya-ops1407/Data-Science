import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Height": [150, 155, 160, 162, 165, 168, 170, 172, 175, 178],
    "Weight": [45, 50, 54, 56, 60, 63, 65, 68, 72, 75]
}

df = pd.DataFrame(data)

print(df)

plt.style.use("dark_background")
plt.scatter(df["Height"],df["Weight"], alpha=0.7, color='yellow')
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight")
plt.grid()
plt.show()
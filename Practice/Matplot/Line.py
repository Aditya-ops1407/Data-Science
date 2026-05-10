import pandas as pd
import matplotlib.pyplot as plt

temp = {
    "Days":['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
    "Temperature":[44,43,38,37,41,40,35]
}

df = pd.DataFrame(temp)

plt.style.use("dark_background")
plt.figure(figsize=(8,5))
plt.plot(df["Days"],df["Temperature"], '-y')
plt.plot(df["Days"],df["Temperature"], 'wo')
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Temperature over a week")
plt.show()
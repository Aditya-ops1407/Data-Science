import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd

data = {
    "Math": [85, 78, 90, 66, 72, 95, 88, 76],
    
    "Science": [80, 74, 92, 60, 70, 96, 85, 73],
    
    "English": [78, 72, 89, 64, 68, 91, 84, 70],
    
    "Computer": [90, 85, 95, 70, 75, 99, 92, 80]
}

df = pd.DataFrame(data)
print(df.corr())
sns.heatmap(df.corr(), annot=True)
plt.show()

df1 = pd.read_csv("flights.csv")
flight_df = df1.pivot(index="month",columns="year",values="passengers")
print(flight_df)
print(flight_df.corr())

plt.figure(figsize=(12,6))
sns.heatmap(flight_df.corr(), annot=True)
plt.show()
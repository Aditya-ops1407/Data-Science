import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Course":["BCA","BBA","B.Com","B.Tech","BA"],
    "Students":[60,74,85,45,98]
}

df = pd.DataFrame(data)

plt.style.use("dark_background")
color = ['red','green','blue','orange','cyan']

plt.barh(df["Course"],df["Students"], color=color, edgecolor="white")
plt.title("Number of students in each course")
plt.xlabel("Students")
plt.ylabel("Course")
for i in range(len(df)):
    plt.text(df["Students"][i], i, df["Students"][i])
plt.show()
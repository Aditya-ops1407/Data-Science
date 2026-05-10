import pandas as pd
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 72, 75, 80, 200]

plt.boxplot(marks, patch_artist=True, )
plt.title("Marks Distribution")
plt.show()


# Multiple Courses

bca = [60,65,70,75,80]
bba = [50,55,60,90,95]

plt.boxplot([bca,bba], labels=["BCA","BBA"])
plt.title("Marks Distribution")
plt.xlabel("Courses")
plt.ylabel("Marks")
plt.show()
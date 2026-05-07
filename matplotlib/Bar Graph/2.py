import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 2 bar plots on same graph

plt.style.use('dark_background')

subjects = ['Maths', 'English', 'Science', 'Social Studies', 'Computer']
student1 = [89, 90, 45, 78, 99]
student2 = [78, 56, 34, 90, 12]

colours = ['red','green','blue','cyan','yellow']

subject_len = np.arange(len(subjects))
width = 0.4

plt.bar(subject_len,student1, color = colours, width= width)
plt.bar(subject_len + width,student2, color = colours, width= width, alpha = 0.5)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
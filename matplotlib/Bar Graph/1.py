import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('dark_background')

subjects = ['Maths', 'English', 'Science', 'Social Studies', 'Computer']
marks = [89, 90, 45, 78, 99]
colours = ['red','green','blue','cyan','yellow']
plt.bar(subjects,marks, color = colours, width=0.6, edgecolor = 'white', linewidth = 2 , linestyle = ':')
plt.yticks(np.arange(0,101,10))
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Use plt.barh() for horizontal bar


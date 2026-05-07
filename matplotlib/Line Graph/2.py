import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Multiple Plots on same graph

study_hours = [2,3,4,4, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12]
marks = [6, 10, 15, 20, 34, 44, 55, 60, 55, 67, 70, 80, 90, 99, 100]

plt.style.use('dark_background')

plt.plot(study_hours,marks,'y-')
plt.plot(study_hours,marks,'wo')
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()
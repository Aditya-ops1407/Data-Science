import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Multiple Plots on same graph

marks_Section_A = np.random.randint(0,101,(50))
marks_Section_B = np.random.randint(0,101,(50))

plt.style.use('dark_background')
bins = np.arange(0,101,5)

plt.hist([marks_Section_A,marks_Section_B],bins=bins, color=['yellow','white']) # You have to give list for multiple parameters in histogram
plt.xticks(np.arange(0,101,10))

plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title('Marks of Section A vs Section B')
plt.show()
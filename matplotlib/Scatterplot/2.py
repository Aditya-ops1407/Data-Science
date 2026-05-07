import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('dark_background')

roll_no = [1,2,3,4,5,6,7,8]
marks = [10,20,30,40,50,60,70,80]

# Defining plt.figure()

plt.figure(figsize=(12,8)) #Fig size defines the size of chart
plt.scatter(roll_no,marks, color = 'yellow', marker='v')
plt.xlabel("Roll no.")
plt.ylabel("Marks")
plt.show()
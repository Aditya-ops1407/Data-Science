import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('dark_background')

roll_no = [1,2,3,4,5,6,7,8]
marks = [10,20,30,40,50,60,70,80]

#Scatter takes 2 compulsory variables x and y

plt.scatter(roll_no, marks , color = 'white', marker='*')
plt.xlabel("Roll No.") #For labeling x axis
plt.ylabel("Marks") #For labeling y axis
plt.show()
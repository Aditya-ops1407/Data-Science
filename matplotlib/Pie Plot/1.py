import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('dark_background')

classes = ['Physics', 'Chemistry', 'Maths', 'Science', 'SST']
marks = [89, 45, 78, 23, 90]
colours = ['red','green','blue','turquoise','brown']
explode = [0.1,0.2,0.1,0.1,0.1]
plt.pie(marks, labels= classes, colors= colours,autopct='%0.2f%%', explode=explode) #autopct is used for showing percentages
plt.show()
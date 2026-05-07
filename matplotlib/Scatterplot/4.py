import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(os.path.join(os.getcwd(),"Scatterplot//IRIS.csv"))
print(df.head())

#Scatter plot comparing sepal length and petal length

plt.style.use('dark_background')
plt.xticks(np.arange(0,7,1))
plt.yticks(np.arange(0,7,1))
plt.scatter(df['sepal_length'], df['petal_length'],color = 'yellow', alpha=0.5)
plt.xlabel("Sepal Length")
plt.xlabel("Petal Length")
plt.show()

#Scatter plot comparing Sepal Width and Petal Width

plt.xticks(np.arange(0,7,1))
plt.yticks(np.arange(0,7,1))
plt.plot(df['sepal_width'], df['petal_width'],'wo',markersize = 10, alpha=0.5)
plt.xlabel("Sepal Width")
plt.xlabel("Petal Width")
plt.show()

#Note alpha is used for showing transparency over overlaping points 
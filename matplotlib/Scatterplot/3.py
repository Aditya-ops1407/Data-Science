import numpy as np
import matplotlib.pyplot as plt

temperature_pune = [25,34,21,45,28,6,43,18,7,2]
humidity_pune = [28, 25,29,20, 26, 50, 19, 29, 52, 55]

temperature_bangalore = [34,35,36,37,28,27,26,25,31,20]
humidity_bangalore = [40, 38, 36, 35, 42, 44, 41, 40, 34, 45]

plt.style.use('dark_background')

plt.figure(figsize=(10,10))
plt.xticks(np.arange(0,60,5))
plt.yticks(np.arange(0,60,5))
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.scatter(temperature_pune,humidity_pune,color = 'yellow', marker='o')
plt.scatter(temperature_bangalore,humidity_bangalore,color = 'blue', marker='o')
plt.show()
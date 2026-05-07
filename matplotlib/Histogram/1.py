import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('dark_background')

marks = np.random.randint(0,100,(50))
bins = np.arange(0,101,5)
plt.hist(marks, bins= bins, color = 'blue', orientation='vertical', histtype='step') # Default orientation is vertical you can change it to horizontal
plt.xticks(bins)
plt.show()
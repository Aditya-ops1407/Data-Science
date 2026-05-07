import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

roll_no = [1,2,3,4,5,6,7,8]
marks = [89,96,84,86,75,67,75,66]

plt.style.use('dark_background')

plt.plot(roll_no,marks, color = 'yellow', linestyle = '-', linewidth = 5)
plt.xlabel("Roll no")
plt.ylabel("Marks")
plt.show()

#linestyles
# 'solid' (default) '-' 
# 'dotted' ':' 
# 'dashed' '--' 
# 'dashdot' '-.' 
# 'None' '' or ' '
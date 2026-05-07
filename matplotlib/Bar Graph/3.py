import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(os.path.join(os.getcwd(),"Bar Graph//SUPERMARKET.csv"))
print(df.head())

#Generate a bar plot for payments methods of above data

payment_df = pd.DataFrame(df['Payment'].value_counts())
print(payment_df)

payment_counts = df['Payment'].value_counts()
print(payment_counts)

plt.bar(payment_counts.index, payment_counts.values, color=['red','blue','green'], width=0.7)
plt.show()
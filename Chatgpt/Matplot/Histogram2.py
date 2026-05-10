import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Age":[88,89,57,98,84,94,74,66,81,57,69,81,71,74,98,87,45,65,62,32,57]
}

df = pd.DataFrame(data)

bins = np.arange(0,101,5)
plt.style.use("dark_background")
plt.title("Age distribution")
plt.hist(df["Age"],bins=bins, color='red', edgecolor="white")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Marks":[88,89,75,98,84,94,74,66,81,57,69,81,71,74,48]
}

df = pd.DataFrame(data)

bins = np.arange(0,101,5)
plt.style.use("dark_background")
plt.title("Student Marks Distribution")
plt.hist(df["Marks"],bins=bins, color='red', histtype='step')
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
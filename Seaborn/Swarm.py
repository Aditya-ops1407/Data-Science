import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Course": [
        "BCA","BCA","BCA","BCA",
        "BBA","BBA","BBA","BBA",
        "BCom","BCom","BCom","BCom"
    ],
    
    "Marks": [
        85, 78, 92, 88,
        70, 75, 80, 72,
        65, 68, 74, 69
    ],
    
    "Gender": [
        "Male","Female","Male","Female",
        "Male","Female","Male","Female",
        "Male","Female","Male","Female"
    ]
}

df = pd.DataFrame(data)
plt.style.use("dark_background")
sns.swarmplot(x = "Course", y = "Marks", data=df, hue="Gender", palette="inferno")
plt.title("Course vs Marks")
plt.grid()
plt.show()
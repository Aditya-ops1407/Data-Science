import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Course": [
        "BCA","BCA","BCA","BCA","BCA",
        "BBA","BBA","BBA","BBA","BBA",
        "BCom","BCom","BCom","BCom","BCom"
    ],
    
    "Marks": [
        85, 88, 90, 78, 82,
        70, 72, 75, 68, 80,
        60, 65, 70, 74, 66
    ],
    
    "Gender": [
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male"
    ]
}

df = pd.DataFrame(data)
plt.style.use("dark_background")
sns.violinplot(x="Course",y="Marks",data=df, hue="Gender", palette="inferno", split=True)
plt.title("Course vs Marks")
plt.grid()
plt.show()
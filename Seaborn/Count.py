import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Course": [
        "BCA","BCA","BBA","BCom","BCA",
        "BBA","BCom","BCA","BBA","BCom",
        "BCA","BBA","BCom","BCA","BBA"
    ],
    
    "Gender": [
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male"
    ],
    
    "City": [
        "Lucknow","Delhi","Mumbai","Delhi","Lucknow",
        "Mumbai","Delhi","Lucknow","Mumbai","Delhi",
        "Lucknow","Mumbai","Delhi","Lucknow","Mumbai"
    ]
}

df = pd.DataFrame(data)

plt.style.use("dark_background")
sns.countplot(x="Course",data=df, hue="Gender", palette="inferno")
plt.show()

#Horizontal
plt.style.use("dark_background")
sns.countplot(y="Course",data=df, hue="Gender", palette="inferno")
plt.show()
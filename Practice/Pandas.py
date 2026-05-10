import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["Aditya","Rohan","Priya","Kunal","Sneha","Aryan","Neha"],
    "Course": ["BCA","BCA","BBA","BCA","BBA","BCA","BBA"],
    "Marks": [85,72,90,60,78,95,88],
    "City": ["Lucknow","Delhi","Mumbai","Delhi","Lucknow","Mumbai","Delhi"]
}

df = pd.DataFrame(data)

# Task 1
# Display first 3 rows.
print(df.head(3),"\n")

# Task 2
# Display only:
# Student
# Marks
print(df[["Student","Marks"]])

# Task 3
# Show students whose marks are greater than 80.
print(df[df["Marks"]>80],"\n")

# Task 4
# Show only BCA students.
print(df[df["Course"]=="BCA"],"\n")

# Task 5
# Find average marks of all students.
print(df["Marks"].sum()/len(df["Marks"]),"\n")
print(df["Marks"].mean())

# Task 6
# Show students from Delhi whose marks are greater than 70.
for i in range (len(df["City"])):
    if(df["City"][i]=="Delhi" and df["Marks"][i]>70):
        print(df.iloc[i])

print(df[(df["City"]=="Delhi") & (df["Marks"]>70)])

# Task 7
# Show students whose marks lie between 70 and 90.
print(df[(df["Marks"]>=70) & (df["Marks"]<=90)])

# Task 8
# Sort dataframe by Marks in descending order.
print(df.sort_values("Marks", ascending=False))

# Task 9
# Find highest marks scored.
print(df["Marks"].max())

# Task 10
# Find student having maximum marks.
print(df[df["Marks"] == df["Marks"].max()])

# Task 11
# Find average marks course-wise.

print(df.groupby("Course")["Marks"].mean())

# Task 12
# Find total marks city-wise
print(df.groupby("City")["Marks"].sum())

# Task 13
# Count number of students in each course
print(df.groupby("Course")["Student"].count())

# Task 14
# Find maximum marks city-wise.
print(df.groupby("City")["Marks"].max())

# Task 15
# Create a dataframe containing:
# Course
# Average Marks

df1 = pd.DataFrame(df.groupby("Course")["Marks"].mean())
print(df1)

# Task 16
# Create a bar graph of: Course vs Average Marks

avg = df.groupby("Course")["Marks"].mean()
plt.style.use('dark_background')
plt.bar(avg.index,avg.values , color = ['red','yellow'])
plt.xlabel("Course")
plt.ylabel("Avg. Marks")
plt.title("Average Marks by Course")
plt.show()

# Task 17
# Create a pie chart showing number of students in each city.
student_count = df.groupby("City")["Student"].count()
plt.style.use('dark_background')
plt.pie(student_count.values, labels= student_count.index , colors=['red','green','blue'], autopct="%0.2f%%", explode=[0.1,0.1,0.1])
plt.title("Students Distribution by City")
plt.show()

# Task 18
# Add New Column

df["Result"] = ["Pass" if marks >= 75 else "Fail" for marks in df["Marks"]]


# Task 19
# Create new column: Grade

df["Grade"] = [
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C"
    for marks in df["Marks"]
]
print(df)

# Task 20
# Find number of Pass students in each course.
print(df[df["Result"]=="Pass"].groupby("Course")["Result"].count())
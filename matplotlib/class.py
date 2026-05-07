import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("csv.csv")   # Make sure csv.csv is in same folder

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Remove 'cm' and 'kg' and convert to float
df['Height'] = df['Height'].str.replace('cm', '').astype(float)
df['Weight'] = df['Weight'].str.replace('kg', '').astype(float)

# Display cleaned data
print("Cleaned Data:")
print(df)

# Histogram for Height
plt.figure()
plt.hist(df['Height'], bins=5)
plt.title("Histogram of Student Heights (cm)")
plt.xlabel("Height (cm)")
plt.ylabel("Number of Students")
plt.show()

# Histogram for Weight
plt.figure()
plt.hist(df['Weight'], bins=5)
plt.title("Histogram of Student Weights (kg)")
plt.xlabel("Weight (kg)")
plt.ylabel("Number of Students")
plt.show()
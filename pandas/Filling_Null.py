import pandas as pd

df = pd.read_csv("sample.csv")
print(df.head())

print(df.isnull().sum())

#Filling null values

df2 = df.fillna(0) #Replaces all the null values with 0
print(df2)

df3 = df.fillna({'Physics':'none','Chemistry':0,'Maths':10,'Computer':20}) #Replaces null values accordingly
print(df3)

# df4 = df.fillna(method = 'ffill') # Fills with prev row value #Note this method attributes are being depricated in new pandas versions
# print(df4)

# df5 = df.fillna(method = 'ffill', axis=1) # Fills with prev coloumn value
# print(df5)

df6 = df['Physics'].fillna(value=df['Physics'].mean()) #Fills null values of Physics coloumn with it's mean
print(df6)
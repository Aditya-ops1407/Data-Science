import pandas as pd

df = pd.read_csv("sample.csv")
print(df.head())

# To check if DF contains null values
print(df.isnull())

print(df.isnull().sum()) # Gives number of null values in each coloumn

print(df.isnull().sum().sum()) # Gives total number of null values


# Dropping rows with null values

print(df.shape)
df2 = df.dropna(axis = 0) #Default axis is 0
print(df2.shape)


# Dropping coloumns with null values

print(df.shape)
df3 = df.dropna(axis = 1) 
print(df3.shape)

# dropna() attributes

df4 = df.dropna(how='any') #Drop if a row have at least one null value
df5 = df.dropna(how='all') #Drop if a all values are null in a row
print(df4)
print(df5)

# df.dropna(inplace=True) #It replaces the orignal dataframe
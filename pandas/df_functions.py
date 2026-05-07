import pandas as pd

df = pd.read_csv("csv.csv")
rest = pd.read_csv("Restaurant.csv")

print(df.columns) #Prints name of coloumns

print(df.shape) #Gives rows*coloumns

print(df.size) #gives total number of cells

print(df.head(2)) #Gives first two rows

print(df.tail(2)) #Gives last two rows

print(rest.describe()) #Gives basic mathematical stats

print(rest.info()) #Gives basic info like null values, D types


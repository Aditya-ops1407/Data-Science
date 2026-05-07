import pandas as pd

df = pd.read_csv("sample.csv")
print(df.head())

df2 = df.replace(to_replace=46, value=0)

print(df2) #Replaces all 46 with 0

df3 = df.replace(to_replace=[23,46,55,54,34], value='NA') #Replaces given list of numbers with 'NA'
print(df3)

df4 = df.replace(to_replace=[23,46,55,54,34], value=[20,50,60,50,30]) #Replaces given list of numbers with provided list of numbers
print(df4)

df5 = df.replace(to_replace=[23,46,55,54,34], value=['A','B','C','D','E']) #Replaces given list of numbers with provided list of characters
print(df5)

df6 = df['Physics'].replace(to_replace=[23,46,55,54,34], value=['A','B','C','D','E']) #Replaces given list of numbers with provided list of characters in Physics coloumn only
print(df6)
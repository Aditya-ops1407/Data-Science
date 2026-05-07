import pandas as pd

df = pd.DataFrame()
print(df)

# Data Frame using lists

lst = [1,2,3,4,5]

df = pd.DataFrame(lst)
print(df)

# Multiple coloumns

lst = [[1,2,3,4,5],[6,7,8,9,10]]
df = pd.DataFrame(lst)
print(df)

# Using dictionaries

dict = [{'a':8,'b':7,'c':9,'d':4},{'a':12,'b':23,'c':29,'d':54}] # Dictionary keys becomes coloumn names

df = pd.DataFrame(dict)
print(df)

# Using series

new_dict = {'Roll no.':pd.Series([1,2,3,4,5]),
             'Maths':pd.Series([77,88,34,89,76]),
             'Physics':pd.Series([87,98,65,88,86])}

df = pd.DataFrame(new_dict)
print(df)

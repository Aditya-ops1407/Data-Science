import pandas as pd
lst = [1,2,3,4,5]
series = pd.Series(lst) #Creates a series using list

print(series)
print(type(series))

empty = pd.Series([]) #To create empty series. Def Data type is float64

# You can also define indexes and define name of series:-

a = pd.Series(['p','q','r','s','t'], index = [10,11,12,13,14], name = "alphabets")
print(a)

# Series with dictionaries

dict_series = pd.Series({'p':1,'q':2,'r':3,'s':4,'t':5})
print(dict_series)

# print(dict_series[1]) will throw an error. Dict keys becomes indexes here

print(dict_series['q'])

print(max(dict_series)) #Returns max value of the dict series

# Now to increase number of coloumns

new_dict_series = pd.Series({'p':[1,2,3],'q':[4,5,6],'r':[7,8,9],'s':[10,11,12],'t':[13,14,15]})
print(new_dict_series)

print(new_dict_series['p']) # Returns row at key 'p'
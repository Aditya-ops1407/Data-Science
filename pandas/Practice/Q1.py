#Create Series using a list and add index and name then using dictionary

import numpy as np
import pandas as pd

#Using List

lst = [1,2,3,4,5,6]
lst_series = pd.Series(lst , index=['a','b','c','d','e','f'], name="numbers")

print(lst_series)
print(lst_series['d'])

#Using Dictionary

dict = {'a':1,'b':2,'c':3,'d':4}
dict_series = pd.Series(dict)
print(dict_series['b'])

new_dict_series = pd.Series({'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]})
print(new_dict_series['a'])
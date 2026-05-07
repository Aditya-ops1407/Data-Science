import pandas as pd

df1 = pd.DataFrame({'Roll no.':[1,2,3,4,5],
                    'Maths':[78,55,69,67,84],
                    'Physics':[78,58,92,85,78]})

df2 = pd.DataFrame({'Roll no.':[6,7,8,9],
                    'Maths':[78,55,69,67,],
                    'Physics':[78,58,92,85,]})

df3 = pd.concat([df1, df2], ignore_index=True) #Adds df2 to df1 while ignoring the indexes
print(df3)
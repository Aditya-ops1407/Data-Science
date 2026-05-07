import pandas as pd

df = pd.DataFrame({"Roll no.":[1,2,3,4,5],
                   "Physics":[88,76,91,87,71]})

df1 = pd.DataFrame({"Roll no.":[1,2,3,4,5],
                    "Chemistry":[78,87,92,78,37]})

df_merged = pd.merge(df, df1, on='Roll no.') #Merges df and df1 into single dataframe according corresponding roll no.
print(df_merged)

#If we don't provide on= then by default intersecting coloumns are taken

df2 = pd.DataFrame({'Roll no.':[1,2,3,4,5],
                    "Physics":[88,76,91,87,71]})

df3 = pd.DataFrame({'Roll no.':[1,2,3,6,7],
                    "Chemistry":[78,87,92,78,37]})

merge = pd.merge(df2, df3, on='Roll no.') #Only common role numbers are merged
print(merge)

print(pd.merge(df2, df3, how='left')) #Only roll numbers present in df2 are merged

print(pd.merge(df2, df3, how='right')) #Only roll numbers present in df3 are merged

print(pd.merge(df2, df3, how='outer')) #All roll numbers are merged


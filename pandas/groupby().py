import pandas as pd
import os


df = pd.read_csv(os.path.join(os.getcwd(),"pandas\sample2.csv"))
print(df.head())

branch_group = df.groupby(by='Branch') #Groups data according to Branch coloumn

print(branch_group)
print(branch_group.groups)

new_group = df.groupby(by=['Branch','Section'])#Groups data according to Branch and Section coloumn
print(new_group.groups)

for group, data_frame in new_group: #Using for loop 
    print(group)
    print(data_frame)
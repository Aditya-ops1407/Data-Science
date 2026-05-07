import pandas as pd

df = pd.read_csv("sample2.csv", index_col=['Roll No.']) #Index_col attribute makes the provided coloumn as index for df
print(df.head())

# loc() Location as per defined index, # iloc() Location as per default index

print(df.loc[1]) #Provides details for Roll No.1
print(df.iloc[0]) #Provides details for Roll No.1

print(df.loc[[2,3,4,5]]) #Provides details for Roll No. 2,3,4 and 5 # Note that you have to provide list of list
print(df.iloc[[1,2,3,4]]) #Same thing using iloc

print(df.loc[[1,2,3,4,5],'Physics']) #Provides details of physics coloumn for Roll No. 1,2,3,4 and 5

print(df.loc[1:20:2,'Physics']) #Same thing using range of numbers giving only odd roll numbers

print(df.loc[df['Physics']<50]) # Gives all roll numbers whose marks are less than 50 in physics

print(df.loc[df['Physics']<50,['Maths']]) # Gives only maths marks of all those students whose marks are less than 50 in physics

print(df.iloc[:,0]) #Gives all the rows and first coloumn

print(df.iloc[0:5,1]) #Returns rows from index 0 to 4 and coloumn at index 1 #Roll 1 to 5 and Branch
print(df.iloc[0:5,1:4]) #Returns rows from index 0 to 4 and coloumns from index 1 to 3 #Roll 1 to 5 and Branch,Physics and Chemistry




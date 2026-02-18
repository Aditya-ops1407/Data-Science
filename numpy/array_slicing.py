import numpy as np

a = np.arange(1,51)
a = a.reshape((10,5))


#Indexing in Arrays

print(a[0]) #Prints first row

print(a[0,0]) #Prints first element of first row
print(a[3,4]) #Prints 5th element of 4th row

print(a[0:3]) #Prints all rows from first to third index
print(a[0:10:2]) #Prints all odd rows.

print(a[0:3,1]) #Prints all elements at index 1 from first to third row
print(a[1:10:2,::2]) #Prints all even indexes of even rows

# You can also check dtype of coloumns

print(a[:, 2:5].dtype)
import numpy as np

print("1D Array")
a = np.array([1,2,3,4])
print(a,"\n")

print("2D Array")
b = np.array([[1,2,3,4],[5,6,7,8]])
print(b,"\n")

print("3D Array")
c = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(c,"\n")

print(type(a),type(b),type(c))

print(b.size) #Number of elements in b

print(c.shape) #Rows and Coloumns

print(a.dtype) #Gives data type

print(b.transpose()) #Interchanges rows and coloumns. i.e. 2*4 -> 4*2


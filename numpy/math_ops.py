import numpy as np


a = np.arange(0,18).reshape(6,3)
b = np.arange(20,38).reshape(6,3)

print(a)
print(b)

print(a+b) #Elements with identical indexes are added
print(np.add(a,b)) #The same thing using function

print(a-b) #Elements with identical indexes are subtracted
print(np.subtract(a,b)) #The same thing using function

print(a*b) #Elements with identical indexes are multiplied. Note this is simple multiplication not matrix multiplication
print(np.multiply(a,b)) #The same thing using function

print(a/b) #Elements with identical indexes are divided. Note this is simple division not matrix division
print(np.divide(a,b)) #The same thing using function

# To perform matrix multiplication coloumn number of first matrix and row number of second matrix should be identical
b = b.reshape(3,6) #Now a(6*3) and b(3*6) so a@b = (6*6)
print(a@b)
print(a.dot(b)) #Same thing using function

print(b.max()) #Returns element with max value
print(b.argmax()) #Returns index of element with max value

print(b.min()) #Returns element with min value
print(b.argmin()) #Returns index of element with min value

print(np.sum(a)) #Returns sum of all elements of a

print(np.sum(a, axis = 0)) #Returns sum of all elements of each column of a

print(np.sum(a, axis = 1)) #Returns sum of all elements of each row of a

print(np.mean(a)) # Returns mean of all elements of a

print(np.sqrt(a)) # Returns sq roots of each elements of a


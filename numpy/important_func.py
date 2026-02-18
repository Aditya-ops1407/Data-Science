import numpy as np

a = np.arange(1,21) #It behaves just like range function but gives output as list
print(a)

a = a.reshape((4,5)) #Reshape 1*20 to 4*5
print(a)

b = np.arange(1,100,2)
print(b)

b = b.reshape((10,5))
print(b)

b = b.flatten() #It is just inverse funtion of reshape. Turns it back to single row array. It doesn't affect orignal array
print(b)

b = b.ravel() #Same as flatten but modifies orignal array
print(b)


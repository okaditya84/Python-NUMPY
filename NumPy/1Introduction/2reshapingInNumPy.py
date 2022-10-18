#from course https://www.educative.io/courses/from-python-to-numpy/JEOAM8onYkv
import numpy as np

#To reshape an array: Z=(any np array).reshape(x_dimension,y_dimension), x=rows, y=columns
#example: reshape a 1D array of 24 elements into a 6x4 matrix
Z = np.arange(24).reshape(6,4) #here np.arange(10) will create a 1D array of 24 elements, then it reshaped to 6x4 matrix
print(Z)
#Reshaping the same to 8x3 matrix
R = Z.reshape(8,3)
print(R)
#Z.reshape(x,y) do not mutate the Z, instead returns new NumPy Object
#NOTE: x_dimension*y_dimension must be equal to the number of elements in the np array

# E = R.reshape(3,4) : will throw an error as 3*4 != 24
# ValueError: cannot reshape array of size 24 into shape (3,4)
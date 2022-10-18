# from course https://www.educative.io/courses/from-python-to-numpy/39q42AmPVq4

import numpy as np

SIZE = 9
Z = np.zeros(SIZE) # create a 1D array of zeros
print(Z)        # [0. 0. 0. 0. 0. 0. 0. 0. 0.]
print(Z.shape)  # Will return cardinality of the array in form of a tuple
print(Z.size)   # Will return number of elements in the array i.e. multiplication of all elements in cardinality
print(type(Z))  # Will return numpy.ndarray

O = np.ones(SIZE) # create a 1D array of ones
print(O)        # [1. 1. 1. 1. 1. 1. 1. 1. 1.]

#To create np array from a list use np.array(list)
L = [1,2,4,5,6,7,9]
A = np.array(L)
print(A)        # [1 2 3 4 5 6 7 8 9]

#If we multiply a list by a number, it will repeat the list that many times, but the np array will multiply each element by that number
print(L*2)      # [1, 2, 4, 5, 6, 7, 9, 1, 2, 4, 5, 6, 7, 9]
print(A*2)      # [ 2 4 8 10 12 14 18]

#create a np array of any SIZE
S = np.arange(SIZE) #S = np. array from 0 to SIZE-1
print(S)        # [0 1 2 3 4 5 6 7 8]

#create a np array of any SIZE with a start, stop and step
#it will be somewhat similar to range(start, stop, step), will include values till stop-1
R = np.arange(1,SIZE,2) #S = np. array from 1 to SIZE-1 with step 2
print(R)

#Reshape a NumPy Array into a Column Vector
C = np.arange(1,SIZE).reshape(SIZE-1,1) #reshape takes two arguments, number of rows and number of columns
#1 column and SIZE-1 rows == column vector
print(C) #in short it is a 2D array with SIZE-1(no. of rows) elements and each element contains a list of 1(no. of columns) element

#Generate Array of Random Numbers and in Grid Format
#np.random.rand() will generate random numbers between 0 and 1
#np.random.randint(x, y, shape) will generate random integers between the given range (x,y) and in the given shape(tuple(rows, columns))
B = np.random.randint(1,10,(3,3))
print(B)
C = np.random.rand(3,4)
print(C)

#Create a Linspace
#To create evenly spaced numbers over a specified interval write np.linspace(start, stop, num)
L = np.linspace(1,10,7) # Will add 7 evenly spaced numbers between 1 and 10
"""
a = 1, n=7, an = 10
10 = 1 + (7-1)*d
d = (10-1)/(7-1)
d = 9/6 = 1.5
L = [1, 2.5, 4, 5.5, 7, 8.5, 10]
"""
print(L)
#Create a Mesh Grid#
#To create a dense multi-dimensional “meshgrid”. ,write: np.mgrid[0:x_dimension, 0:y_dimension]
M = np.mgrid[0:3, 0:3]
print(M) # array containing two elements, each element containing a matrix with value either row number or column number
"""
[[[0 0 0]
  [1 1 1]
  [2 2 2]]

 [[0 1 2]
  [0 1 2]
  [0 1 2]]]
"""

#null vector of size n = np.zeros(n)
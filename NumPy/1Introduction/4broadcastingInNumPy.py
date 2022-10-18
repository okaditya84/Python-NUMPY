#from course: https://www.educative.io/courses/from-python-to-numpy/7nDQvG1YXXr
import numpy as np
""" 
    The term broadcasting describes how numpy handles arrays of different shapes during arithmetic operations.
    Under certain restrictions, smaller arrays are "broadcast" to larger arrays so they are shape compatible.
    Broadcasting provides a means of vectorizing array operations.

    When working with two arrays, NumPy compares their shapes element by element.
    It starts with the subsequent dimension and works forward. Two dimensions of size N are compatible if:

    they are equal, or
    one of them is 1x1
    one is NxN and other is Nx1
    one is NxN and other is 1xN
"""

#When one operand is NxN and other is 1x1
Z1 = np.arange(9).reshape(3,3)
Z2 = 1 
print("Z1\n",Z1)
print("Z2\n",Z2)
print("Z1+Z2\n", Z1 + Z2)
#Hence Z2 is broadcasted to Z1, after broadcasting it is a 3x3 array with all elements as 1
Z3 = np.array([1,2])
# print("Z1+Z3\n", Z1 + Z3) Will throw error as we cant broadcast 1x2 to 3x3
#we can only broadcast 1x1 to nxn, 1xn to nxn, nx1 to nxn
#We can broadcast 1x1 to any shape

Z2 = np.arange(3)[::-1].reshape(3,1)
print("Z2\n", Z2)
print("Z1+Z2\n", Z1 + Z2)

#When one operand is NxN and other is Nx1
Z1 = np.arange(9).reshape(3,3)
Z2 = np.arange(3)[::-1].reshape(3,1)
print(Z1 + Z2)

#When one operand is NxN and other is 1xN
Z1 = np.arange(9).reshape(3,3)
Z2 = np.arange(3)[::-1]
print(Z1 + Z2)
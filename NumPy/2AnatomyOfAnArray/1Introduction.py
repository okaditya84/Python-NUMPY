#from course: https://www.educative.io/courses/from-python-to-numpy/B1JRzK0zVrN
import numpy as np
Z = np.ones(4*1000000, np.float32) #create an array of ones of size 4 *1000000 with float32 as datatype
print(Z)
# Z[...] = x will set all elements of Z to x
Z[...] = 0 #clear the array,sets every value to 0
print(Z)
print(Z.dtype)#prints the datatype of Z

#casting the array into a larger data type such as np.float64, can gain 25% speed factor.
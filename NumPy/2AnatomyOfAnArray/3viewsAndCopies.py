#from course: https://www.educative.io/courses/from-python-to-numpy/x1WGzzwZ3GP
import numpy as np

#Direct and indirect access
"""
A copy of the input array is made or a view is provided during the execution of the numpy statement.
When content is physically stored in another location, this is called a copy.
On the other hand, when it provides another view of the same memory contents, it is called a view.
"""

#Indexing and Fancy Indexing
Z = np.zeros(9)
Z_view = Z[:3]
Z_view[...] = 1 #Z_view modifies the base array 'Z'
# When we assign a new variable sliced numpy array, it doesn't create a new copy, instead refer to the original ones
print(Z)
Z = np.zeros(9)
Z_copy = Z[[0,1,2]]
Z_copy[...] = 1 #Z_copy does not modify the base array 'Z'
# When we assign a new variable an array through indexing, a new block of memory would be created and any change to that will not make any change to original array
print(Z)

# It is better to work on copy of the array
Z = np.zeros(9)
index = [0,1,2]
Z_copy = Z[index]
Z_copy[...] = 1
print(Z)
print(Z_copy)

"""
If you are unsure that the result of your indexing is a view or a copy, you can check the base of your result.
If it is of type None, then your result is a copy:
"""
Z = np.random.uniform(0,1,(5,5)) #draws sample from a uniform distribution
Z1 = Z[:3,:]
Z2 = Z[[0,1,2], :]
print(np.allclose(Z1,Z2)) #returns True if two arrays are element-wise equal within a tolerance.
print(Z1.base is Z)#return true if memory of Z1 is shared with Z and false otherwise
print(Z2.base is Z)#return true if memory of Z2 is shared with Z and false otherwise
print(Z2.base is None) #return true if memory of Z2 is not shared

# ravel: https://numpy.org/doc/stable/reference/generated/numpy.ravel.html
# ravel converts any multi-dimensional array to 1D array

R = np.random.randint(0, 10, 9).reshape(3,3)
print(R)
print(R.ravel()) # will return copy of the array instead of mutating it

#flatten: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten
#Flatten always returns a copy of the input array, flattened to one dimension.

#np.byte_bounds(np.array)[0] will return a pointer to the starting index of an array and np.byte_bounds(np.array)[-1] will  return pointer to end
Z = np.random.randint(0,10,9).reshape(3,3)
print(np.byte_bounds(Z)[0], np.byte_bounds(Z)[-1])
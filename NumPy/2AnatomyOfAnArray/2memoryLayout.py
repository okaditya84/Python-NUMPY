#from course: https://www.educative.io/courses/from-python-to-numpy/q2NogpVJKWy
import numpy as np
#Memory layout

S = np.random.randint(0, 10, 9, dtype=np.int16).reshape(3,3)
print(S)
print(S.itemsize)  # returns size of S in bytes
print(S.shape)  # returns the x dimension and y dimension of S
print(S.ndim)  # dimension in S i.e (2 in this case) since the array is 2D


"""
Imagine an array of 32-bit integers (each 4 bytes):
x = np.array([[0, 1, 2, 3, 4],
              [5, 6, 7, 8, 9]], dtype=np.int32)
This array is stored in memory as 40 bytes, one after the other (known as a contiguous block of memory).
The strides of an array tell us how many bytes we have to skip in memory to move to the next position along a certain axis.
For example, we have to skip 4 bytes (1 value) to move to the next column, but 20 bytes (5 values) to get to the same position in the next row.
As such, the strides for the array x will be (20, 4).

from: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.strides.html#numpy.ndarray.strides
"""

y = np.reshape(np.arange(2*3*4), (2,3,4))
print(y)
print(y.strides)     #96, 32, 8 ==> need 8 byte jump to go to next element, 32 bytes to go to next row and 64 bytes to go to next column
print(y[1,1,1])
offset = sum(y.strides * np.array((1,1,1)))
print(offset/y.itemsize)


"""
numpy.ndarray.tobytes

ndarray.tobytes(order="C")

Construct Python bytes containing the raw data bytes in the array.
Constructs Python bytes showing a copy of the raw contents of data memory.
The bytes object is produced in C-order by default.
This behavior is controlled by the order parameter.

Parameters
order{"C", "F", "A"}, optional
Controls the memory layout of the bytes object. "C" means C-order, "F" means F-order, "A" (short for Any) means "F" if a is Fortran contiguous, "C" otherwise. Default is "C".

from: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html
"""

x = np.array([[0, 1], [2, 3]], dtype='<u2')
print(x.tobytes())  #default parameter is "C"
print(x.tobytes('F'))

#Item layout
Z = np.arange(9).reshape(3,3)
V= Z[::2,::2]       #V will have corner element of Z
print(Z)
print(V)

L = np.arange(9)        #[0 1 2 3 4 5 6 7 8]
print(L)
L = L.reshape(3,3).astype(np.int16)     #[[0 1 2], [3 4 5], [6 7 8]]
V = L[::2,::2]      #[[0 2]. [6,8]]
V=V.reshape(1,4)    #[0 2 6 8]
print(V)
#from course : https://www.educative.io/courses/from-python-to-numpy/gxzy8y5Zr5r
import numpy as np

#Indexing means to refer to any value in an array. Each item in a numpy array is stored at a specific index.
#It is similar to accessing an element in a list. The index of the first element is 0, the second element is 1, and so on.

Z = np.random.randint(0,10,9)
print(Z)
print("Element at index 0 is:", Z[0])

R = Z.reshape(3,3)
print(R)
#Get an element from a Grid (rowIndex, columnIndex)
print("Element at rowIndex 2 and columnIndex 1 is:", R[2,1]) #Will access the element at row index 2 and column index 1

#We can also access the elements of a numpy array using negative indexing.
print("The Element from Last is:", R[-1,-1]) #Will access the last element

#Get a row from a Grid
print("Row at index 1 is:", R[1]) #Will access the Index 1 row
#Get a Column from a Grid
print("Column at index 1 is:", R[:,1]) #Will access the Index 1 column

#Get a Mini-grid from a Grid
#To get a subset of a grid, write: R[row_index:,column_index:]
print(R[1:,1:]) #Will access a mini grid from rowIndex 1 to end and columnIndex 1 to end

bigGrid = np.random.randint(0, 100, 25).reshape(5,5)
print("bigGrid\n",bigGrid)
print("3x3 mini grid of bigGrid is:")
print(bigGrid[1:4,1:4]) #The Ending index is not included   

#We can add step value here as well
veryBigGrid = np.random.randint(0, 100, 49).reshape(7,7)
print("veryBigGrid\n",veryBigGrid)
print("3x3 mini grid of veryBigGrid is:")
print(veryBigGrid[1:7:2,1:7:2]) #The Ending index is not included

#Arrange Values from a Grid in a Mini-grid
#To get the values from corners of a grid and arrange them in a grid format write: R[::row_size-1,::column_size-1]
print("Corners of bigGrid are:")
print(bigGrid[::4,::4]) #Will access the corners of bigGrid

#getting values at specific index of grid
print("Values at specific index of bigGrid are:")
print(bigGrid[(1,1), (3,4)]) #Will access the values at specific index of bigGrid
print("Type of returned elements of specific index: ",type(bigGrid[(1,1), (3,4)])) #showing that return value will be numpy array
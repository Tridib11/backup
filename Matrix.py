from numpy import *
import numpy as np

# arr1 = array([
#     [1, 2, 3, 6, 2, 9],
#     [4, 5, 6, 7, 5, 3]
# ])
# print(arr1.dtype)  # to check the type of data working with
# print(arr1.ndim)  # to check the number of dimensions we are working on
# print(arr1.shape)  # gives a tuple with number of rows and number of columns
# print(arr1.size)  # size of the entire block
# """Convert any dimensional array to 1D array"""
# arr2 = arr1.flatten()
# print(arr2)
# """Convert any dimensional array to 1D/2D/3D(any) """
# # arr3 = arr2.reshape(3, 4)  # (rows,columns)
# # arr3 = arr2.reshape(2,2,3)  # (2 2D array with 3 coloumns)
#
# """Convert the array to a matrix"""
# m = matrix(arr1)  # or matrix('1 2 3 4;5 6 7 8') 2 rows 4 coloumns
#
# """Diagonal elements"""
#
# print(diagonal(m))
#
# """Minimum elements"""
#
# print(m.min())
#
# """Maximum"""
#
# print(m.max())

"""Multiple two matrices"""

m1 = matrix('1 2;3 4;5 6')
m2 = matrix('7 8;9 1;1 2')
print(m1)
print(m2)
# m3 = m1 + m2 #There is an issue u can add like this but cant multiple like this print(np.multiply(m1,m2))# to do
# multiple either u need to change the way u took the array or u can use the multiply function
# m4 = m1 * m2 This doesnot work using this type of matrix declaration use np.multuply(m1,m2)
print(np.multiply(m1,m2))


"""But works in trandional way"""
arr1 = array([
    [1, 2, 3, 6, 2, 9],
    [4, 5, 6, 7, 5, 3]
])
arr2 = array([
    [1, 2, 3, 6, 2, 9],
    [4, 5, 6, 7, 5, 3]
])
m4=arr1*arr2
# print("Addition")
# print(m3)
print("Multiplication")
print(m4)

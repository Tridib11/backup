# """Used for multidimensional arrays"""
from numpy import *

#
# # arr=array('i',[1, 2, 3, 4, 5, 6]) doesn't works  the type mentioning is optional
# if u really want to put some type then use arr = array([1, 2, 3, 4, 5, 6.0],int)
#
# arr = array([1, 2, 3, 4, 5, 6])  # while using numpy we don't need to mention the type of the array
# print(arr)

"""Different ways of creating array in numpy"""
# arr = array([1, 2, 3, 4, 5, 6.0],int)
# print(arr.dtype)  # to check the type
# arr = linspace(0, 15,16)
# number 0 to 15 divided into 16 parts  (start,end,parts)  if u don't mention the part then it will
# automatically divide the number into 50 parts the default is 50
# arr=arrange(1,15,2)  #1 to 15 2 steps
# arr = logspace(1, 40, 5)
# arr = zeros(5, int)  # all the number are zeroes in array
# print(arr)

"""Copy in python"""
arr1 = array([2, 4, 6, 7, 8])
arr2 = array([1, 9, 0, 19])
# arr1=arr2
"""TO change the address in the heap memory"""
arr2 = arr1.view()
print(arr1)
print(arr2)

"""To check the id or the location u can use"""
print(id(arr1))
print(id(arr2))
"""2913747825552
2913747825552"""  # It has the same address
print(arr2)

"""Shallow copy"""
# Suppose u have two arrays and u make them point to eachother then
# arr1=arr2 #then if u change one array it will automatically reflect int the array pointing to it


"""Deep copy"""
# Suppose u have two arrays and u make them point to each-other then
# arr1=arr2 then if u change one array it won't reflect the array pointing to it
# we have an array1 and array2 to make them point to each-other we use
# array1=[3,3,4,0,5,5]
# array2=array1.copy()
# any change done in the array1 won't be reflected to array2 and the address will also not be the same

# import array as arr
from array import *

vals = array('i', [5, 9, 8, 4, 2])
# vals=array('u',['a','e','i']) #for character
# print(vals)
print(vals.buffer_info())  # size of the array
print(vals.typecode)  # says the type of array
# vals.reverse()
print(vals[0]);

# newArr=array(vals.typecode,(a for a in vals)) #use typecode if u dont know the type of array
newArr = array(vals.typecode, (a * a for a in vals))  # square of it
for i in newArr:
    print(i, end=",")

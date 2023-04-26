"""Lambda=function written in 1 line using lambda keyword accepts any 
number of arguments but only has one expression 
(think of it as a shortcut)(usefull if needed for a short period of tim,throw away)"""

# #lambda parameters:expression
#
# # double=lambda x:x*2
# # print(double(5))
# # multiply=lambda x,y:x*y
# # add=lambda x,y,z:x+y+z
# # full_name= lambda first_name,last_name:first_name+" "+last_name
# age_check=lambda age:True if age>=18 else False
# print(age_check(12))

"""Normal Function"""
# def square(a):
#     return a * a
# result = square(5)
# print(result)

"""Lambda Function"""

f = lambda a: a * a  # a,b:a+b it has to be of one expression
result = f(5)
print(result)

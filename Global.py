
"""Changing th global variable"""
# a=10
# def something():
#     global a
#     a=15
#     print("in fun",a)
#     a=9
# something()
# print("Outside",a)

"""Using the global and local variable at the sametime"""
a=10
b=8
c=9
print(id(a))
def something():
    a=9
    # x = globals()  it will return al the global variables
    x=globals()['a']
    print(id(x))
    print("in fun",a)

    """to change the global variable"""
    globals()['a']=15
something()
print("Outside",a)
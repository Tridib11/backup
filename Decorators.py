# def check(func):
#     def inside(a, b):
#         if b == 0:
#             print("Cant divide")
#             return
#         func(a, b)
#
#     return inside
#
#
# @check
# def myfunc(a, b):
#     return a / b
#
#
# print(myfunc(5, 0))


def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
# div1=smart_div(div)

@smart_div
def div(a,b):
    print(a/b)
div(2,4)
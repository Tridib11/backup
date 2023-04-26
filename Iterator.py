# users=['efef','wwdwd','wddddd','fffff']
# # for user in users:
# #     print(user)
# """To do this without loop we will be using
# iterator"""
#
# looper=iter(users)
# while True:
#     try:
#         user=next(looper)
#         print(user)
#     except StopIteration:
#         break


"""Creating own iterator"""
class Topten:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values=Topten()
for i in values:
    print(i)
# print(values.__next__())
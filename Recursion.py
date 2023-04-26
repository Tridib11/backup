import sys

sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())
i = 0


def greet():
    global i
    i += 1
    print("Hello", i)
    greet()


greet()

####Limit of recursion is 1000

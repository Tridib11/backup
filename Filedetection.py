import os
path="D:\\VScode\\Python\\dircheck"
# path="D:\\VScode\\Python\\test.txt"
# # if os.path.exists(path):

#     print("Yea it exits")
# else:
#     print("Its removed")

if os.path.isfile(path):
    print("It is a file")
elif os.path.isdir(path):
    print("It is a directory")
else:
    print("It is not a file")
from array import *

arr = array("i", [])
n = int(input("Enter the length of the array"))
for i in range(n):
    x = int(input(f"Enter the value {i + 1}"))
    arr.append(x)
print(arr)

val = int(input("Enter the value to search for"))
k = 0
for i in arr:
    if i == val:
        print(f"Element found at {k}")
        break
    k += 1
else:
    print("Not found")

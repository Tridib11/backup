def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


lst = [20, 25, 3, 5, 62, 2, 7, 90, 1]
even, odd = count(lst)
print(even)
print(odd)
print("Even number's : {}, Odd number's :{} ".format(even,odd))

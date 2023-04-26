# def iseven(n):
#     return n%2==0

nums = [3, 2, 4, 5, 56, 7, 8, 9]
# evens=list(filter(iseven,nums))  #(function,iterable)
evens = list(filter(lambda n: n % 2 == 0, nums))  # using lambda
print(evens)

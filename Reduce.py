from functools import reduce

import doubles as doubles

nums = [3, 2, 4, 5, 56, 7, 8, 9]
print("The list",nums)
evens = list(filter(lambda n: n % 2 == 0, nums))  # using lambda
print("All the even numbers in the list",evens)
# whenever u want to change any value, we use a map
#doubling the number
doubles=list(map(lambda a:a*2,evens))  #(function,iterable)
print("Doubling the even numbers in the list")
print(doubles)


#to add all everything we use the reduce function like to perform operations
sum=reduce(lambda a,b:a+b,doubles)
print("The reduced thing after adding all the doubled values is",sum)
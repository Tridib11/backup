# fruits=["apple","mango","grapes"]
# fruits.extend(["oranges","grapes"])
# c=fruits.count("grapes")

# print(c)

# fruits.sort()
# for i in fruits:    
#     print(i)

# if "grapes">"apple":
#     print("True")    
# else:
#     print("False")

# a="grapes"
# print(ord(a))


# append() - adds an element to the end of the list.
# extend() - adds the elements of another list to the end of the list.
# insert() - inserts an element at a specific index in the list.
# remove() - removes the first occurrence of an element from the list.
# pop() - removes and returns the element at a specific index in the list.
# index() - returns the index of the first occurrence of an element in the list.
# count() - returns the number of times an element appears in the list.
# sort() - sorts the elements in the list in ascending order.
# reverse() - reverses the order of the elements in the list.
# copy() - returns a copy of the list.
# clear() - removes all the elements from the list.



food=["pizza","hamburger","hotdog"]
food[0]="sushi"
# food.append("ice cream")
# food.remove("hotdog")
#food.pop(0) #if nothing is given inside the bracket it will remove from the back
# food.insert(0,"Cake")
# food.sort()
food.clear()

for x in food:
    print(x)

##lists are orderd and changable
## collection which is unordered,unindexed.No 
# duplicate values

utensils = {"fork", "spoon", "knife"}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.discard("fork") #its similarly like remove but if it doesnot find
# anything like "fork" it wont raise an error but remove would

# utensils.pop()  #pops a random value

dishes = {"bowl", "plate", "cup", "spoon"}
# utensils.update(dishes)  #combines 1st set with second set permanently

diner_table = utensils.union(dishes)  # combines two set

# for x in diner_table:
#     print(x)

# print(utensils.difference(dishes))# its like utensils-dishes
print(utensils.intersection(dishes))  ##prints the common in two sets

print(utensils.isdisjoint(dishes))  ##prints true if their is no common in both the sets
print(utensils.issuperset(dishes))  # it means that does the content of utensils are their in dishes

"""to delete the set"""
# del utensils

"""
The difference between the 
two methods is that while union() 
creates and returns a new set containing all distinct
 elements present in all
 the iterables 
passed as arguments, update() updates the set on which
 it is called with all distinct elements present in all
 the iterables passed as arguments1.

a set and a dictionary is written the same way so
in {} so to make an empty set we cant write as
tridib={} it will become a dictionary
to make an empty set we need to write tridib=set()

when a set is printed it will not be in ordered
"""

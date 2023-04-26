
## Achangeabe ,unorderd collection of unique key:value
#pairs Fast beacuse they use hashing, allows us to access
# a value quickly


dict={
    "ram":"Good",
    "rohan":"bad",
    "sally":"worst"
}
# dict["rohit"]="better"  #old way

#dict.update({"rohit":"OKOK"}) #new way used to add new and update old one
# dict.pop("ram")  ##to remove

dict.clear()
# print(dict)
# print(dict["rohan"]) ##old way
print(dict.get("kiwi")) #new way
print(dict.keys())
print(dict.values())
print(dict.items())   #displays everything
#wipe an existing dictionary
#dict={}
for key,value in dict.items():
    print(key,value)
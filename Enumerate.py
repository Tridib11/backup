"""the enumerate function is a built in function in python
that allows you to loop over a sequence (such as list,tuple,string)
and get the index and value of each element in the sequence at the same 
time """



marks=[12,56,32,98,12,45,1,4]
for index,mark in enumerate(marks): #u can also specify the 
#for index,mark in enumerate(marks,start=1) it starts with 0 index but now it will 
# start with so the ist index is not 1 not 0
    print(mark)
    if(index==3):
        print("Tridib,awesome")




try:
    with open("D:\\VScode\\Python\\copy.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")
# print(file.closed)


#using with open will automatically 
# close the file for u ,,u can check it using
#file.closed

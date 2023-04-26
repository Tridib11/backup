""" The shutil module offers a number of high-level
 operations on files and collections of files. In particular, functions are provided
 which support file copying and removal. For operations on individual files, 
 see also the os module. """

"""The OS module in Python provides 
functions for creating and removing a 
directory (folder), fetching its contents,
 changing and identifying the current directory, etc. 
 You first need to import the os module to interact 
with the underlying operating system."""

import os
import shutil
source="D:\\VScode\\Python\\test.txt"
destination="C:\\Users\\tridi\\OneDrive\\Documents\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file named this")
    else:
        shutil.move(source,destination)
        print(source+"was moved")
except FileNotFoundError:
    print(source+"File not found")
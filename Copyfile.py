#copyfile() = copies contents of a file
#copy() = copyfile()+permission mode + destination can be a directory
#copy2() = copy()+copies metadata(file's creation and modification times)

import shutil
shutil.copyfile("D:\\VScode\\Python\\test.txt","D:\\VScode\\Python\\copy.txt") #src,dat



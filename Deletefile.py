import os
import shutil
# path_file="D:\\VScode\\Python\\test.txt"
path_folder="D:\\VScode\\Python\\dircheck"
try:
    # os.remove(path_file) ##this function doesnot remove folder  its for filr
    # os.rmdir(path_folder)#is for folder but wont delete folder containing files
    shutil.rmtree(path_folder)#used to remove folder containing files
    

except FileNotFoundError:
    print("No file found")
except PermissionError:#used when it is a folder insetad of a file
    print("You donot have permission to delete that")
except OSError: #used when folder not empty
    print("Folder not empty")

else:
    print(path_folder+"was deleted")

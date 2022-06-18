import os
import shutil

path = ".\\files_managment\\empty_folder"

try:
    os.remove(path)  #removes files 
    os.rmdir(path)  #removes empty directories
    shutil.rmtree(path)  #removes directories conteining files
except FileNotFoundError:
    print("The file has not been found.")
except PermissionError:
    print("You do not have permission to remove that")

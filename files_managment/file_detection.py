import os

path = "C:\\Users\\Josue\\Documents\\folder"

if os.path.exists(path):
    print("This location exists")
    if os.path.isfile(path):
        print("And it is a file")
    elif os.path.isdir(path):
        print("It is a directory")
else:
    print("This location doesn't exist")

import os

src = ".\\files_managment\\test2.txt"
dst = "C:\\Users\\Josue\\Documents\\Coding\\test2.txt"

try:
    if os.path.exists(dst):
        print("There is already a file there.")
    else:
        os.replace(src,dst)
        print(src + " was moved")
except FileNotFoundError as e:
    print("The file", src, "has not been found")

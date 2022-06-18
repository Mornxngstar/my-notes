try:
    with open(".\\files_managment\\test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("The file was not found.")
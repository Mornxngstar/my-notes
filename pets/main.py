from os import system
import os
#---------------------------------------------------
class Pets:
    def __init__(self, animal, name, age, color, gender):
        self.animal = animal
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender
#---------------------------------------------------
def packing_data():
    animal = ""
    while animal == "":
        system("cls")
        print("Enter the data as it is requested.\n")
        animal = input("Animal: ")

    name = ""
    while name == "":
        system("cls")
        print("Enter the data as it is requested.\n")
        name = input("Name: ")

    age = ""
    while age == "":
        system("cls")
        print("Enter the data as it is requested.\n")
        age = input("Age: ")

    color = ""
    while color == "":
        system("cls")
        print("Enter the data as it is requested.\n")
        color = input("Color: ")

    gender = ""
    while gender == "":
        system("cls")
        print("Enter the data as it is requested.\n")
        gender = input("Gender: ")

    pet = Pets(animal, name, age, color, gender)
    write(pet)
#---------------------------------------------------
def write(pet):
    with open(".\\pets\\names.txt", 'a') as f:
        f.write(pet.name+"\n")
        f.close()
    with open(".\\pets\\{0}.txt".format(pet.name), 'w') as f:
        f.write("Animal: ")
        f.write(pet.animal)
        f.write("\n")
        f.write("Name: ")
        f.write(pet.name)
        f.write("\n")
        f.write("Age: ")
        f.write(pet.age)
        f.write("\n")
        f.write("Color: ")
        f.write(pet.color)
        f.write("\n")
        f.write("Gender: ")
        f.write(pet.gender)
        f.write("\n")
        f.close()
#---------------------------------------------------
def read():
    system("cls")
    with open(".\\pets\\names.txt", 'r') as f:
        choice = input("Which file do you want to open?\n\n"+f.read()+"\nWrite your pet's name: ")
        try:
            system("cls")
            with open(".\\pets\\{}.txt".format(choice), 'r') as file:
                slct = input(file.read())
                
        except FileNotFoundError:
            system("cls")
            input("The file you were trying to open does not exist.\nPress ENTER to try again.")
            read()
#---------------------------------------------------
def main_menu():
    system("cls")
    try:
        options = int(input("What would you like to do?: \n\n1)Register a new pet.\n2)Open a pet's file.\n3)Exit\n\n"))            
    except ValueError:
        system("cls")
        input("You must select 1 or 2 please.\nPress ENTER to try again")
        main_menu()
    else:
        if options == 1:
            packing_data()
            system("cls")
            input("Done!\n\nPress ENTER to head back to the menu.")
            main_menu()
        elif options == 2:
            read()
            main_menu()
        elif options == 3:
            system("cls")
            quit()    
        else:
            system("cls")
            input("You must select 1 or 2 please.\nPress ENTER to try again")
            main_menu()
#---------------------------------------------------
main_menu()


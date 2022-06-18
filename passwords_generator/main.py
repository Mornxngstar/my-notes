import random
from os import system

def main():  
    #the password must have atleast 8 digits and max 15
    passw = [
    random.randint(1, 3),         # 1 mayusc min and 3 max 
    random.randint(4, 7),         # 4 minusules min and 7 max 
    random.randint(2,3),          # 2 numbers min and 3 max 
    random.randint(1,2)           # 1 special min character and 2 max
    ]

    def collecting(paths):
        # each kind of character (Mayusc, minus, numbers and specials), will be sorted in a different list
        # and this lists will be in a General list (2D)

        gen_char = []    # General list

        for i in paths:
            char = []    # list for one kinf of character
            f = open(f".\\passwords_generator\\{i}", 'r')
            for line in f:
                char.append(line.strip("\n"))
            gen_char.append(char)

            # if we are working with the file that contains letters (upper_case.txt) we will lower case
            # those already appended inside of 'char' to an alternative 'char2' and then to the General list

            if i == "upper_case.txt":
                char2 = []
                for j in char:
                    char2.append(j.lower())
                gen_char.append(char2)
                f.close()
            f.close()     
        return gen_char

    def generate(passw, chars):
        psw = []            # psw will contain the characters generated
        password = ""       # contains the characters generated as a string and shuffled

        counter = 0    # indicator so we can know wich list of characters to access when generating a random char
                       # 0 = upper cases, 1 = lower cases, 2 = numbers and 3 = specials

        for i in passw:     # 'i' would be the random amount of characters will be generated
            for j in range(i):
                w = random.choice(chars[counter])
                psw.append(w)
            counter += 1

        random.shuffle(psw)   
        for i in psw:
            password += i
            
        return password

    def menu():
        system('cls')
        input("Press ENTER to generate a password\n\n")
        paths = ["upper_case.txt","numbers.txt","special_characters.txt"]
        char = collecting(paths)
        password = generate(passw,char)
        input(password+"\n\n")
        menu()
    
    menu()

if __name__ == '__main__':
    main()
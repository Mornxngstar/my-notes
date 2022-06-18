from os import system

user_data = {"UserName": None, "Password": None}

def run():
    system('cls')
    def create_account():
        system('cls')
        user_data["UserName"] = input("Enter a username: ")
        user_data["Password"] = input("Enter a password: ")
        input("You have succesfully created a new account. Press ENTER to continue.\n\n")

    username = input("Enter your username: ")
    password = input("Enter you password: ")
    system('cls')

    if username == user_data["UserName"] and password == user_data["Password"]:
        system('cls')
        print("You have succesfully logged in.")
    elif username == user_data["UserName"] and password != user_data["Password"]:
        system('cls')
        print("Password not recognized.")
        run()
    elif username != user_data:
        system('cls')
        input("User not found. Please create an account.\n\n")
        create_account()
        run()
        


if __name__ == '__main__':
    run()
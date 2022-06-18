age = int(input("How old are you?: "))

if age >= 100:
    print("How are you even still breathing?")
elif age >= 18:
    print("You are an adult.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You ain't an adult.")
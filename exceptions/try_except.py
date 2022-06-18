
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator 
    if result == 3:
        raise ValueError("Forbbiden value")
except ValueError as e:
    print("Enter a number please\n", e)
except ZeroDivisionError as e:
    print("You cannot divide by zero\n", e)
except Exception:
    print("Something went wrong")
else:
    print(result)  
finally:
    print("This will always execute")


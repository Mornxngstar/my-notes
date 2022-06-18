
def is_palindrome(word):
    try:
        word = word.replace(" ","").lower()
        if len(word) == 0: raise ValueError("Not empty strings please")
    except ValueError as ve:
        print(ve)
        return False

    return word == word[::-1]

def run():
    answr = input("Enter your word: ")
    try:
        print(is_palindrome(answr))
    except ValueError:
        print("ONLY TEXT")
        run()

if __name__ == '__main__':
    run()
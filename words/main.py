from os import system

def run():
    system('cls')
    sentence = input("Enter your sentence: ")
    system('cls')
    word = input("Enter the word you'd like to change: ")
    system('cls')
    index = sentence.find(word)
    while index < 0:
        system('cls')
        word = input("Word not found. Try again: ")
        index = sentence.find(word)
    
    system('cls')
    replacement = input("And finally, what word do you want to place instead?: ")

    new_sentence = sentence.replace(word, replacement)
    system('cls')
    print(new_sentence)
    


if __name__ == '__main__':
    run()

from os import system

def new_game():
    guesses = []
    correct_answers = 0
    num = 0
    for key in questions:
        system("cls")
        print("-------------------------------")
        print(key,'\n')
        for i in options[num]:
            print(i)
        player_answer = input("Enter your answer: ").upper()
        guesses.append(player_answer)
        correct_answers += check_answer(questions.get(key),player_answer)
        num += 1
    display_score(correct_answers, guesses)
#-----------------------
def check_answer(correct_answer, player_answer):
    if correct_answer == player_answer:
        return 1
    else:
        return 0
#-----------------------
def display_score(correct_answers,guesses):
    system("cls")
    print("-------------------------------")
    print("RESULTS")
    print("-------------------------------")
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()
    print("Answers: ", end="") 
    for i in questions:
        print(questions.get(i), end="")
    print()
    score = int((correct_answers/len(questions)) * 100)
    print("Your score is: "+ str(score) +"%")
    input("-------------------------------")
#-----------------------
def play_again():
    system("cls")
    print("-------------------------------")
    answr = input("Would you like to play again? (y/n)\n"). lower()
    if answr == "y":
        return True
    else:
        return False
#-----------------------

questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()

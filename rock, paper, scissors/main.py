import random
from os import system

choices = ["rock","paper","scissors"]

def checking_winner(p,c):  #p = player / c = computer
    #0 = Tie / 1 = Victory / 2 = Defeat
    #choices[0] = rock / choices[1] = paper / choices[2] = scissors
    if p == c:
        return 0
    elif p == choices[0]:
        if c == choices[1]:
            return 2
        elif c == choices[2]:
            return 1
    elif p == choices[1]:
        if c == choices[0]:
            return 1
        elif c == choices[2]:
            return 2
    elif p == choices[2]:
        if c == choices[0]:
            return 2
        elif c == choices[1]:
            return 1

def main_menu():
    system("cls")
    computer = random.choice(choices)  #computer chooses one option to play
    player = None
    while player not in choices:
            system("cls")
            player = input("Rock, paper or scissors?\n\n").lower()
    result = checking_winner(player,computer)
    if result == 0:
        system("cls")
        input("TIE\n\nPlayer: {0}\nComputer: {1}\n\nPress ENTER to play again.\n".format(player.capitalize(), 
        computer.capitalize()))
        main_menu()
    elif result == 1:
        system("cls")
        input("YOU WIN\n\nPlayer: {0}\nComputer: {1}\n\nPress ENTER to play again.\n".format(player.capitalize(), 
        computer.capitalize()))
        main_menu()
    elif result == 2:
        system("cls")
        input("YOU LOSE\n\nPlayer: {0}\nComputer: {1}\n\nPress ENTER to play again.\n".format(player.capitalize(), 
        computer.capitalize()))
        main_menu()

main_menu()
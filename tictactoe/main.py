from os import system

def main():
    showing = [" "," "," "," "," "," "," "," "," "]
    options = [1,2,3,4,5,6,7,8,9]
    player1 = "X"
    player2 = "O"
    turn = False
    first = False
    times = 9 

    def printing(first):
        system('cls')
        counter = 0
        if first:
            for i in options:
                if i == "X" or i == "O":
                    showing[counter] = i
                counter += 1
            print("|  {0}  |  {1}  |  {2}  |\n|  {3}  |  {4}  |  {5}  |\n|  {6}  |  {7}  |  {8}  |\n\n".format(showing[0],
            showing[1],showing[2],showing[3],showing[4],showing[5],showing[6],showing[7],showing[8]))
    
        else:
            print("|  {0}  |  {1}  |  {2}  |\n|  {3}  |  {4}  |  {5}  |\n|  {6}  |  {7}  |  {8}  |\n\n".format(options[0],
            options[1],options[2],options[3],options[4],options[5],options[6],options[7],options[8]))
    
    def play(choice,player):
        for i in options:
            if choice == i:
                options[i-1] = player
                break
    
    def checking():

        f1, f2, f3 = 0, 1, 2
        f4, f5, f6 = 3, 4, 5
        f7, f8, f9 = 6, 7, 8

        if options[f1] == options[f2] == options[f3]:
            return True
        elif options[f4] == options[f5] == options[f6]:
            return True
        elif options[f7] == options[f8] == options[f9]:
            return True
        elif options[f1] == options[f4] == options[f7]:
            return True
        elif options[f2] == options[f5] == options[f8]:
            return True
        elif options[f3] == options[f6] == options[f9]:
            return True
        elif options[f1] == options[f5] == options[f9]:
            return True
        elif options[f3] == options[f5] == options[f7]:
            return True
        else:
            return False

    def menu(turn,times):
        turn = not turn
        choice = None
        first = True

        if turn:
            playing = "PLAYER 1"
        else:
            playing = "PLAYER 2"

        while choice not in options:
            printing(first)
            try:
                choice = int(input(f"{playing}\n\nChoose a box.\n\n"))
            except ValueError:
                system('cls')
                input("Enter only a number between 1 and 9.")
                turn = not turn
                menu(turn,times)
        
        if turn:
            play(choice,player1)
            times -= 1
            win_con = checking()
            if win_con:
                printing(first)
                input(f"{playing} WINS\n\nPress ENTER to play again\n\n")
                main()
            elif times == 0:
                printing(first)
                input("TIE\n\nPress ENTER to play again\n\n")
                main()
        
        else:
            play(choice,player2)
            times -= 1
            win_con = checking()
            if win_con:
                printing(first)
                input(f"{playing} WINS\n\nPress ENTER to play again\n\n")
                main()
            elif times == 0:
                printing(first)
                input("TIE\n\nPress ENTER to play again\n\n")
                main()

        menu(turn,times)

    printing(first)
    input("To select a box, enter its number.\n\nPress ENTER to start the game\n\n")
    menu(turn,times)

if __name__ == "__main__":
    main()
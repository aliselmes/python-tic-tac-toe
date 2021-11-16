#Create the game board
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#Main game function
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It is " + turn +'\'s' + " turn!" + " Select a space on the board using the numberpad...")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else: 
            print('That space is already taken, choose another space!')
            continue
        
        #check the winning conditions if more than 5 moves
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGAME OVER\n")
                print(" *** " + turn + " won! " + "*** ")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nGAME OVER\n")
                print(" *** " + turn + " won! " + "*** ")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGAME OVER\n")
                print(" *** " + turn + " won! " + "*** ")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nGAME OVER\n")
                print(" *** " + turn + " won! " + "*** ")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nGAME OVER\n")
                print(" *** " + turn + " won! " + "*** ")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGAME OVER\n")
                print(" *** " + turn + " won! " + "*** ")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGAME OVER\n")
                print(" *** " + turn + " won! " + "*** ")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGAME OVER\n")
                print(" *** " + turn + " won! " + "*** ")
                break
        
        #Tie
        if count == 9:
            print("\nGAME OVER\n")
            print("It's a tie!")

        #Change player after every move:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    #restart the game
    board_keys = []

    for key in theBoard:
        board_keys.append(key)

    restart = input('Do you want to play again? (y/n)')

    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            theBoard[key] = ' '
    
        game()
    else:
        print("Goodbye!")
        exit()

if __name__ == "__main__":
    game()

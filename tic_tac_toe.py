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
            theBoard[move] == turn
            count += 1
        else: 
            print('That space is already taken, choose another space!')
            continue
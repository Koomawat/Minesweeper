from createboard import *
from agent import *
from more_termcolor.colors import brightred, brightgreen, brightyellow, brightblue, brightmagenta, brightcyan

# Print out the board with the specified colors
def printBoard(board):

    for i in range(len(board)):
        row = ""
        for j in range(len(board)):
            current = str(board[i,j])
            if (current) == 'M':
                row += brightred(current) + "  "
            elif (current) == '1':
                row += brightblue(current) + "  "
            elif (current) == '2':
                row += brightgreen(current) + "  "
            elif (current) == '3':
                row += brightcyan(current) + "  "
            elif (current) == '4':
                row += brightmagenta(current) + "  "
            elif (current) == '5':
                row += brightyellow(current) + "  "
            elif (current) == '6':
                row += brightyellow(current) + "  "
            elif (current) == '7':
                row += brightyellow(current) + "  "
            elif (current) == '8':
                row += brightyellow(current) + "  "
            else:
                row += current + "  "
        print(row)

    return 


def main():

    boardDimension = int(input("Enter the dimension of the board: "))

    if boardDimension <= 5:
        print("Board too small")
        exit()

    initial = board(boardDimension)

    mines = int(input("Enter the number of mines: "))

    minesweeper = minePlacer(mines, initial)

    minesweeperHints = hintsCalculator(minesweeper)

    printBoard(minesweeperHints)

    result = search(minesweeperHints, boardDimension)

    print()

    printBoard(result)

if __name__ == "__main__":
    main()
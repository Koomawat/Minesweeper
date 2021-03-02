from createboard import *
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from more_termcolor.colors import brightred, brightgreen, brightyellow, brightblue, brightmagenta, brightcyan

def main():

    boardDimension = int(input("Enter the dimension of the board: "))

    if boardDimension <= 5:
        print("Board too small")
        exit()

    minesweeper = board(boardDimension)

    mines = int(input("Enter the number of mines: "))

    minesweeper = minePlacer(mines, minesweeper)

    minesweeper = hintsCalculator(minesweeper)

    for i in range(len(minesweeper)):
        row = ""
        for j in range(len(minesweeper)):
            current = str(minesweeper[i,j])
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


if __name__ == "__main__":
    main()
from createboard import *
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from termcolor import colored

def main():

    boardDimension = int(input("Enter the dimension of the board: "))

    #mines = int(input("Enter the number of mines: "))

    minesweeper = board(boardDimension)
    #minesweeper[0,5] = 1
   

    mines = int(input("Enter the number of mines: "))

    minesweeper = minePlacer(mines, minesweeper)

    #plt.imshow(minesweeper)
    #plt.pcolor(minesweeper, edgecolors ='k', linewidths=1)
    #plt.xticks(np.arange(0.5, len(minesweeper), 1), color = 'white')
    #plt.yticks(np.arange(0.5, len(minesweeper), 1), color = 'white')
    #plt.grid(linestyle='-', linewidth='1', color ='white')
    #plt.show()

    #print()
    for i in range(len(minesweeper)):
        row = ""
        for j in range(len(minesweeper)):
            current = str(minesweeper[i,j])
            if (current) == 'M':
                row += "  " + colored((current),'red')
            else:
                row += "  " + current
        print(row)



if __name__ == "__main__":
    main()
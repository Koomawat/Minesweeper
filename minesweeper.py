from createboard import *
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def main():

    boardDimension = int(input("Enter the dimension of the board: "))

    #mines = int(input("Enter the number of mines: "))

    minesweeper = board(boardDimension)

    plt.imshow(minesweeper)
    plt.xticks(np.arange(0.5, len(minesweeper), 1), color = 'white')
    plt.yticks(np.arange(0.5, len(minesweeper), 1), color = 'white')
    plt.grid(linestyle='-', linewidth='1', color ='white')
    plt.show()

if __name__ == "__main__":
    main()
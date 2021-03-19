from createboard import *
from agent import *
from advAgent import *

def main():

    boardDimension = int(input("Enter the dimension of the board: "))

    if boardDimension <= 5:
        print("Board too small")
        exit()

    initial = board(boardDimension)

    mines = int(input("Enter the number of mines: "))

    minesweeper = minePlacer(mines, initial)

    minesweeperHints = hintsCalculator(minesweeper)

    # printBoard(minesweeperHints)
    printAdvBoard(minesweeperHints)

    # result, mineHits = search(minesweeperHints, boardDimension)
    result, mineHits = advSearch(minesweeperHints, boardDimension)

    print()

    # printBoard(result)
    printAdvBoard(result)

    print()

    #M,m = mineScan(result, boardDimension)

    percent = (mines-mineHits) / mines
    percent *= 100

    print("Found", percent, "percent of mines without hitting a mine")

if __name__ == "__main__":
    main()
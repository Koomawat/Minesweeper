from createboard import *
from agent import *
from advAgent import *

# x = mine density
# y = average final score

def plotting():

    # Initialize the averages for the basic and advanced agents
    basicAgentAvg, advAgentAvg = [], []
    # Mine density testing
    mineDensity = [x * 0.05 for x in range(1, 20)]


    # Get the desired board size => can change it to just 1 fixed size if neeeded
    boardDimension = int(input("Enter the dimension of the board: "))
    if boardDimension <= 5:
        print("Board too small")
        exit()

    # Do minesweeper runs for each density being tested
    for x in range(1, 20):
        # Get the amount of mines needed for the current density
        mines = (boardDimension * boardDimension) * 0.5 * x
        # if for some reason it exceeds the limit (which it shouldnt)
        if mines > boardDimension * boardDimension:
            print("Mine limit exceeded")
            exit()
        
        # hold the various boards being tested so that they can be done on both basic and advanced agents
        boards = []

        # Create this many boards
        for y in range(0, 10):
            # Create the board
            initial = board(boardDimension)
            # Add mines to the board
            minesweeper = minePlacer(mines, initial)
            # Add the hints to the board
            finalBoard = hintsCalculator(minesweeper)
            # Add the board to the list
            boards.append(finalBoard)
        
        # Since we are calculating for the average final score => 
        # total up the finalScores and divide by the # of mines * the amount of boards made



if __name__ == "__main__":
    main()
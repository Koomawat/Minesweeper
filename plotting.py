from createboard import *
from agent import *
from advAgent import *
from matplotlib import pyplot as plt
from matplotlib import colors
from decimal import Decimal

# x = mine density
# y = average final score
def main():
    plotting()
    print("End of the program.")


def plotting():

    # Initialize the averages for the basic and advanced agents
    basicAgentAvgList, advAgentAvgList = [], []
    # Mine density testing
    mineDensity = [x * 0.05 for x in range(1, 21)]


    # Get the desired board size => can change it to just 1 fixed size if neeeded
    boardDimension = int(input("Enter the dimension of the board: "))
    if boardDimension <= 5:
        print("Board too small")
        exit()

    # Do minesweeper runs for each density being tested
    for x in range(1, len(mineDensity)+1):
        # Get the amount of mines needed for the current density
        mines = (boardDimension * boardDimension) * 0.05 * x
        # if for some reason it exceeds the limit (which it shouldnt)
        if mines > boardDimension * boardDimension:
            print("Mine limit exceeded")
            exit()
        
        # hold the various boards being tested so that they can be done on both basic and advanced agents
        boards = []

        # Create this many boards
        for y in range(0, 10): # change this back to 10 later
            # Create the board
            initial = board(boardDimension)
            # Add mines to the board
            minesweeper = minePlacer(int(mines), initial)
            # Add the hints to the board
            finalBoard = hintsCalculator(minesweeper)
            # Add the board to the list
            boards.append(finalBoard)
        
        # the total score of the agent in the 10 runs
        basicAgentScore, advAgentScore = 0, 0
        # Since we are calculating for the average final score => 
        # total up the finalScores and divide by the # of mines * the amount of boards made
        # now for each maze, run the basic and advanced agents
        for currBoard in boards:
            # Basic agent
            result, mineHits = search(finalBoard, boardDimension)
            percent = ((mines-mineHits) / mines)*100
            basicAgentScore += percent
            # Advanced agent
            result, mineHits = advSearch(finalBoard, boardDimension)
            advScore = ((mines - mineHits) / mines)*100
            advAgentScore += advScore

        #put averages to be plotted here
        basicAgentScoreAvg = basicAgentScore/(len(boards)) #Change according to board amount here
        basicAgentAvgList.append(basicAgentScoreAvg)
        advAgentScoreAvg = advAgentScore/(len(boards))
        advAgentAvgList.append(advAgentScoreAvg)

    #Begin plotting
    plt.plot(mineDensity, basicAgentAvgList, label = "Basic Agent")
    plt.plot(mineDensity, advAgentAvgList, label = "Advanced Agent")

    plt.xlabel('Mine Density')
    plt.ylabel('Average Final Score')
    plt.title(f"Basic and Advanced Agent Final Score Comparisons\n Board size: {boardDimension} x {boardDimension}")
    plt.legend(loc = "upper right")
    plt.show()            

        




if __name__ == "__main__":
    main()
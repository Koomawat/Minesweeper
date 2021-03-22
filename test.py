import random, numpy as np
from createboard import *
from agent import *
from advAgent import *


def main():

    board = theBoard()
    board = np.array(board)

    basicResult, mineHits = search(board, len(board))

    print('*\n*\n*\n')

    advResult, mineHits = advSearch(board, len(board))

    print('Basic result: ')
    printBoard(basicResult)

    print('*\n*\n*\n')

    print('Advanced result: ')
    printAdvBoard(advResult)
    print()



def createBoard():
    # Initialize the board
    boardDimension = int(input("Enter the dimension of the board: "))
    if boardDimension <= 5:
        print("Board too small")
        exit()
    initial = board(boardDimension)

    # Place the desired amount of mines and display an error when there are more mines than available cells
    mines = int(input("Enter the number of mines: "))    
    if mines >= boardDimension * boardDimension:
        print("Mine limit exceeded")
        exit()
    minesweeper = minePlacer(mines, initial)
    # printBoard(minesweeper)



    minesweeperHints = hintsCalculator(minesweeper)
    # printBoard(minesweeperHints)
    # printAdvBoard(minesweeperHints)

    return minesweeperHints

def theBoard():

    daBoard = [
            [0,   0, 0,   2, 'M', 1,   0, 0, 0, 0],
            [0,   1, 1,   2, 'M', 1,   0, 0, 0, 0],
            [0,   1, 1,   2, 1,   1,   0, 0, 0, 0],
            [0,   1, 'M', 1, 0,   0,   0, 0, 0, 0],
            [1,   2, 1,   1, 1,   1,   1, 0, 0, 0],
            ['M', 1, 0,   1, 3,   'M', 2, 0, 0, 0],
            [1,   1, 0,   1, 'M', 'M', 2, 0, 0, 0],
            [0,   0, 0,   1, 3,   3,   2, 0, 0, 0],
            [0,   1, 1,   1, 2,   'M', 2, 0, 0, 0],
            [0,   1, 'M', 1, 2,   'M', 2, 0, 0, 0]
        ]
    
    return daBoard
    

def decisionTest():
    # Initialize the board
    boardDimension = int(input("Enter the dimension of the board: "))
    if boardDimension <= 5:
        print("Board too small")
        exit()
    initial = board(boardDimension)

    # Place the desired amount of mines and display an error when there are more mines than available cells
    mines = int(input("Enter the number of mines: "))    
    if mines >= boardDimension * boardDimension:
        print("Mine limit exceeded")
        exit()
    minesweeper = minePlacer(mines, initial)
    minesweeperHints = hintsCalculator(minesweeper)
    
    board, mineList =  searches()

def searchesssssss():

    # Fill in cells as unknown
    result = board(dim)
    for i in range(dim):
        for j in range(dim):
            result[i,j] = '-'

    # Getting a starter random cell to start the game
    x = random.randint(0,dim-1)
    y = random.randint(0,dim-1)
    #print(x, y)

    # Keeping track of when the agent hits a mine 
    mineHitList = []

    # While there are unrevealed cells, repeat until all cells are revealed.
    hiddenCells = True
    while hiddenCells:
        # The x,y coordinates to hit next unrevealed cell is randomly chosen  before looping.

        # Storing the click as a hint
        hint = minesweeper[x,y]

        # Adding the click to our knowledge base
        result[x,y] = minesweeper[x,y]
        print(f"Clicked on cell\t\tx: {str(y)},\ty: {str(x)},\thint: {str(hint)}")

        # If the cell we clicked on was a mine we update our knowledge base
        if hint == 'M':
            print("******CLICKED A MINE******")
            result[x,y] = 'm'
            mineHitList.append((x,y))
            printAdvBoard(result)

        # If the clicked cell was a 0 cell we expose the surrounding safe cells
        elif hint == 0:

            print("Safe cell 0 clicked, exposing adjacent 0 cells.")
            print('\nBefore exposing:')
            printAdvBoard(result)

            # If we can expand on adjacent 0's, expand as much as possible
            moreSafe = True
            while(moreSafe == True):
                for i in range(dim):
                    for j in range(dim):
                        if result[i,j] == 0:
                            #print((i, j))
                            # Calling exposeSafe function to add those safe cells to the knowledge base
                            result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)
            
            print('\nAfter exposing:')
            printAdvBoard(result)
        
        print('=======================================================')

        # Loop through to reveal mines/safe cells and expand only if there is a zero cell revealed on the board:
        if checkIfValueExists(result, 0):
            for i in range(dim):
                for j in range(dim):

                    # If there are no more hidden cells, then break out.
                    hiddenCells, hidden = hiddenScan(result, dim)
                    if not hiddenCells:
                        break

                    # To be compared with previously expanded board and to-be-sweeped board of it
                    expanded = copy.deepcopy(result)

                    # Calling mineSweep and safeSweep (basic agent checks of guaranteed mines or safe cells)
                    result = mineSweep(result, dim)
                    result = sweeped = safeSweep(result, minesweeper, dim)

                    # Only print the result if there is a difference
                    if not compareBoards(expanded, sweeped):
                        print()
                        print('After sweeps: ')
                        printAdvBoard(sweeped)

                    expanded = result
                    # If the current cell is 0, expand through its adjacent 0's
                    if result[i,j] == 0:
                        result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)
                        while moreSafe:
                            for i in range(dim):
                                for j in range(dim):
                                    if result[i,j] == 0:
                                        #print((i, j))
                                        result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)
                            print('After expansion loops:')
                            printAdvBoard(result)

                    # Only print hte result if there is a difference
                    if not compareBoards(expanded, sweeped):
                        print()
                        print('After expansion:')
                        printAdvBoard(result)
        
        print('Before board changes:')
        printAdvBoard(result)
                                    
        boardChange = True
        # Looping through our equations and going through inferences until no more inferences are possible and we need a random cell click in the remaining cells
        while boardChange:
            boardChange = False

            consDict = constraintsCheck(dim, result)

            # remove empty keys
            for k in list(consDict):
                if not consDict[k]:
                    del consDict[k]

            #print(consDict)
            #print()

            eqs = []

            if len(consDict) >= 1:
                eqs = guessCheck(result, consDict)

            #print(eqs)
            #print()

            oldResult = copy.deepcopy(result)

            result = equationIterate(eqs, result, minesweeper)

            printAdvBoard(result)

            result = checks(result, minesweeper, dim)

            # Keeping track of the old state of the board so we know to keep looping this process until board changes are no longer made
            if oldResult.all() != result.all():
                boardChange = True

        print('After board changes:')
        printAdvBoard(result)
        
        # Scanning for remaining hidden cells to click our next random cell
        hiddenCells, hidden = advHiddenScan(result, dim)
        if hiddenCells == False:
            hiddenCells, hidden = hiddenScan(result, dim)

        if hiddenCells == True:
            randomCell = random.choice(hidden)
            x = randomCell[0]
            y = randomCell[1]

        print('Updated before click: ')
        printAdvBoard(result)
        print('******************************************************')
        print('******************************************************')
        print('******************************************************')

    print("Agent hit mines at: ", mineHitList)
    print("Total mines clicked: " + str(len(mineHitList)))

    return result, len(mineHitList)



def permuteTest():

    #listt = []

    #listt.append((1,2))
    #listt.append((3,4))

    #test = random.choice(listt)

    #print(test[1])

    #topRightCoords = [(1,-1), (1,0), (0,-1)]
                    #   SW,     S,      W

    #for x,y in topRightCoords:
    #    print(x, y)

    lst = permute([1,0,0])
    print(lst)

def permute(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #here we need a global wise list, each time we just append to the result
        rslt=[]
        
        def dfs(temp, elements):
            #gather rslt
            if len(elements)==0:
                rslt.append(temp[:]) #still remember to use temp[:]
            for e in elements:
                temp.append(e)
                #backtrack
                next_elements=elements[:]
                next_elements.remove(e)
                
                dfs(temp, next_elements)
                temp.pop()
                
                
        dfs([],nums) #first is the current result
        return rslt

if __name__ == "__main__":
    main()
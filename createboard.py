import numpy as np
import random

###############################################################

def board(dim):

    gameboard = np.zeros(shape=(dim,dim), dtype=object)

    return gameboard

def minePlacer(n, board):

    boardCopy = board

    boardLen = len(boardCopy)

    for i in range(n):
        
        tupleX = random.randint(0, boardLen-1)
        tupleY = random.randint(0, boardLen-1)

        if (boardCopy[tupleX,tupleY] == 0):
            # M represents a mine 
            boardCopy[tupleX,tupleY] = 'M'
        else:

            placed = False

            while(placed == False):

                tupleX = random.randint(0, boardLen-1)
                tupleY = random.randint(0, boardLen-1)

                if (boardCopy[tupleX,tupleY] == 0):
                    # M represents a mine 
                    boardCopy[tupleX,tupleY] = 'M'
                    placed = True

    return boardCopy

def hintsCalculator(board):

    boardCopy = board
    boardLen = len(board)

    surroundingCoords = [(x,y) for x in range(-1,2) 
                            for y in range(-1,2)]
        # creates coordinates to add onto x,y coordinates:
        # [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for i in range(boardLen):
        for j in range(boardLen):

            if (str(board[i,j]) == '0'):

                tempHint = 0

                for x, y in surroundingCoords:
                    a, b = i, j # reset to next iteration of i, j

                    a += x
                    b += y

                    if (0 <= a < boardLen) and (0 <= b < boardLen) and (str(board[a,b]).lower() == 'm'):
                        tempHint += 1
                    
                boardCopy[i,j] = tempHint
    
    return boardCopy

# Returns true if all elements in both numpy arrays are equal
def compareBoards(original, result):
    originalConvert = np.where(original == 'm', 'M', original)
    resultConvert = np.where(result == 'm', 'M', result)
    if (originalConvert == resultConvert).all():
        return True
    else:
        return False


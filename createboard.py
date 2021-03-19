import numpy as np
import random

# The following functions search nearby neighbours based on the location of the selected cell to create the clue/hint #
def topLeft(i,j, board):

    tempHint = 0

    topLeftCoords = [(1,1), (1,0), (0,1)]
                    #  SE,    S,     E

    for x,y in topLeftCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if str(board[a, b]).lower() == 'm':
            tempHint += 1

    return tempHint


def topRight(i,j, board):

    tempHint = 0

    topRightCoords = [(1,-1), (1,0), (0,-1)]
                    #   SW,     S,      W

    for x,y in topRightCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if str(board[a, b]).lower() == 'm':
            tempHint += 1

    return tempHint


def botLeft(i,j, board):

    tempHint = 0

    botLeftCoords = [(-1,1), (-1,0), (0,1)]
                    #   NE,     N,      E

    for x,y in botLeftCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if str(board[a, b]).lower() == 'm':
            tempHint += 1

    return tempHint


def botRight(i,j, board):

    tempHint = 0

    botRightCoords = [(-1,-1), (-1,0), (0,-1)]
                    #    NW,      N,      W

    for x,y in botRightCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if str(board[a, b]).lower() == 'm':
            tempHint += 1

    return tempHint


def topEdge(i,j, board):

    tempHint = 0

    topEdgeCoords = [(0,-1), (0,1), (1,0), (1,-1), (1,1)]
                    #   W,     E,     S,     SW,    SE

    for x,y in topEdgeCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if str(board[a, b]).lower() == 'm':
            tempHint += 1

    return tempHint
    

def leftEdge(i,j, board):

    tempHint = 0

    leftEdgeCoords = [(0,1), (1,0), (1,1), (-1,0), (-1,1)]
                    #   E,     S,    SE,      N      NE

    for x,y in leftEdgeCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if str(board[a, b]).lower() == 'm':
            tempHint += 1

    return tempHint


def rightEdge(i,j, board):

    tempHint = 0

    rightEdgeCoords = [(0,-1), (1,0), (1,-1), (-1,0), (-1,-1)]
                    #   W,      S,     SW,      N,      NW
    
    for x,y in rightEdgeCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if str(board[a, b]).lower() == 'm':
            tempHint += 1

    return tempHint


def botEdge(i,j, board):

    tempHint = 0

    botEdgeCoords = [(0,-1), (-1,1), (0,1), (-1,0), (-1,-1)]
                    #   W,     NE,     E,     N,      NW

    for x,y in botEdgeCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if str(board[a, b]).lower() == 'm':
            tempHint += 1

    return tempHint


def middle(i,j, board):

    tempHint = 0

    midCoords = [(0,-1), (-1,1), (0,1), (-1,0), (-1,-1), (1,0), (1,-1), (1,1)]

    for x,y in midCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if str(board[a, b]).lower() == 'm':
            tempHint += 1

    return tempHint

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
                    
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


def safeCheck(boardLen, board):
    
    moreSafe = False

    for i in range(boardLen):
        for j in range(boardLen):

            if i == 0 and j == 0:

                #if board[i+1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True
                    
                if board[i+1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i, j+1] == '-' and board[i,j] == 0:
                    moreSafe = True

            elif i == boardLen-1 and j == 0:

                #if board[i-1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i-1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i, j+1] == '-' and board[i,j] == 0:
                    moreSafe = True

            elif i == 0 and j == boardLen-1:

                #if board[i+1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i+1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i,j-1] == '-' and board[i,j] == 0:
                    moreSafe = True

            elif i == boardLen-1 and j == boardLen-1:

                #if board[i-1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i-1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i,j-1] == '-' and board[i,j] == 0:
                    moreSafe = True

            elif i == 0 and j != 0 and j != boardLen-1:

                if board[i,j-1] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i, j+1] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i+1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i+1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                #if board[i+1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True

            elif i != 0 and i != boardLen-1 and j == 0:

                if board[i, j+1] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i+1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i+1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i-1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i-1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True

            elif i != 0 and i != boardLen-1 and j == boardLen-1:

                if board[i,j-1] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i+1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i+1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i-1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i-1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

            elif i == boardLen-1 and j != 0 and j != boardLen-1:

                if board[i-1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i-1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                #if board[i-1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i,j-1] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i, j+1] == '-' and board[i,j] == 0:
                    moreSafe = True

            else:   
                
                if board[i-1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i-1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                #if board[i-1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i+1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i+1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                #if board[i+1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i,j-1] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i, j+1] == '-' and board[i,j] == 0:
                    moreSafe = True

    return moreSafe


def topLeft(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # South East
    board[i+1,j+1] = minesweeper[i+1,j+1]
    if board[i+1,j+1] == 0:
        moreSafe = True
            
    # South
    board[i+1,j] = minesweeper[i+1,j]
    if board[i+1,j] == 0:
        moreSafe = True

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe


def topRight(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # South West 
    board[i+1,j-1] = minesweeper[i+1,j-1]
    if board[i+1,j-1] == 0:
        moreSafe = True

    # South
    board[i+1, j] = minesweeper[i+1, j]
    if board[i+1,j] == 0:
        moreSafe = True

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe


def botLeft(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # North East
    board[i-1,j+1] = minesweeper[i-1,j+1]
    if board[i-1,j+1] == 0:
        moreSafe = True

    # North
    board[i-1,j] = minesweeper[i-1,j]
    if board[i-1,j] == 0:
        moreSafe = True

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe


def botRight(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # North West 
    board[i-1,j-1] = minesweeper[i-1,j-1]
    if board[i-1,j-1] == 0:
        moreSafe = True

    # North
    board[i-1, j] = minesweeper[i-1, j]
    if board[i-1,j] == 0:
        moreSafe = True

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe


def topEdge(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0:
        moreSafe = True

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0:
        moreSafe = True

    # South
    board[i+1, j] = minesweeper[i+1, j]
    if board[i+1,j] == 0:
        moreSafe = True

    # South West 
    board[i+1,j-1] = minesweeper[i+1,j-1]
    if board[i+1,j-1] == 0:
        moreSafe = True

    # South East
    board[i+1,j+1] = minesweeper[i+1,j+1]
    if board[i+1,j+1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe
    

def leftEdge(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0:
        moreSafe = True

    # South
    board[i+1, j] = minesweeper[i+1, j]
    if board[i+1,j] == 0:
        moreSafe = True

    # South East
    board[i+1,j+1] = minesweeper[i+1,j+1]
    if board[i+1,j+1] == 0:
        moreSafe = True

    # North
    board[i-1, j] = minesweeper[i-1, j]
    if board[i-1,j] == 0:
        moreSafe = True

    # North East
    board[i-1,j+1] = minesweeper[i-1,j+1]
    if board[i-1,j+1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe


def rightEdge(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0:
        moreSafe = True

    # South
    board[i+1, j] = minesweeper[i+1, j]
    if board[i+1,j] == 0:
        moreSafe = True

    # South West 
    board[i+1,j-1] = minesweeper[i+1,j-1]
    if board[i+1,j-1] == 0:
        moreSafe = True

    # North
    board[i-1, j] = minesweeper[i-1, j]
    if board[i-1,j] == 0:
        moreSafe = True

    # North West 
    board[i-1,j-1] = minesweeper[i-1,j-1]
    if board[i-1,j-1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe


def botEdge(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # North
    board[i-1, j] = minesweeper[i-1, j]
    if board[i-1,j] == 0:
        moreSafe = True

    # North West 
    board[i-1,j-1] = minesweeper[i-1,j-1]
    if board[i-1,j-1] == 0:
        moreSafe = True
    
    return boardCopy


###############################################################
# Functionality/Utility 

# Returns true if all elements in both numpy arrays are equal, false otherwise
def compareBoards(original, result):
    originalConvert = np.where(original == 'm', 'M', original)
    resultConvert = np.where(result == 'm', 'M', result)
    if (originalConvert == resultConvert).all():
        return True
    else:
        return False

# Returns true if the value is in the board, false otherwise
def checkIfValueExists(board, value):
    return np.any(board == value)

###############################################################
# Functionality/Utility for both agents

# Scanning function to find location of hidden cells, used for the next random move call
def hiddenScan(board, dim): 
    
    hidden = False

    hiddenList = []

    for i in range(dim):
        for j in range(dim):
            if board[i,j] == '-':
                hiddenList.append((i,j))
                hidden = True

    return hidden, hiddenList

# Scanning function to scan known mine locations and get a mine count
def mineScan(board, dim):

    bigM = 0
    smallM = 0

    for i in range(dim):
        for j in range(dim):
            if board[i,j] == 'M':
                bigM += 1
            if board[i,j] == 'm':
                smallM += 1

    return bigM, smallM


# Safe check function that sees if theres a safe cell next to hidden cell, if so a True is returned so we know to expose those safe cells
def safeCheck(boardLen, board):

    moreSafe = False

    for i in range(boardLen):
        for j in range(boardLen):

            if i == 0 and j == 0:

                #if board[i+1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True
                    
                if board[i+1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i, j+1] == '-' and board[i,j] == 0:
                    moreSafe = True

            elif i == boardLen-1 and j == 0:

                #if board[i-1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i-1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i, j+1] == '-' and board[i,j] == 0:
                    moreSafe = True

            elif i == 0 and j == boardLen-1:

                #if board[i+1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i+1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i,j-1] == '-' and board[i,j] == 0:
                    moreSafe = True

            elif i == boardLen-1 and j == boardLen-1:

                #if board[i-1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i-1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i,j-1] == '-' and board[i,j] == 0:
                    moreSafe = True

            elif i == 0 and j != 0 and j != boardLen-1:

                if board[i,j-1] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i, j+1] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i+1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i+1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                #if board[i+1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True

            elif i != 0 and i != boardLen-1 and j == 0:

                if board[i, j+1] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i+1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i+1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i-1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i-1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True

            elif i != 0 and i != boardLen-1 and j == boardLen-1:

                if board[i,j-1] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i+1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i+1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i-1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i-1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

            elif i == boardLen-1 and j != 0 and j != boardLen-1:

                if board[i-1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i-1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                #if board[i-1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i,j-1] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i, j+1] == '-' and board[i,j] == 0:
                    moreSafe = True

            else:   
                
                if board[i-1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i-1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                #if board[i-1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i+1,j] == '-' and board[i,j] == 0:
                    moreSafe = True

                #if board[i+1,j-1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                #if board[i+1,j+1] == '-' and board[i,j] == 0:
                    #moreSafe = True

                if board[i,j-1] == '-' and board[i,j] == 0:
                    moreSafe = True

                if board[i, j+1] == '-' and board[i,j] == 0:
                    moreSafe = True

    return moreSafe

# Exposes top left safe cells
def topLeft(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # South East
    board[i+1,j+1] = minesweeper[i+1,j+1]
    if board[i+1,j+1] == 0:
        moreSafe = True
            
    # South
    board[i+1,j] = minesweeper[i+1,j]
    if board[i+1,j] == 0:
        moreSafe = True

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe

# Exposes top right safe cells
def topRight(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # South West 
    board[i+1,j-1] = minesweeper[i+1,j-1]
    if board[i+1,j-1] == 0:
        moreSafe = True

    # South
    board[i+1, j] = minesweeper[i+1, j]
    if board[i+1,j] == 0:
        moreSafe = True

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe

# Exposes bottom left safe cells
def botLeft(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # North East
    board[i-1,j+1] = minesweeper[i-1,j+1]
    if board[i-1,j+1] == 0:
        moreSafe = True

    # North
    board[i-1,j] = minesweeper[i-1,j]
    if board[i-1,j] == 0:
        moreSafe = True

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe

# Exposes bottom right safe cells
def botRight(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # North West 
    board[i-1,j-1] = minesweeper[i-1,j-1]
    if board[i-1,j-1] == 0:
        moreSafe = True

    # North
    board[i-1, j] = minesweeper[i-1, j]
    if board[i-1,j] == 0:
        moreSafe = True

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe

# Exposes top edge safe cells
def topEdge(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0:
        moreSafe = True

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0:
        moreSafe = True

    # South
    board[i+1, j] = minesweeper[i+1, j]
    if board[i+1,j] == 0:
        moreSafe = True

    # South West 
    board[i+1,j-1] = minesweeper[i+1,j-1]
    if board[i+1,j-1] == 0:
        moreSafe = True

    # South East
    board[i+1,j+1] = minesweeper[i+1,j+1]
    if board[i+1,j+1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe
    
# Exposes left edge safe cells
def leftEdge(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0:
        moreSafe = True

    # South
    board[i+1, j] = minesweeper[i+1, j]
    if board[i+1,j] == 0:
        moreSafe = True

    # South East
    board[i+1,j+1] = minesweeper[i+1,j+1]
    if board[i+1,j+1] == 0:
        moreSafe = True

    # North
    board[i-1, j] = minesweeper[i-1, j]
    if board[i-1,j] == 0:
        moreSafe = True

    # North East
    board[i-1,j+1] = minesweeper[i-1,j+1]
    if board[i-1,j+1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe

# Exposes right edge safe cells
def rightEdge(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0:
        moreSafe = True

    # South
    board[i+1, j] = minesweeper[i+1, j]
    if board[i+1,j] == 0:
        moreSafe = True

    # South West 
    board[i+1,j-1] = minesweeper[i+1,j-1]
    if board[i+1,j-1] == 0:
        moreSafe = True

    # North
    board[i-1, j] = minesweeper[i-1, j]
    if board[i-1,j] == 0:
        moreSafe = True

    # North West 
    board[i-1,j-1] = minesweeper[i-1,j-1]
    if board[i-1,j-1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe

# Exposes bottom edge safe cells
def botEdge(i,j, board, minesweeper, boardLen):

    moreSafe = False

    # North
    board[i-1, j] = minesweeper[i-1, j]
    if board[i-1,j] == 0:
        moreSafe = True

    # North West 
    board[i-1,j-1] = minesweeper[i-1,j-1]
    if board[i-1,j-1] == 0:
        moreSafe = True
    
    # North East
    board[i-1,j+1] = minesweeper[i-1,j+1]
    if board[i-1,j+1] == 0:
        moreSafe = True

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0:
        moreSafe = True

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe

# Exposes safe cells found in the middle (not a corner or edge)
def middle(i,j, board, minesweeper, boardLen):
    
    moreSafe = False

    # North
    board[i-1, j] = minesweeper[i-1, j]
    if board[i-1,j] == 0:
        moreSafe = True

    # North West 
    board[i-1,j-1] = minesweeper[i-1,j-1]
    if board[i-1,j-1] == 0:
        moreSafe = True

    # North East
    board[i-1,j+1] = minesweeper[i-1,j+1]
    if board[i-1,j+1] == 0:
        moreSafe = True

    # South
    board[i+1, j] = minesweeper[i+1, j]
    if board[i+1,j] == 0:
        moreSafe = True

    # South West 
    board[i+1,j-1] = minesweeper[i+1,j-1]
    if board[i+1,j-1] == 0:
        moreSafe = True

    # South East
    board[i+1,j+1] = minesweeper[i+1,j+1]
    if board[i+1,j+1] == 0:
        moreSafe = True

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0:
        moreSafe = True

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe

# Function that calls the relevant board location function to expose safe cells 
def exposeSafe(i,j, result, minesweeper, boardLen):

    boardCopy = result
    moreSafe = True

    if i == 0 and j == 0:

        boardCopy, moreSafe = topLeft(i,j, boardCopy, minesweeper, boardLen)

    elif i == boardLen-1 and j == 0:

        boardCopy, moreSafe = botLeft(i,j, boardCopy, minesweeper, boardLen)

    elif i == 0 and j == boardLen-1:

        boardCopy, moreSafe = topRight(i,j, boardCopy, minesweeper, boardLen)

    elif i == boardLen-1 and j == boardLen-1:

        boardCopy, moreSafe = botRight(i,j, boardCopy, minesweeper, boardLen)

    elif i == 0 and j != 0 and j != boardLen-1:

        boardCopy, moreSafe = topEdge(i,j, boardCopy, minesweeper, boardLen)

    elif i != 0 and i != boardLen-1 and j == 0:

        boardCopy, moreSafe = leftEdge(i,j, boardCopy, minesweeper, boardLen)

    elif i != 0 and i != boardLen-1 and j == boardLen-1:

        boardCopy, moreSafe = rightEdge(i,j, boardCopy, minesweeper, boardLen)

    elif i == boardLen-1 and j != 0 and j != boardLen-1:

        boardCopy, moreSafe = botEdge(i,j, boardCopy, minesweeper, boardLen)

    else:   
        boardCopy, moreSafe = middle(i,j, boardCopy, minesweeper, boardLen)

    return boardCopy, moreSafe

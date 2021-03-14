import numpy as np
import random

# The following functions help determine the amount of bombs surrounding the selected cell based on where it is on the board

def topLeft(i,j, board):

    tempHint = 0

    # South East
    if (board[i+1,j+1] == 'M'):
        tempHint += 1
    # South
    if (board[i+1,j] == 'M'):
        tempHint += 1
    # East
    if (board[i, j+1] == 'M'):
        tempHint += 1

    return tempHint


def topRight(i,j, board):

    tempHint = 0

    # South West 
    if (board[i+1,j-1] == 'M'):
        tempHint += 1
    # South
    if (board[i+1, j] == 'M'):
        tempHint += 1
    # West
    if (board[i,j-1] == 'M'):
        tempHint += 1

    return tempHint


def botLeft(i,j, board):

    tempHint = 0

    # North East
    if (board[i-1,j+1] == 'M'):
        tempHint += 1
    # North
    if (board[i-1,j] == 'M'):
        tempHint += 1
    # East
    if (board[i, j+1] == 'M'):
        tempHint += 1

    return tempHint


def botRight(i,j, board):

    tempHint = 0

    # North West 
    if (board[i-1,j-1] == 'M'):
        tempHint += 1
    # North
    if (board[i-1, j] == 'M'):
        tempHint += 1
    # West
    if (board[i,j-1] == 'M'):
        tempHint += 1

    return tempHint


def topEdge(i,j, board):

    tempHint = 0

    # West
    if (board[i,j-1] == 'M'):
        tempHint += 1
    # East
    if (board[i, j+1] == 'M'):
        tempHint += 1
    # South
    if (board[i+1, j] == 'M'):
        tempHint += 1
    # South West 
    if (board[i+1,j-1] == 'M'):
        tempHint += 1
    # South East
    if (board[i+1,j+1] == 'M'):
        tempHint += 1

    return tempHint
    

def leftEdge(i,j, board):

    tempHint = 0

    # East
    if (board[i, j+1] == 'M'):
        tempHint += 1
    # South
    if (board[i+1, j] == 'M'):
        tempHint += 1
    # South East
    if (board[i+1,j+1] == 'M'):
        tempHint += 1
    # North
    if (board[i-1, j] == 'M'):
        tempHint += 1
    # North East
    if (board[i-1,j+1] == 'M'):
        tempHint += 1

    return tempHint


def rightEdge(i,j, board):

    tempHint = 0

    # West
    if (board[i,j-1] == 'M'):
        tempHint += 1
    # South
    if (board[i+1, j] == 'M'):
        tempHint += 1
    # South West 
    if (board[i+1,j-1] == 'M'):
        tempHint += 1
    # North
    if (board[i-1, j] == 'M'):
        tempHint += 1
    # North West 
    if (board[i-1,j-1] == 'M'):
        tempHint += 1

    return tempHint


def botEdge(i,j, board):

    tempHint = 0

    # North
    if (board[i-1, j] == 'M'):
        tempHint += 1
    # North West 
    if (board[i-1,j-1] == 'M'):
        tempHint += 1
    # North East
    if (board[i-1,j+1] == 'M'):
        tempHint += 1
    # West
    if (board[i,j-1] == 'M'):
        tempHint += 1
    # East
    if (board[i, j+1] == 'M'):
        tempHint += 1

    return tempHint


def middle(i,j, board):

    tempHint = 0

    # North
    if (board[i-1, j] == 'M'):
        tempHint += 1
    # North West 
    if (board[i-1,j-1] == 'M'):
        tempHint += 1
    # North East
    if (board[i-1,j+1] == 'M'):
        tempHint += 1
    # South
    if (board[i+1, j] == 'M'):
        tempHint += 1
    # South West 
    if (board[i+1,j-1] == 'M'):
        tempHint += 1
    # South East
    if (board[i+1,j+1] == 'M'):
        tempHint += 1
    # West
    if (board[i,j-1] == 'M'):
        tempHint += 1
    # East
    if (board[i, j+1] == 'M'):
        tempHint += 1

    return tempHint

# Create the board with its specified parameters
def board(dim):

    gameboard = np.zeros(shape=(dim,dim), dtype=object)

    return gameboard

# Place the mines randomly throughout the board
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

# Calculate the hints for all the cells of the board
def hintsCalculator(board):

    boardCopy = board

    boardLen = len(board)

    for i in range(boardLen):

        for j in range(boardLen):
            
            if(boardCopy[i,j] == 0):

                tempHint = 0

                if i == 0 and j == 0:

                    tempHint = topLeft(i,j, boardCopy)

                elif i == boardLen-1 and j == 0:

                    tempHint = botLeft(i,j, boardCopy)

                elif i == 0 and j == boardLen-1:

                    tempHint = topRight(i,j, boardCopy)

                elif i == boardLen-1 and j == boardLen-1:

                    tempHint = botRight(i,j, boardCopy)

                elif i == 0 and j != 0 and j != boardLen-1:

                    tempHint = topEdge(i,j, boardCopy)

                elif i != 0 and i != boardLen-1 and j == 0:

                    tempHint = leftEdge(i,j, boardCopy)

                elif i != 0 and i != boardLen-1 and j == boardLen-1:

                    tempHint = rightEdge(i,j, boardCopy)

                elif i == boardLen-1 and j != 0 and j != boardLen-1:

                    tempHint = botEdge(i,j, boardCopy)

                else:   
                    tempHint = middle(i,j, boardCopy)


                boardCopy[i,j] = tempHint
                


    return boardCopy
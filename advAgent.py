from createboard import *
from mineRevealer import *
from safeHiddenRevealer import *
import random
from more_termcolor.colors import brightred, brightgreen, brightyellow, brightblue, brightmagenta, brightcyan
import copy

def printAdvBoard(board):
    n = len(board)
    print(" "*(len(str(n))+1), end='')
    for i in range(n):
        if i >= 10: 
            i = i-(10*(int(i/10)))
        print(str(i) + "  ", end='')
    print()

    for i in range(len(board)):
        row = ""
        print(str(i).zfill(len(str(n))) + "|", end='')
        for j in range(len(board)):
            current = str(board[i,j])
            if (current) == 'm':
                row += brightred(current) + "  "
            elif (current) == 'M':
                row += brightred(current) + "  "
            elif (current) == '1':
                row += brightblue(current) + "  "
            elif (current) == '2':
                row += brightgreen(current) + "  "
            elif (current) == '3':
                row += brightcyan(current) + "  "
            elif (current) == '4':
                row += brightmagenta(current) + "  "
            elif (current) == '5':
                row += brightyellow(current) + "  "
            elif (current) == '6':
                row += brightyellow(current) + "  "
            elif (current) == '7':
                row += brightyellow(current) + "  "
            elif (current) == '8':
                row += brightyellow(current) + "  "
            else:
                row += current + "  "
        print(row)
    print()

    return 


def hiddenScan(board, dim): 
    
    hidden = False

    hiddenList = []

    for i in range(dim):
        for j in range(dim):
            if board[i,j] == '-':
                hiddenList.append((i,j))
                hidden = True

    return hidden, hiddenList


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


def exposeSafe(i,j, result, minesweeper, dim):

    boardCopy = result

    compare = minesweeper

    boardLen = dim

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


def constraintsCheck(boardLen, board):

    constraints = {(i,j) :
    [] for i in range(boardLen)
            for j in range(boardLen)
                if (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8)}

    for i,j in constraints.keys():
        
        if i == 0 and j == 0:

            # E
            if board[i, j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i,j+1))

            # S     
            if board[i+1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i+1,j))

            # SE
            if board[i+1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i+1,j+1))

        elif i == boardLen-1 and j == 0:

            # N
            if board[i-1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i-1,j))

            # NE
            if board[i-1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i-1,j+1))

            # E
            if board[i, j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
               constraints[(i,j)].append((i,j+1))

        elif i == 0 and j == boardLen-1:

            # W
            if board[i,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i,j-1))

            # SW
            if board[i+1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i+1,j-1))

            # S
            if board[i+1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i+1,j))

        elif i == boardLen-1 and j == boardLen-1:

            # NW
            if board[i-1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i-1,j-1))

            # N
            if board[i-1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i-1,j))

            # W
            if board[i,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i,j-1))

        elif i == 0 and j != 0 and j != boardLen-1:

            # W
            if board[i,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i,j-1))

            # E
            if board[i, j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i,j+1))

            # SW
            if board[i+1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i+1,j-1))

            # S
            if board[i+1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i+1,j))

            # SE
            if board[i+1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i+1,j+1))

        elif i != 0 and i != boardLen-1 and j == 0:

            # N
            if board[i-1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i-1,j))

            # NE
            if board[i-1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i-1,j+1))

            # E
            if board[i, j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i,j+1))

            # S
            if board[i+1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i+1,j))

            # SE
            if board[i+1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i+1,j+1))

        elif i != 0 and i != boardLen-1 and j == boardLen-1:

            # NW
            if board[i-1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i-1,j-1))

            # N
            if board[i-1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i-1,j))

            # W
            if board[i,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i,j-1))

            # SW
            if board[i+1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i+1,j-1))

            # S
            if board[i+1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i+1,j))

        elif i == boardLen-1 and j != 0 and j != boardLen-1:

            # NW
            if board[i-1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i-1,j-1))

            # N
            if board[i-1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i-1,j))

            # NE
            if board[i-1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i-1,j+1))

            # W
            if board[i,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i,j-1))

            # E
            if board[i, j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i,j+1))

        else:   
                
            # NW
            if board[i-1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i-1,j-1))

            # N
            if board[i-1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i-1,j))

            # NE
            if board[i-1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i-1,j+1))

            # W
            if board[i,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i,j-1))

            # E
            if board[i, j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i,j+1))

            # SW
            if board[i+1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i+1,j-1))

            # S
            if board[i+1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i+1,j))
            
            # SE
            if board[i+1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                constraints[(i,j)].append((i+1,j+1))

    return constraints


def permuteConstraints(numList):

    permutationsList = []
        
    def dfsBacktrack(currPermutation, elems):

        elemLen = len(elems)

        if elemLen == 0:
            permutationsList.append(currPermutation[:]) 

        # Only unique permutations
        unique = list(set(elems))

        for number in unique:
                
            currPermutation.append(number)

            nextElem = elems[:]

            nextElem.remove(number)
                
            #backtracking
            dfsBacktrack(currPermutation, nextElem)

            currPermutation.pop()
                
                
    dfsBacktrack( [], numList) 


    return permutationsList


def surroundingMines(board, tuple):

    count = 0

    boardLen = len(board)

    i = tuple[0]
    j = tuple[1]

    if i == 0 and j == 0:

            # E
            if board[i, j+1] == 'M' or board[i, j+1] == 'm':
                count+=1

            # S     
            if board[i+1,j] == 'M' or board[i+1,j] == 'm':
                count+=1

            # SE
            if board[i+1,j+1] == 'M' or board[i+1,j+1] == 'm':
                count+=1

    elif i == boardLen-1 and j == 0:

            # N
            if board[i-1,j] == 'M' or board[i-1,j] == 'm':
                count+=1

            # NE
            if board[i-1,j+1] == 'M' or board[i-1,j+1] == 'm':
                count+=1

            # E
            if board[i, j+1] == 'M' or board[i, j+1] == 'm':
               count+=1

    elif i == 0 and j == boardLen-1:

            # W
            if board[i,j-1] == 'M' or board[i,j-1] == 'm':
                count+=1

            # SW
            if board[i+1,j-1] == 'M' or board[i+1,j-1] == 'm':
                count+=1

            # S
            if board[i+1,j] == 'M' or board[i+1,j] == 'm':
                count+=1

    elif i == boardLen-1 and j == boardLen-1:

            # NW
            if board[i-1,j-1] == 'M' or board[i-1,j-1] == 'm':
                count+=1

            # N
            if board[i-1,j] == 'M' or board[i-1,j] == 'm':
                count+=1

            # W
            if board[i,j-1] == 'M' or board[i,j-1] == 'm':
                count+=1

    elif i == 0 and j != 0 and j != boardLen-1:

            # W
            if board[i,j-1] == 'M' or board[i,j-1] == 'm':
                count+=1

            # E
            if board[i, j+1] == 'M' or board[i, j+1] == 'm':
                count+=1

            # SW
            if board[i+1,j-1] == 'M' or board[i+1,j-1] == 'm':
                count+=1

            # S
            if board[i+1,j] == 'M' or board[i+1,j] == 'm':
                count+=1

            # SE
            if board[i+1,j+1] == 'M' or board[i+1,j+1] == 'm':
                count+=1

    elif i != 0 and i != boardLen-1 and j == 0:

            # N
            if board[i-1,j] == 'M' or board[i-1,j] == 'm':
                count+=1

            # NE
            if board[i-1,j+1] == 'M' or board[i-1,j+1] == 'm':
                count+=1

            # E
            if board[i, j+1] == 'M' or board[i, j+1] == 'm':
                count+=1

            # S
            if board[i+1,j] == 'M' or board[i+1,j] == 'm':
                count+=1

            # SE
            if board[i+1,j+1] == 'M' or board[i+1,j+1] == 'm':
                count+=1

    elif i != 0 and i != boardLen-1 and j == boardLen-1:

            # NW
            if board[i-1,j-1] == 'M' or board[i-1,j-1] == 'm':
                count+=1

            # N
            if board[i-1,j] == 'M' or board[i-1,j] == 'm':
                count+=1

            # W
            if board[i,j-1] == 'M' or board[i,j-1] == 'm':
                count+=1

            # SW
            if board[i+1,j-1] == 'M' or board[i+1,j-1] == 'm':
                count+=1

            # S
            if board[i+1,j] == 'M' or board[i+1,j] == 'm':
                count+=1

    elif i == boardLen-1 and j != 0 and j != boardLen-1:

            # NW
            if board[i-1,j-1] == 'M' or board[i-1,j-1] == 'm':
                count+=1

            # N
            if board[i-1,j] == 'M' or board[i-1,j] == 'm':
                count+=1

            # NE
            if board[i-1,j+1] == 'M' or board[i-1,j+1] == 'm':
                count+=1

            # W
            if board[i,j-1] == 'M' or board[i,j-1] == 'm':
                count+=1

            # E
            if board[i, j+1] == 'M' or board[i, j+1] == 'm':
                count+=1

    else:   
                
            # NW
            if board[i-1,j-1] == 'M' or board[i-1,j-1] == 'm':
                count+=1

            # N
            if board[i-1,j] == 'M' or board[i-1,j] == 'm':
                count+=1

            # NE
            if board[i-1,j+1] == 'M' or board[i-1,j+1] == 'm':
                count+=1

            # W
            if board[i,j-1] == 'M' or board[i,j-1] == 'm':
                count+=1

            # E
            if board[i, j+1] == 'M' or board[i, j+1] == 'm':
                count+=1

            # SW
            if board[i+1,j-1] == 'M' or board[i+1,j-1] == 'm':
                count+=1

            # S
            if board[i+1,j] == 'M' or board[i+1,j] == 'm':
                count+=1
            
            # SE
            if board[i+1,j+1] == 'M' or board[i+1,j+1] == 'm':
                count+=1

    return count


def checks(result, answers, dim):

    for i in range(dim):
            for j in range(dim):

                result = mineSweep(result, dim)

                result = safeSweep(result, answers, dim)

                if result[i,j] == 0:

                    result, moreSafe = exposeSafe(i,j, result, answers, dim)

                    while(moreSafe == True):
                
                        for i in range(dim):
                            for j in range(dim):
                                if result[i,j] == 0:

                                    #print((i, j))
                                    result, moreSafe = exposeSafe(i,j, result, answers, dim)

    return result

def guessCheck(boardCopy, constraints):

    consLen = len(constraints)

    equations = []

    for i in range(consLen):

        constraintKey = list(constraints.keys())[i]

        keyList = constraints.get(constraintKey)

        hint = boardCopy[constraintKey]

        surroundingM = surroundingMines(boardCopy, constraintKey)

        hint = hint - surroundingM

        keyListLen = len(keyList)

        equations.append((keyList,hint))

        #print(keyList," = ", hint)
        #print()


    return equations


def listDifference(l1, l2):
    
    return (list(list(set(l1) - set(l2)) + list(set(l2) - set (l1))))


def equationIterate(equations, result, answers):

    eqLen = len(equations)

    safeTuplesList = []

    for i in range(eqLen):

        for j in range(eqLen):

            if i != j:

                primaryList = equations[i][0]
                primaryHint = equations[i][1]
                comparedList = equations[j][0]
                comparedHint = equations[j][1]

                listDiff = listDifference(primaryList, comparedList)

                if len(listDiff) == 1:
                    
                    if primaryHint - comparedHint == 0:
                        
                        result[listDiff[0]] = answers[listDiff[0]]

                    if primaryHint - comparedHint == 1:

                        result[listDiff[0]] = 'M'

    

    return result


def advSearch(minesweeper, dim):
    
    result = board(dim)

    # fill in cells as unknown
    for i in range(dim):
        for j in range(dim):
            result[i,j] = '-'


    hiddenCells = True

    x = random.randint(0,dim-1)
    y = random.randint(0,dim-1)

    mineHitList = []

    #print(x, y)

    while (hiddenCells is True):
    #if 1 == 1:

        hint = minesweeper[x,y]

        print()
        print("Clicked on cell - ", 'x: ' + str(y), 'y: ' + str(x), 'hint: ' + str(hint))

        result[x,y] = minesweeper[x,y]

        if hint == 'M':
            print("******CLICKED A MINE******")
            result[y,x] = 'm'
            mineHitList.append((y,x))
            print('Agent knowledge updated!\n')

        if hint == 0:

            moreSafe = True

            while(moreSafe == True):
                
                for i in range(dim):
                    for j in range(dim):
                        if result[i,j] == 0:
                            #print((i, j))
                            result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)
                            
        copyboard = result

        for i in range(dim):
            for j in range(dim):

                result = mineSweep(result, dim)

                result = safeSweep(result, minesweeper, dim)

                if result[i,j] == 0:

                    result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)

                    while(moreSafe == True):
                
                        for i in range(dim):
                            for j in range(dim):
                                if result[i,j] == 0:

                                    #print((i, j))
                                    result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)
                                    
        boardChange = True

        while(boardChange == True):

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

            oldResult = result

            result = equationIterate(eqs, result, minesweeper)

            result = checks(result, minesweeper, dim)

            if oldResult.all() == result.all():
                boardChange = False


        hiddenCells, hidden = hiddenScan(result, dim)

        if hiddenCells == True:

            randomCell = random.choice(hidden)

            x = randomCell[0]
            y = randomCell[1]


        print()
        printAdvBoard(result)

    print("Agent hit mines at: ", mineHitList)
    print("Total mines clicked: " + str(len(mineHitList)))

    return result, len(mineHitList)
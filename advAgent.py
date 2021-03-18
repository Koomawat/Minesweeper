from createboard import *
from mineRevealer import *
from safeHiddenRevealer import *
import random
from more_termcolor.colors import brightred, brightgreen, brightyellow, brightblue, brightmagenta, brightcyan

def printAdvBoard(board):

    for i in range(len(board)):
        row = ""
        for j in range(len(board)):
            current = str(board[i,j])
            if (current) == 'M':
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


def constraintsCheck(boardLen, board):

    constraints = {(i,j) :
    [] for i in range(boardLen)
            for j in range(boardLen)
                if (board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8))}

    for i,j in constraints.keys():
        
        if i == 0 and j == 0:

            if board[i+1,j+1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i+1,j+1))
                    
            if board[i+1,j] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i+1,j))

            if board[i, j+1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i,j+1))

        elif i == boardLen-1 and j == 0:

            if board[i-1,j+1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i-1,j+1))

            if board[i-1,j] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i-1,j))

            if board[i, j+1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
               constraints[(i,j)].append((i,j+1))

        elif i == 0 and j == boardLen-1:

            if board[i+1,j-1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i+1,j-1))

            if board[i+1,j] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i+1,j))

            if board[i,j-1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i,j-1))

        elif i == boardLen-1 and j == boardLen-1:

            if board[i-1,j-1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i-1,j-1))

            if board[i-1,j] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i-1,j))

            if board[i,j-1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i,j-1))

        elif i == 0 and j != 0 and j != boardLen-1:

            if board[i,j-1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i,j-1))

            if board[i, j+1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i,j+1))

            if board[i+1,j] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i+1,j))

            if board[i+1,j-1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i+1,j-1))

            if board[i+1,j+1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i+1,j+1))

        elif i != 0 and i != boardLen-1 and j == 0:

            if board[i, j+1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i,j+1))

            if board[i+1,j] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i+1,j))

            if board[i+1,j+1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i+1,j+1))

            if board[i-1,j] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i-1,j))

            if board[i-1,j+1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i-1,j+1))

        elif i != 0 and i != boardLen-1 and j == boardLen-1:

            if board[i,j-1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i,j-1))

            if board[i+1,j] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i+1,j))

            if board[i+1,j-1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i+1,j-1))

            if board[i-1,j] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i-1,j))

            if board[i-1,j-1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i-1,j-1))

        elif i == boardLen-1 and j != 0 and j != boardLen-1:

            if board[i-1,j] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i-1,j))

            if board[i-1,j-1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i-1,j-1))

            if board[i-1,j+1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i-1,j+1))

            if board[i,j-1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i,j-1))

            if board[i, j+1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i,j+1))

        else:   
                
            if board[i-1,j] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i-1,j))

            if board[i-1,j-1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i-1,j-1))

            if board[i-1,j+1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i-1,j+1))

            if board[i+1,j] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i+1,j))

            if board[i+1,j-1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i+1,j-1))

            if board[i+1,j+1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i+1,j+1))

            if board[i,j-1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i,j-1))

            if board[i, j+1] == '-' and board[i,j] == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
                constraints[(i,j)].append((i,j+1))
    
    return constraints



def topLeft(i,j, board, minesweeper, boardLen, visitedSet):

    moreSafe = False

    # South East
    board[i+1,j+1] = minesweeper[i+1,j+1]
    if board[i+1,j+1] == 0 and (i+1,j+1) not in visitedSet:
        moreSafe = True
            
    # South
    board[i+1,j] = minesweeper[i+1,j]
    if board[i+1,j] == 0 and (i+1,j) not in visitedSet:
        moreSafe = True

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0 and (i,j+1) not in visitedSet:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe


def topRight(i,j, board, minesweeper, boardLen, visitedSet):

    moreSafe = False

    # South West 
    board[i+1,j-1] = minesweeper[i+1,j-1]
    if board[i+1,j-1] == 0 and (i+1,j-1) not in visitedSet:
        moreSafe = True

    # South
    board[i+1, j] = minesweeper[i+1, j]
    if board[i+1,j] == 0 and (i+1,j) not in visitedSet:
        moreSafe = True

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0 and (i,j-1) not in visitedSet:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe


def botLeft(i,j, board, minesweeper, boardLen, visitedSet):

    moreSafe = False

    # North East
    board[i-1,j+1] = minesweeper[i-1,j+1]
    if board[i-1,j+1] == 0 and (i-1,j+1) not in visitedSet:
        moreSafe = True

    # North
    board[i-1,j] = minesweeper[i-1,j]
    if board[i-1,j] == 0 and (i-1,j) not in visitedSet:
        moreSafe = True

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0 and (i,j+1) not in visitedSet:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe


def botRight(i,j, board, minesweeper, boardLen, visitedSet):

    moreSafe = False

    # North West 
    board[i-1,j-1] = minesweeper[i-1,j-1]
    if board[i-1,j-1] == 0 and (i-1,j-1) not in visitedSet:
        moreSafe = True

    # North
    board[i-1, j] = minesweeper[i-1, j]
    if board[i-1,j] == 0 and (i-1,j) not in visitedSet:
        moreSafe = True

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0 and (i,j-1) not in visitedSet:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe


def topEdge(i,j, board, minesweeper, boardLen, visitedSet):

    moreSafe = False

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0 and (i,j-1) not in visitedSet:
        moreSafe = True

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0 and (i,j+1) not in visitedSet:
        moreSafe = True

    # South
    board[i+1, j] = minesweeper[i+1, j]
    if board[i+1,j] == 0 and (i+1,j) not in visitedSet:
        moreSafe = True

    # South West 
    board[i+1,j-1] = minesweeper[i+1,j-1]
    if board[i+1,j-1] == 0 and (i+1,j-1) not in visitedSet:
        moreSafe = True

    # South East
    board[i+1,j+1] = minesweeper[i+1,j+1]
    if board[i+1,j+1] == 0 and (i+1,j+1) not in visitedSet:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe
    

def leftEdge(i,j, board, minesweeper, boardLen, visitedSet):

    moreSafe = False

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0 and (i,j+1) not in visitedSet:
        moreSafe = True

    # South
    board[i+1, j] = minesweeper[i+1, j]
    if board[i+1,j] == 0 and (i+1,j) not in visitedSet:
        moreSafe = True

    # South East
    board[i+1,j+1] = minesweeper[i+1,j+1]
    if board[i+1,j+1] == 0 and (i+1,j+1) not in visitedSet:
        moreSafe = True

    # North
    board[i-1, j] = minesweeper[i-1, j]
    if board[i-1,j] == 0 and (i-1,j) not in visitedSet:
        moreSafe = True

    # North East
    board[i-1,j+1] = minesweeper[i-1,j+1]
    if board[i-1,j+1] == 0 and (i-1,j+1) not in visitedSet:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe


def rightEdge(i,j, board, minesweeper, boardLen, visitedSet):

    moreSafe = False

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0 and (i,j-1) not in visitedSet:
        moreSafe = True

    # South
    board[i+1, j] = minesweeper[i+1, j]
    if board[i+1,j] == 0 and (i+1,j) not in visitedSet:
        moreSafe = True

    # South West 
    board[i+1,j-1] = minesweeper[i+1,j-1]
    if board[i+1,j-1] == 0 and (i+1,j-1) not in visitedSet:
        moreSafe = True

    # North
    board[i-1, j] = minesweeper[i-1, j]
    if board[i-1,j] == 0 and (i-1,j) not in visitedSet:
        moreSafe = True

    # North West 
    board[i-1,j-1] = minesweeper[i-1,j-1]
    if board[i-1,j-1] == 0 and (i-1,j-1) not in visitedSet:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe


def botEdge(i,j, board, minesweeper, boardLen, visitedSet):

    moreSafe = False

    # North
    board[i-1, j] = minesweeper[i-1, j]
    if board[i-1,j] == 0 and (i-1,j) not in visitedSet:
        moreSafe = True

    # North West 
    board[i-1,j-1] = minesweeper[i-1,j-1]
    if board[i-1,j-1] == 0 and (i-1,j-1) not in visitedSet:
        moreSafe = True
    
    # North East
    board[i-1,j+1] = minesweeper[i-1,j+1]
    if board[i-1,j+1] == 0 and (i-1,j+1) not in visitedSet:
        moreSafe = True

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0 and (i,j-1) not in visitedSet:
        moreSafe = True

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0 and (i,j+1) not in visitedSet:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe


def middle(i,j, board, minesweeper, boardLen, visitedSet):
    
    moreSafe = False

    # North
    board[i-1, j] = minesweeper[i-1, j]
    if board[i-1,j] == 0 and (i-1,j) not in visitedSet:
        moreSafe = True

    # North West 
    board[i-1,j-1] = minesweeper[i-1,j-1]
    if board[i-1,j-1] == 0 and (i-1,j-1) not in visitedSet:
        moreSafe = True

    # North East
    board[i-1,j+1] = minesweeper[i-1,j+1]
    if board[i-1,j+1] == 0 and (i-1,j+1) not in visitedSet:
        moreSafe = True

    # South
    board[i+1, j] = minesweeper[i+1, j]
    if board[i+1,j] == 0 and (i+1,j) not in visitedSet:
        moreSafe = True

    # South West 
    board[i+1,j-1] = minesweeper[i+1,j-1]
    if board[i+1,j-1] == 0 and (i+1,j-1) not in visitedSet:
        moreSafe = True

    # South East
    board[i+1,j+1] = minesweeper[i+1,j+1]
    if board[i+1,j+1] == 0 and (i+1,j+1) not in visitedSet:
        moreSafe = True

    # West
    board[i,j-1] = minesweeper[i,j-1]
    if board[i,j-1] == 0 and (i,j-1) not in visitedSet:
        moreSafe = True

    # East
    board[i, j+1] = minesweeper[i, j+1]
    if board[i, j+1] == 0 and (i,j+1) not in visitedSet:
        moreSafe = True

    moreSafe = safeCheck(boardLen, board)

    return board, moreSafe


def exposeSafe(i,j, result, minesweeper, dim, visitedSet):

    boardCopy = result

    compare = minesweeper

    boardLen = dim

    moreSafe = True

    if i == 0 and j == 0:

        boardCopy, moreSafe = topLeft(i,j, boardCopy, minesweeper, boardLen, visitedSet)

    elif i == boardLen-1 and j == 0:

        boardCopy, moreSafe = botLeft(i,j, boardCopy, minesweeper, boardLen, visitedSet)

    elif i == 0 and j == boardLen-1:

        boardCopy, moreSafe = topRight(i,j, boardCopy, minesweeper, boardLen, visitedSet)

    elif i == boardLen-1 and j == boardLen-1:

        boardCopy, moreSafe = botRight(i,j, boardCopy, minesweeper, boardLen, visitedSet)

    elif i == 0 and j != 0 and j != boardLen-1:

        boardCopy, moreSafe = topEdge(i,j, boardCopy, minesweeper, boardLen, visitedSet)

    elif i != 0 and i != boardLen-1 and j == 0:

        boardCopy, moreSafe = leftEdge(i,j, boardCopy, minesweeper, boardLen, visitedSet)

    elif i != 0 and i != boardLen-1 and j == boardLen-1:

        boardCopy, moreSafe = rightEdge(i,j, boardCopy, minesweeper, boardLen, visitedSet)

    elif i == boardLen-1 and j != 0 and j != boardLen-1:

        boardCopy, moreSafe = botEdge(i,j, boardCopy, minesweeper, boardLen, visitedSet)

    else:   
        boardCopy, moreSafe = middle(i,j, boardCopy, minesweeper, boardLen, visitedSet)

    return boardCopy, moreSafe


def advSearch(minesweeper, dim):

    result = board(dim)

    for i in range(dim):
        for j in range(dim):
            result[i,j] = '-'


    hiddenCells = True

    x = random.randint(0,dim-1)
    y = random.randint(0,dim-1)

    mineHits = 0

    #print(x, y)

    visitedSet = set()

    #while (hiddenCells is True):
    if 1 == 1:

        hint = minesweeper[x,y]

        print()
        print("Clicked on cell", x, y)

        result[x,y] = minesweeper[x,y]

        if result[x,y] == 'M':
            mineHits += 1

        if hint == 0:

            moreSafe = True

            

            while(moreSafe == True):
                
                for i in range(dim):
                    for j in range(dim):
                        if result[i,j] == 0 and ((i,j) not in visitedSet):
                            visitedSet.add((i,j))
                            #print((i, j))
                            result, moreSafe = exposeSafe(i,j, result, minesweeper, dim, visitedSet)
                            
        
        consDict = constraintsCheck(dim, result)

        print(consDict)
        print()

        #hiddenCells, hidden = hiddenScan(result, dim)


        #if hiddenCells == True:

            #randomCell = random.choice(hidden)

            #x = randomCell[0]
            #y = randomCell[1]


        
        printAdvBoard(result)

    return result, mineHits
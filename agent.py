from createboard import *
from mineRevealer import *
from safeHiddenRevealer import *
import random
from more_termcolor.colors import brightred, brightgreen, brightyellow, brightblue, brightmagenta, brightcyan

def printBoard(board):

    n = len(board)
    print(" "*(len(str(n))+1), end='')
    for i in range(n):
        if i >= 10:
            i = i-(10*(int(i/10)))
        print(str(i) + "  ", end='')
    print()

    for i in range(n):
        row = ""
        print(str(i).zfill(len(str(n))) + "|", end='')
        for j in range(n):
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


def exposeSafe(i,j, result, minesweeper, dim, visitedSet):

    boardCopy = result
    
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


def search(minesweeper, dim):

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

    while (hiddenCells is True):


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
                        if result[i,j] == 0:

                            #print((i, j))
                            result, moreSafe = exposeSafe(i,j, result, minesweeper, dim, visitedSet)

            


        for i in range(dim):
            for j in range(dim):

                result = mineSweep(result, dim)

                result = safeSweep(result, minesweeper, dim)

                if result[i,j] == 0:

                    result, moreSafe = exposeSafe(i,j, result, minesweeper, dim, visitedSet)

                    while(moreSafe == True):
                
                        for i in range(dim):
                            for j in range(dim):
                                if result[i,j] == 0:

                                    #print((i, j))
                                    result, moreSafe = exposeSafe(i,j, result, minesweeper, dim, visitedSet)

                
            
        
        hiddenCells, hidden = hiddenScan(result, dim)

        if hiddenCells == True:

            randomCell = random.choice(hidden)

            x = randomCell[0]
            y = randomCell[1]


        printBoard(result)

        
    return result, mineHits
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
    surroundingCoords = [(x,y) for x in range(-1,2) 
                            for y in range(-1,2)]
        # creates coordinates to add onto x,y coordinates:
        # [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for i in range(boardLen):
        for j in range(boardLen):
            a, b = i, j # reset to next iteration of i, j
            for x, y in surroundingCoords:
                if (abs(x)==1 and abs(y)==1):
                    continue

                a += x
                b += y

                if (0 <= a < boardLen) and (0 <= b < boardLen) and (str(board[a,b]) == '-') and (str(board[i,j]) == '0'):
                    moreSafe = True
                    break

    return moreSafe

###############################################################

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

###############################################################

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

    # boardCopy = result
    # moreSafe = True

    # # Check if agent is at the top of the board
    # if i == 0:
    #     if j == 0: # top left corner
    #         boardCopy, moreSafe = topLeft(i,j, boardCopy, minesweeper, boardLen)
    #     elif j == boardLen-1: # top right corner
    #         boardCopy, moreSafe = topRight(i,j, boardCopy, minesweeper, boardLen)
    #     elif j != 0 and j != boardLen-1: # top, but not in the corner
    #         boardCopy, moreSafe = topEdge(i,j, boardCopy, minesweeper, boardLen)

    # # Check if agent is at the bottom of the board
    # elif i == boardLen-1:
    #     if j == 0: # bottom left corner
    #         boardCopy, moreSafe = botLeft(i,j, boardCopy, minesweeper, boardLen)
    #     elif j == boardLen-1: # bottom right corner
    #         boardCopy, moreSafe = botRight(i,j, boardCopy, minesweeper, boardLen)
    #     elif j != 0 and j != boardLen-1: # bottom, but not in the corner
    #         boardCopy, moreSafe = botEdge(i,j, boardCopy, minesweeper, boardLen)

    # # Check if agent is on left/right border of the board
    # elif i != 0 and i != boardLen-1: 
    #     if j == 0: # at the left border
    #         boardCopy, moreSafe = leftEdge(i,j, boardCopy, minesweeper, boardLen)
    #     elif j == boardLen-1: # at the right border
    #         boardCopy, moreSafe = rightEdge(i,j, boardCopy, minesweeper, boardLen)


    # # The agent is not on the border
    # else:   
    #     boardCopy, moreSafe = middle(i,j, boardCopy, minesweeper, boardLen)

    # return boardCopy, moreSafe


def search(minesweeper, dim):

    result = board(dim)

    for i in range(dim):
        for j in range(dim):
            result[i,j] = '-'

    mineHitList = []

    hiddenCells = True
    rowUnrevealCheck = False
    while (hiddenCells):
        resultList = result.tolist()

        x = random.randint(0,dim-1)
        y = random.randint(0,dim-1)

        if rowUnrevealCheck:
            for a in range(dim):
                if '-' in resultList[a]:
                    x = a
                    y = resultList[a].index('-')
        print(y, x)
        
        hint = minesweeper[x,y]

        # Avoid clicking already-exploded mine again
        if (x,y) in mineHitList:
            # print('Agent already knows that there is a mine at ', 'x: ' + str(y), 'y: ' + str(x), '... SKIP')
            continue


        # Avoid going through revealed cells
        # print('result[x,y]: ' + str(result[x,y]))
        if result[x,y] != '-':
            rowUnrevealCheck = True
            # print(hint)
            # print('Skipping revealed cell')
            continue


        print("Clicked on cell - ", 'x: ' + str(y), 'y: ' + str(x), 'hint: ' + str(hint))


        # If clicked on mine, append in mineHitList to update the knowledge of the agent
        if str(hint) == 'M':
            print("******CLICKED A MINE******")
            result[x,y] = 'm'
            mineHitList.append((x,y))
            print('Agent knowledge updated!\n')
            continue

        result[x,y] = hint

        # Expand neighboring/adjacent safe cells once a safe cell is clicked
        if str(hint) == '0': 

            print("Safe cell 0 clicked, expanding adjacent 0 cells.")
            
            moreSafe = True
            # result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)

            while moreSafe:
                for i in range(dim):
                    for j in range(dim):
                        if moreSafe == True:
                            if result[i,j] == 0:
                                print((i, j))
                                result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)
                                printBoard(result)


        printBoard(result)
        print()


        for i in range(dim):
            # print('i: ' + str(i))
            for j in range(dim):
                # print('j: ' + str(j))

                result = mineSweep(result, dim)

                # print('After minesweep: ')
                # printBoard(result)
                # print()

                result = safeSweep(result, minesweeper, dim)
                # print('After safesweep: ')
                # printBoard(result)
                # print()


                if result[i,j] == 0:

                    result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)
                    
                    while moreSafe:
                        for i in range(dim):
                            for j in range(dim):
                                if (moreSafe == True):
                                    if result[i,j] == 0:
                                        result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)
        
        print('After mine/safe sweeper')
        printBoard(result)
        print()
            
        
        hiddenCells, hidden = hiddenScan(result, dim)
        
        if hiddenCells == True:
            randomCell = random.choice(hidden)

            x = randomCell[0]
            y = randomCell[1]


    printBoard(result)
    print()

    print()
    print("Agent hit mines at: ", mineHitList)
    print("Total mines clicked: " + str(len(mineHitList)))

    return result, len(mineHitList)
from createboard import *
from mineRevealer import *
from safeHiddenRevealer import *
import random, copy
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


# Bsic search function that updates the status as it traverse through the board
def search(minesweeper, dim):

    # Fill in cells as unknown
    result = board(dim)
    for i in range(dim):
        for j in range(dim):
            result[i,j] = '-'


    # Initially sets the random x,y coordinate to reveal.
    # After the initial hit, the next coordinate will always be from unrevealed cells as it updates hidden cell lists.
    x = random.randint(0,dim-1)
    y = random.randint(0,dim-1)
    #print(x, y)

    # The coordinates of exploded mines taht the agent hit.
    mineHitList = []

    # While there are unrevealed cells, repeat until all cells are revealed.
    hiddenCells = True
    while hiddenCells:
        # The x,y coordinates to hit next unrevealed cell is randomly chosen  before looping.

        # The content that the agent clicked on
        hint = minesweeper[x,y]

        # Reveal the content on the board
        result[x,y] = minesweeper[x,y]
        # print(f"Clicked on cell\t\tx: {str(y)},\ty: {str(x)},\thint: {str(hint)}")

        # If the agent hit the unrevealed mine, update exploded mine list
        if hint == 'M':
            # print("******CLICKED A MINE******")
            result[x,y] = 'm'
            mineHitList.append((x,y))
            # printBoard(result)

        # If the agent hits 0, expand until it encounters either the border or a non-zero number.
        elif hint == 0:

            # print("Safe cell 0 clicked, exposing adjacent 0 cells.")
            # print('\nBefore exposing:')
            # printBoard(result)

            # If we can expand on adjacent 0's, expand as much as possible
            moreSafe = True
            while moreSafe:
                for i in range(dim):
                    for j in range(dim):
                        if result[i,j] == 0:
                            #print((i, j))
                            result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)

            # print('\nAfter exposing:')
            # printBoard(result)

            # Flag potential mines                
            result = mineSweep(result, dim)
            # Show neighbors around the mines
            result = safeSweep(result, minesweeper, dim)

        # print('=======================================================')

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

                    # For each cell, reveal mines and safe cells around them
                    result = mineSweep(result, dim)
                    result = sweeped = safeSweep(result, minesweeper, dim)

                    # Only print the result if there is a difference
                    if not compareBoards(expanded, sweeped):
                        print()
                        # print('After sweeps: ')
                        # printBoard(sweeped)

                    expanded = result
                    # If the current cell is 0, expand through its adjacent 0's
                    if result[i,j] == 0:
                        result = mineSweep(result, dim)
                        result = sweeped = safeSweep(result, minesweeper, dim)
                        result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)

                        # If we can expand on the adjacent 0's more, expand as much as possible
                        while moreSafe:
                            for i in range(dim):
                                for j in range(dim):
                                    if result[i,j] == 0:
                                        expanded, moreSafe = exposeSafe(i,j, result, minesweeper, dim)
                                        result = expanded

                            # print('After expansion loops:')
                            # printBoard(result)

                    # Only print hte result if there is a difference
                    if not compareBoards(expanded, sweeped):
                        print()
                        # print('After expansion:')
                        # printBoard(result)

        # Check to see if there are hidden cells still remaining to reveal
        # If there are no more hidden cells, then break out.
        hiddenCells, hidden = hiddenScan(result, dim)
        if hiddenCells == True:
            randomCell = random.choice(hidden)
            x = randomCell[0]
            y = randomCell[1]

        # print('Updated before click: ')
        # printBoard(result)
        # print('******************************************************')
        # print('******************************************************')
        # print('******************************************************')

    # print("Agent hit mines at: ", mineHitList)
    # print("Total mines clicked: " + str(len(mineHitList)))

    return result, len(mineHitList)
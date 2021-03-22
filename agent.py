
# from proj2.createboard import compareBoards
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


# def safeCheck(boardLen, board):

#     surroundingCoords = [(x,y) for x in range(-1,2) 
#                             for y in range(-1,2)]
#         # creates coordinates to add onto x,y coordinates:
#         # [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


#     for i in range(boardLen):
#         for j in range(boardLen):

#             if str(board[i,j]) != '0':
#                 continue
                
#             for x, y in surroundingCoords:
#                 a, b = i, j # reset to next iteration of i, j
#                 a += x
#                 b += y

#                 if (a < 0) or (boardLen <= a) or (b < 0) or (boardLen <= b):
#                     continue
#                 if (abs(x) == 1) and (abs(y) == 1):
#                     continue

#                 if board[a,b] == '-':
#                     return True

# def exposeSafe(i,j, boardCopy, minesweeper, boardLen):

#     moreSafe = True

#     surroundingCoords = [(x,y) for x in range(-1,2) 
#                             for y in range(-1,2)]
#         # creates coordinates to add onto x,y coordinates:
#         # [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
#     # if (0,0) in surroundingCoords:
#     #     surroundingCoords.remove((0,0))

#     for x, y in surroundingCoords:
#         a, b = i, j # reset to next iteration of i, j
#         a += x
#         b += y

#         if (a < 0) or (boardLen <= a) or (b < 0) or (boardLen <= b):
#             continue

#         boardCopy[a,b] = minesweeper[a,b]
#         moreSafe = safeCheck(boardLen, boardCopy)

#     return boardCopy, moreSafe

def search(minesweeper, dim):

    result = board(dim)
    for i in range(dim):
        for j in range(dim):
            result[i,j] = '-'

    # Initially sets the random x,y coordinate to reveal.
    # After the initial hit, the next coordinate will always be from unrevealed cells as it updates hidden cell lists.
    x = random.randint(0,dim-1)
    y = random.randint(0,dim-1)
    #print(x, y)

    mineHitList = []

    hiddenCells = True
    while hiddenCells:
        # The x,y coordinates to hit next unrevealed cell is randomly chosen  before looping.

        # The content that the agent clicked on
        hint = minesweeper[x,y]

        # Reveal the content on the board
        result[x,y] = minesweeper[x,y]
        print(f"Clicked on cell\t\tx: {str(y)},\ty: {str(x)},\thint: {str(hint)}")

        # If the agent hit the unrevealed mine, update exploded mine list
        if hint == 'M':
            print("******CLICKED A MINE******\n")
            result[x,y] = 'm'
            mineHitList.append((x,y))
            printBoard(result)

        # If the agent hits 0, expand until it encounters either the border or a non-zero number.
        elif hint == 0:

            print("Safe cell 0 clicked, exposing adjacent 0 cells.")
            print('\nBefore exposing:')
            printBoard(result)

            moreSafe = True
            while moreSafe:
                for i in range(dim):
                    for j in range(dim):
                        if result[i,j] == 0:
                            result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)

            print('\nAfter exposing:')
            printBoard(result)

        print('=======================================================')

        sweeped, mineSweeped, expanded, before, after = None, None, None, result, None    
        afterExpandedSame = False
        # Update neighboring cells, expand as needed.
        # moreSafe = result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)
        # while moreSafe:
        for i in range(dim):
            for j in range(dim):

                hiddenCells, hidden = hiddenScan(result, dim)
                if not hiddenCells:
                    break

                if result[i,j] == 0:

                    # print(i,j)

                    print('---------------------------------------------')

                    sameResult = compareBoards(before, after)
                    if sameResult and afterExpandedSame:
                        print('Before and after two sweeps are same')
                        # printBoard(result)
                        continue

                    mineSweeped = mineSweep(result, dim)
                    print('\nMine sweeped:')
                    printBoard(mineSweeped)

                    before = safeSweep(mineSweeped, minesweeper, dim)
                    after = safeSweep(before, minesweeper, dim)
                    print('\nSafe sweeped:')
                    printBoard(after)

                    
                    
                    result = expanded = after
                    

                    sameResult = compareBoards(before, after)
                    if sameResult and afterExpandedSame:
                        print('Before and after two sweeps are same')
                        printBoard(result)
                        result = sweeped = expanded = after
                        continue
                    else:
                        while sameResult is False:

                            hiddenCells, hidden = hiddenScan(result, dim)
                            if not hiddenCells:
                                break

                            print('---------------------------------------------')

                            mineSweeped = mineSweep(after, dim)
                            print('\nMine sweeped again:')
                            printBoard(mineSweeped)

                            before = safeSweep(mineSweeped, minesweeper, dim)
                            # print('\nSafe sweeped again before:')
                            # printBoard(before)

                            after = safeSweep(before, minesweeper, dim)
                            # print('\nSafe sweeped again after:')
                            # printBoard(after)
                            # print('---------------------------------------------')

                            sameResult = compareBoards(before, after)
                            print(sameResult)

                        result = sweeped = expanded = after
                        print('\nSafe sweeped again final:')
                        printBoard(after)
                        print('---------------------------------------------')
                    
                    # print('---------------------------------------------')
                    
                    sameResult = False
                    moreSafe = True
                    while moreSafe:

                        for i in range(dim):
                            for j in range(dim):

                                if result[i,j] == 0:
                                    after = expanded
                                    expanded, moreSafe = exposeSafe(i,j, after, minesweeper, dim)
                                    
                                    hiddenCells, hidden = hiddenScan(result, dim)
                                    if not hiddenCells:
                                        break

                                    # if expanded is not None:
                                    #     afterExpandedSame = compareBoards(expanded, after)
                                    #     if afterExpandedSame:
                                    #         print('the after is same as previous expanded')
                                    #         printBoard(expanded)
                                    #         printBoard(after)
                                    #         break
                            
                        #     if afterExpandedSame:
                        #         break

                        # if afterExpandedSame:
                        #     break
                

                    result = expanded
                    
                    if expanded is not None:
                        afterExpandedSame = compareBoards(expanded, after)
                        if afterExpandedSame:
                            print('the after is same as previous expanded2')
                            printBoard(expanded)
                            break

                    
                    sameResult = compareBoards(expanded, after)
                    if sameResult:
                        print("Tried to expand 0's, but no improvement could be made.")
                        printBoard(expanded)
                        print('---------------------------------------------')
                        result = expanded
                        continue
                    
                    else:
                        print("Expanded: ")
                        printBoard(expanded)
                        result = expanded 
                        continue

                    
                sweepedSame = compareBoards(expanded, sweeped)
                if sweepedSame and expanded is not None:
                    print('expanded and sweeped same')
                    print('---------------------------------------------')
                    # printBoard(expanded)
                    break
            
            if sweepedSame:
                continue

            if afterExpandedSame:
                continue
            # if sameResult and expanded is not None:
            #     break
                # expanded, moreSafe = exposeSafe(i,j, sweeped, minesweeper, dim)
                # sameResult = compareBoards(sweeped, expanded)
                # if sameResult:
                #     break
        # if sweepedSame:
        #     break

                    
                    
        

        
        # print('\bExpanded:')
        # printBoard(result)


        hiddenCells, hidden = hiddenScan(result, dim)
        if hiddenCells == True:
            randomCell = random.choice(hidden)
            x = randomCell[0]
            y = randomCell[1]

        # print('Before looping:')
        # printBoard(result)

    print("Agent hit mines at: ", mineHitList)
    print("Total mines clicked: " + str(len(mineHitList)))

    return result, len(mineHitList)
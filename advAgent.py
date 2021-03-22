from agent import printBoard
from createboard import *
from mineRevealer import *
from safeHiddenRevealer import *
import random
from more_termcolor.colors import brightred, brightgreen, brightyellow, brightblue, brightmagenta, brightcyan
import copy

# Printing function to print out the minesweeper board on the terminal
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

# Constraints function which appends hidden neighbors of hints next to a hidden cell 
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

# Advanced hidden scan selection that chooses a random cell next to hints instead of completely randomly
def advHiddenScan(board, dim):

    hidden = False

    hiddenList = []

    boardLen = dim

    for i in range(boardLen):

        for j in range(boardLen):
        
            if i == 0 and j == 0:

                # E
                if board[i, j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i,j+1))
                    hidden = True

                # S     
                if board[i+1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i+1,j))
                    hidden = True

                # SE
                if board[i+1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i+1,j+1))
                    hidden = True

            elif i == boardLen-1 and j == 0:

                # N
                if board[i-1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i-1,j))
                    hidden = True

                # NE
                if board[i-1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i-1,j+1))
                    hidden = True

                # E
                if board[i, j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i,j+1))
                    hidden = True

            elif i == 0 and j == boardLen-1:

                # W
                if board[i,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i,j-1))
                    hidden = True

                # SW
                if board[i+1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i+1,j-1))
                    hidden = True

                # S
                if board[i+1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i+1,j))
                    hidden = True

            elif i == boardLen-1 and j == boardLen-1:

                # NW
                if board[i-1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i-1,j-1))
                    hidden = True

                # N
                if board[i-1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i-1,j))
                    hidden = True

                # W
                if board[i,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i,j-1))
                    hidden = True

            elif i == 0 and j != 0 and j != boardLen-1:

                # W
                if board[i,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i,j-1))
                    hidden = True

                # E
                if board[i, j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i,j+1))
                    hidden = True

                # SW
                if board[i+1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i+1,j-1))
                    hidden = True

                # S
                if board[i+1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i+1,j))
                    hidden = True

                # SE
                if board[i+1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i+1,j+1))
                    hidden = True

            elif i != 0 and i != boardLen-1 and j == 0:

                # N
                if board[i-1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i-1,j))
                    hidden = True

                # NE
                if board[i-1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i-1,j+1))
                    hidden = True

                # E
                if board[i, j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i,j+1))
                    hidden = True

                # S
                if board[i+1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i+1,j))
                    hidden = True

                # SE
                if board[i+1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i+1,j+1))
                    hidden = True

            elif i != 0 and i != boardLen-1 and j == boardLen-1:

                # NW
                if board[i-1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i-1,j-1))
                    hidden = True

                # N
                if board[i-1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i-1,j))
                    hidden = True

                # W
                if board[i,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i,j-1))
                    hidden = True

                # SW
                if board[i+1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i+1,j-1))
                    hidden = True

                # S
                if board[i+1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i+1,j))
                    hidden = True

            elif i == boardLen-1 and j != 0 and j != boardLen-1:

                # NW
                if board[i-1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i-1,j-1))
                    hidden = True

                # N
                if board[i-1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i-1,j))
                    hidden = True

                # NE
                if board[i-1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i-1,j+1))
                    hidden = True

                # W
                if board[i,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i,j-1))
                    hidden = True

                # E
                if board[i, j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i,j+1))
                    hidden = True

            else:   
                    
                # NW
                if board[i-1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i-1,j-1))
                    hidden = True

                # N
                if board[i-1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i-1,j))
                    hidden = True

                # NE
                if board[i-1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i-1,j+1))
                    hidden = True

                # W
                if board[i,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i,j-1))
                    hidden = True

                # E
                if board[i, j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i,j+1))
                    hidden = True

                # SW
                if board[i+1,j-1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i+1,j-1))
                    hidden = True

                # S
                if board[i+1,j] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i+1,j))
                    hidden = True
                
                # SE
                if board[i+1,j+1] == '-' and (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 
                    or board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):
                    hiddenList.append((i+1,j+1))
                    hidden = True

    

    return hidden, hiddenList

# Surrounding mine function which counts the number of mines a hint already has
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

# Checks function that calls the basic agent's neighbor calculations to get information to add to the knowledge base and exposing safe cells if needed
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

# Constraints calculator function which take in each hint's neighbors as values and creates a formula equal to the number of remaining mines of that hint
def guessCheck(boardCopy, constraints):

    consLen = len(constraints)

    equations = []

    for i in range(consLen):

        # Placing the constraints in a list and then appending them with the relevant hint into a list of tuples e.g. [(variable, hint), (variable2, hint2)...]

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

# Function to get the difference between 2 lists
def listDifference(l1, l2):
    
    return (list(list(set(l1) - set(l2)) + list(set(l2) - set (l1))))

# Equation iterator to go through every equation and make inferences with the given equations
def equationIterate(equations, result, answers):

    eqLen = len(equations)

    # Safe tuple list that will be used for the actual knowledge base
    safeTuplesList = []

    madeChanges = True

    # Looping until no more inferences can be made
    while madeChanges == True:

        pastResult = copy.deepcopy(result)

        #print("past")
        #printBoard(pastResult)

    #if 1 == 1:
        #print("looping")
        
        madeChanges = False


        for i in range(eqLen):

            for j in range(eqLen):

                listDiff = []

                # If an equation is only 1 length it means it's either a mine or safe which is determined by the hint it has
                if len(equations[i][0]) == 1:

                    # Hint of 1 means a mine
                    if equations[i][1] == 1:

                        result[equations[i][0][0]] = 'M'

                        safeTuplesList.append((equations[i][0][0],1))

                    # Hint of 0 means safe
                    elif equations[i][1] == 0:   

                        result[equations[i][0][0]] = answers[equations[i][0][0]]

                        safeTuplesList.append((equations[i][0][0],0))

                # Avoiding comparing an equation with it self
                if i != j:

                    primaryList = equations[i][0]
                    primaryHint = equations[i][1]
                    comparedList = equations[j][0]
                    comparedHint = equations[j][1]

                    # Getting the list difference between the current equation and the equation being compared
                    listDiff = listDifference(primaryList, comparedList)

                # If the difference is 1 we can assume based on the hint it's either a mine or safe
                if len(listDiff) == 1:
                        
                        # Hint difference of 0 means the variable not present in both equations is a safe cell tuple
                        if primaryHint - comparedHint == 0:
                            
                            result[listDiff[0]] = answers[listDiff[0]]

                            safeTuplesList.append((listDiff[0],0))

                        # Hint difference of 1 means the variable that was not present must be a mine
                        if primaryHint - comparedHint == 1:

                            result[listDiff[0]] = 'M'

                            safeTuplesList.append((listDiff[0],1))

        tempList = []
        #print(safeTuplesList)

        # Looping through our safe tuples list and changing our previous equations by removing the safe ones
        for i in range(eqLen):

                for j in range(len(safeTuplesList)):

                    tuple1 = safeTuplesList[j][0]
                    tupleList = equations[i][0]

                    truth = str(tuple1) in str(tupleList)

                    if truth == True:
                        
                        newHint = equations[i][1] - safeTuplesList[j][1]

                        newList = equations[i][0]
                        newList.remove(safeTuplesList[j][0])

                        # Updating the equation with the safe variables subtracted which leaves us with new equations to re-iterate through
                        equations[i] = (newList, newHint)
                        #print(equations[i])

        #print(equations)
        
        # If there were changes made we loop through the inference process again, if not we continue in our advanced search
        if (pastResult.all() != result.all()):
            madeChanges = True

        #print("madeChange = ", madeChanges)
        #print("new")
        #printBoard(result)

    return result

# Advanced search function that does the basic checks first then calls the inferences functions
def advSearch(minesweeper, dim):
    
    # Fill in cells as unknown
    result = board(dim)
    for i in range(dim):
        for j in range(dim):
            result[i,j] = '-'

    # Getting a starter random cell to start the game
    x = random.randint(0,dim-1)
    y = random.randint(0,dim-1)
    #print(x, y)

    # Keeping track of when the agent hits a mine 
    mineHitList = []

    # While there are unrevealed cells, repeat until all cells are revealed.
    hiddenCells = True
    while hiddenCells:
        # The x,y coordinates to hit next unrevealed cell is randomly chosen  before looping.

        # Storing the click as a hint
        hint = minesweeper[x,y]

        # Adding the click to our knowledge base
        result[x,y] = minesweeper[x,y]
        print(f"Clicked on cell\t\tx: {str(y)},\ty: {str(x)},\thint: {str(hint)}")

        # If the cell we clicked on was a mine we update our knowledge base
        if hint == 'M':
            print("******CLICKED A MINE******")
            result[x,y] = 'm'
            mineHitList.append((x,y))
            printAdvBoard(result)

        # If the clicked cell was a 0 cell we expose the surrounding safe cells
        elif hint == 0:

            print("Safe cell 0 clicked, exposing adjacent 0 cells.")
            print('\nBefore exposing:')
            printAdvBoard(result)

            # If we can expand on adjacent 0's, expand as much as possible
            moreSafe = True
            while(moreSafe == True):
                for i in range(dim):
                    for j in range(dim):
                        if result[i,j] == 0:
                            #print((i, j))
                            # Calling exposeSafe function to add those safe cells to the knowledge base
                            result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)
                            
            print('\nAfter exposing:')
            printBoard(result)
        
        print('=======================================================')

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

                    # Calling mineSweep and safeSweep (basic agent checks of guaranteed mines or safe cells)
                    result = mineSweep(result, dim)
                    result = sweeped = safeSweep(result, minesweeper, dim)

                    # Only print the result if there is a difference
                    if not compareBoards(expanded, sweeped):
                        print()
                        print('After sweeps: ')
                        printAdvBoard(sweeped)

                    expanded = result
                    # If the current cell is 0, expand through its adjacent 0's
                    if result[i,j] == 0:
                        result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)
                        while moreSafe:
                            for i in range(dim):
                                for j in range(dim):
                                    if result[i,j] == 0:
                                        #print((i, j))
                                        result, moreSafe = exposeSafe(i,j, result, minesweeper, dim)
                            print('After expansion loops:')
                            printAdvBoard(result)

                    # Only print hte result if there is a difference
                    if not compareBoards(expanded, sweeped):
                        print()
                        print('After expansion:')
                        printAdvBoard(result)
        
        print('Before board changes:')
        printAdvBoard(result)
                                    
        boardChange = True
        # Looping through our equations and going through inferences until no more inferences are possible and we need a random cell click in the remaining cells
        while boardChange:
            boardChange = False

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

            oldResult = copy.deepcopy(result)

            result = equationIterate(eqs, result, minesweeper)

            result = checks(result, minesweeper, dim)

            # Keeping track of the old state of the board so we know to keep looping this process until board changes are no longer made
            if oldResult.all() != result.all():
                boardChange = True

        print('After board changes:')
        printAdvBoard(result)
        
        # Scanning for remaining hidden cells to click our next random cell
        hiddenCells, hidden = advHiddenScan(result, dim)
        if hiddenCells == False:
            hiddenCells, hidden = hiddenScan(result, dim)

        if hiddenCells == True:
            randomCell = random.choice(hidden)
            x = randomCell[0]
            y = randomCell[1]

        print('Updated before click: ')
        printAdvBoard(result)
        print('******************************************************')
        print('******************************************************')
        print('******************************************************')

    print("Agent hit mines at: ", mineHitList)
    print("Total mines clicked: " + str(len(mineHitList)))

    return result, len(mineHitList)
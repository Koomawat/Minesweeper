# If for a given cell, the total number of mines - the number of revealed mines = the number of hidden neighbours, then every hidden neighbour is a mine
def mineSweep(board, boardLen):

    boardCopy = board

    for i in range(boardLen):
        for j in range(boardLen):
            if str(board[i,j]).isnumeric() and 1 <= board[i,j] <= 8:

                numberHint = board[i,j]

                if i == 0 and j == 0:

                    boardCopy = topLeft(i,j, boardCopy, numberHint)

                elif i == boardLen-1 and j == 0:

                    boardCopy = botLeft(i,j, boardCopy, numberHint)

                elif i == 0 and j == boardLen-1:

                    boardCopy= topRight(i,j, boardCopy, numberHint)

                elif i == boardLen-1 and j == boardLen-1:

                    boardCopy = botRight(i,j, boardCopy, numberHint)

                elif i == 0 and j != 0 and j != boardLen-1:

                    boardCopy = topEdge(i,j, boardCopy, numberHint)

                elif i != 0 and i != boardLen-1 and j == 0:

                    boardCopy = leftEdge(i,j, boardCopy, numberHint)

                elif i != 0 and i != boardLen-1 and j == boardLen-1:

                    boardCopy = rightEdge(i,j, boardCopy, numberHint)

                elif i == boardLen-1 and j != 0 and j != boardLen-1:

                    boardCopy = botEdge(i,j, boardCopy, numberHint)

                else:   
                    boardCopy = middle(i,j, boardCopy, numberHint)

    return boardCopy


def topLeft(i,j, board, hint):

    hiddenCount = 0
    hiddenTuples = []
    mineCount = 0

    topLeftCoords = [(1,1), (1,0), (0,1)]
                    #  SE,    S,     E

    for x,y in topLeftCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] == ('M' or 'm'):
            mineCount += 1

    if (hint - mineCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = 'M'

    return board


def topRight(i,j, board, hint):

    hiddenTuples = []
    hiddenCount = 0
    mineCount = 0

    topRightCoords = [(1,-1), (1,0), (0,-1)]
                    #   SW,     S,      W

    for x,y in topRightCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] == ('M' or 'm'):
            mineCount += 1

    if (hint - mineCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = 'M'

    return board


def botLeft(i,j, board, hint):

    hiddenCount = 0
    hiddenTuples = []
    mineCount = 0

    botLeftCoords = [(-1,1), (-1,0), (0,1)]
                    #   NE,     N,      E

    for x,y in botLeftCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] == ('M' or 'm'):
            mineCount += 1

    if (hint - mineCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = 'M'

    return board


def botRight(i,j, board, hint):

    hiddenCount = 0
    hiddenTuples = []
    mineCount = 0

    botRightCoords = [(-1,-1), (-1,0), (0,-1)]
                    #    NW,      N,      W

    for x,y in botRightCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] == ('M' or 'm'):
            mineCount += 1

    if (hint - mineCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = 'M'

    return board


def topEdge(i,j, board, hint):

    hiddenCount = 0
    hiddenTuples = []
    mineCount = 0

    topEdgeCoords = [(0,-1), (0,1), (1,0), (1,-1), (1,1)]
                    #   W,     E,     S,     SW,    SE

    for x,y in topEdgeCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] == ('M' or 'm'):
            mineCount += 1

    if (hint - mineCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = 'M'

    return board
    

def leftEdge(i,j, board, hint):

    hiddenCount = 0
    hiddenTuples = []
    mineCount = 0

    leftEdgeCoords = [(0,1), (1,0), (1,1), (-1,0), (-1,1)]
                    #   E,     S,    SE,      N      NE

    for x,y in leftEdgeCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] == ('M' or 'm'):
            mineCount += 1

    if (hint - mineCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = 'M'

    return board


def rightEdge(i,j, board, hint):

    hiddenCount = 0
    hiddenTuples = []
    mineCount = 0

    rightEdgeCoords = [(0,-1), (1,0), (1,-1), (-1,0), (-1,-1)]
                    #   W,      S,     SW,      N,      NW

    for x,y in rightEdgeCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] == ('M' or 'm'):
            mineCount += 1

    if (hint - mineCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = 'M'

    return board


def botEdge(i,j, board, hint):

    hiddenCount = 0
    hiddenTuples = []
    mineCount = 0

    botEdgeCoords = [(0,-1), (-1,1), (0,1), (-1,0), (-1,-1)]
                    #   W,     NE,     E,     N,      NW

    for x,y in botEdgeCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] == ('M' or 'm'):
            mineCount += 1

    if (hint - mineCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = 'M'

    return board


def middle(i,j, board, hint):
    
    hiddenCount = 0
    hiddenTuples = []
    mineCount = 0

    midCoords = [(0,-1), (-1,1), (0,1), (-1,0), (-1,-1), (1,0), (1,-1), (1,1)]
                #   W,     NE,     E,     N,      NW      S,     SW,     SE

    for x,y in midCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] == ('M' or 'm'):
            mineCount += 1

    if (hint - mineCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = 'M'

    return board
def safeSweep(board, minesweeper, dim):

    boardCopy = board

    for i in range(dim):
        for j in range(dim):
            if (board[i,j] == 1 or board[i,j] == 2 or board[i,j] == 3 or board[i,j] == 4 or 
                board[i,j] == 5 or board[i,j] == 6 or board[i,j] == 7 or board[i,j] == 8):

                numberHint = board[i,j]

                boardLen = dim

                if i == 0 and j == 0:

                    pass

                elif i == boardLen-1 and j == 0:

                    pass

                elif i == 0 and j == boardLen-1:

                    pass

                elif i == boardLen-1 and j == boardLen-1:

                    pass

                elif i == 0 and j != 0 and j != boardLen-1:

                    pass

                elif i != 0 and i != boardLen-1 and j == 0:

                    pass

                elif i != 0 and i != boardLen-1 and j == boardLen-1:

                    pass

                elif i == boardLen-1 and j != 0 and j != boardLen-1:

                    pass

                else:   

                    boardCopy = middle(i,j, boardCopy, minesweeper, numberHint)

    return boardCopy


def middle(i,j, board, answers, hint):

    hiddenCount = 0
    safeCount = 0
    hiddenTuples = []

    # North
    if board[i-1,j] == '-':
        hiddenCount += 1
        hiddenTuples.append((i-1,j))

    # North West 
    if board[i-1,j-1] == '-':
        hiddenCount += 1
        hiddenTuples.append((i-1,j-1))

    # North East
    if board[i-1,j+1] == '-':
        hiddenCount += 1
        hiddenTuples.append((i-1,j+1))

    # South
    if board[i+1,j] == '-':
        hiddenCount += 1
        hiddenTuples.append((i+1,j))

    # South West 
    if board[i+1,j-1] == '-':
        hiddenCount += 1
        hiddenTuples.append((i+1,j-1))

    # South East
    if board[i+1,j+1] == '-':
        hiddenCount += 1
        hiddenTuples.append((i+1,j+1))

    # West
    if board[i,j-1] == '-':
        hiddenCount += 1
        hiddenTuples.append((i,j-1))

    # East
    if board[i, j+1] == '-':
        hiddenCount += 1
        hiddenTuples.append((i,j+1))

    # North
    if board[i-1,j] != 'M' and board[i-1,j] != '-':
        safeCount += 1

    # North West 
    if board[i-1,j-1] != 'M' and board[i-1,j-1] != '-':
        safeCount += 1

    # North East
    if board[i-1,j+1] != 'M' and board[i-1,j+1] != '-':
        safeCount += 1

    # South
    if board[i+1,j] != 'M' and board[i+1,j] != '-':
        safeCount += 1

    # South West 
    if board[i+1,j-1] != 'M' and board[i+1,j-1] != '-':
        safeCount += 1

    # South East
    if board[i+1,j+1] != 'M' and board[i+1,j+1] != '-':
        safeCount += 1

    # West
    if board[i,j-1] != 'M' and board[i,j-1] != '-':
        safeCount += 1

    # East
    if board[i, j+1] != 'M' and board[i, j+1] != '-':
        safeCount += 1

    if ((8 - hint) - safeCount) == hiddenCount:
        
        hiddenTuplesLen = len(hiddenTuples)

        for i in range(hiddenTuplesLen):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = answers[x,y]

    return board

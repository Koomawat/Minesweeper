import numpy as np
import random

def board(dim):

    gameboard = np.zeros(shape=(dim,dim))

    return gameboard

def minePlacer(n, board):

    boardLen = len(board)

    for i in range(n):
        
        tupleX = random.randint(0, boardLen-1)
        tupleY = random.randint(0, boardLen-1)

        if (board[tupleX,tupleY] == 0):
            # 9 represents a mine 
            board[tupleX,tupleY] = 9
        else:

            while(board[tupleX,tupleY] != 0):

                tupleX = random.randint(0, boardLen-1)
                tupleY = random.randint(0, boardLen-1)

                if (board[tupleX,tupleY] == 0):
                    # 9 represents a mine 
                    board[tupleX,tupleY] = 9

    return board
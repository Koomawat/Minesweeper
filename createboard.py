import numpy as np
import random

def board(dim):

    gameboard = np.zeros(shape=(dim,dim), dtype=object)

    return gameboard

def minePlacer(n, board):

    boardLen = len(board)

    for i in range(n):
        
        tupleX = random.randint(0, boardLen-1)
        tupleY = random.randint(0, boardLen-1)

        if (board[tupleX,tupleY] == 0):
            # M represents a mine 
            board[tupleX,tupleY] = 'M'
        else:

            while(board[tupleX,tupleY] != 0):

                tupleX = random.randint(0, boardLen-1)
                tupleY = random.randint(0, boardLen-1)

                if (board[tupleX,tupleY] == 0):
                    # M represents a mine 
                    board[tupleX,tupleY] = 'M'

    return board
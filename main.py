import numpy as np
import random

def create_board():
    return np.zeros((3,3), dtype=int)
    
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        
def possibilities(board):
    not_occupied = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            not_occupied.append((i,j))
    return not_occupied

def random_place(board, player):
    position = random.choice(possibilities(board))
    place(board, player, position)
    return board # not sure why is needed to return board

def row_win(board, player):
    

import numpy as np

def create_board():
    return np.zeros((3,3), dtype=int)
    
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        
def possibilities(board):
    not_occupied = []
    for i in range(len(board)):
        for j in range(len(board[0]):
            

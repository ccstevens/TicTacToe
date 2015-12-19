'''

Copyright (c) 2015 Chris Stevens. All Rights Reserved.

Module Name:

    minimax.py
    
Abstract:

    This module implements the minimax algorithm for Tic-Tac-Toe AI.
    
Author:

    Chris Stevens 18-Dec-2015

'''
#
# --------------------------------------------------------------------- Imports
#

from constants import *
from tttlib import *
from random import *

#
# ----------------------------------------------------------------- Definitions
#

#
# ------------------------------------------------------------------- Functions
#                

def get_minimax_move(board, moves, player):
    '''
    
    Routine Description:
    
        This routine gets the next move for the given player based on the 
        minimax algorithm.
    
    Arguments:
    
        board - Supplies the current game board.
        
        moves - Supplies the number of moves that have been made so far, not
            including the move being requested.
            
        player - Supplies the token of the player for whom this move is being
            made.
    
    Return Value:
    
        Returns the row and column indices of the chosen move.
    
    '''
    
    value, (row, col) = minimax(board, moves, player, True)
    return row, col
    
def minimax(board, depth, player, maximize):
    '''
    
    Routine Description:
    
        This routine runs the minimax algorithm for the given player, returning
        the indices for the best move and its corresponding point value.
    
    Arguments:
    
        board - Supplies the current game board.
        
        depth - Supplies the depth of the algorithm, which corresponds to the
            total number of moves made.
            
        player - Supplies the token of the player to make the next move.
        
        maximize - Supplies a boolean indicating if the given player is the
            maximizing (True) or minimizing (False) player.
    
    Return Value:

        Returns a tuple consisting of the minimax point value and the indices
        of the move corresponding to that value.
    
    '''
    
    #
    # The first base case for the minimax recursion is a win for the opponent
    # player. If there is a victory, return the associated point value based on
    # the depth of the move and whether the maximizing player won.
    #

    max_depth = len(board) * len(board)
    opponent = get_opponent(player)    
    if has_won(board, opponent):
        winning_value = (max_depth + 1) - depth
        if maximize:
            winning_value = -winning_value
            
        return winning_value, (0, 0)
        
    #
    # If the board is full, it's a draw. Assign zero points to this result.
    #
        
    if depth >= max_depth:
        return 0, (0, 0)

    #
    # The opponent player did not win, so recurse on all possible moves for the 
    # current player.
    #
        
    possible_moves = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == EMPTY_CHAR:
                board[row][col] = player
                value, move = minimax(board, depth + 1, opponent, not maximize)                               
                board[row][col] = EMPTY_CHAR
                possible_moves.append((value, (row, col)))

    #
    # Out of all the moves attempted, find the either the maximum or minimum
    # valued moves depending on whether this is the maximizing or minimizing 
    # player. If there is more than one "best" move, pick randomly.
    #
                
    values = [move[0] for move in possible_moves]
    if maximize:    
        best_value = max(values)        

    else:
        best_value = min(values)
        
    best_moves = [move for move in possible_moves if move[0] == best_value]
    return best_moves[int(random() * len(best_moves))]

'''

Copyright (c) 2015 Chris Stevens. All Rights Reserved.

Module Name:

    tttlib.py
    
Abstract:

    This module implements the support library for the Tic-Tac-Toe game.
    
Author:

    Chris Stevens 18-Dec-2015

'''

#
# --------------------------------------------------------------------- Imports
#

from constants import *
from random import *

#
# ----------------------------------------------------------------- Definitions
#

#
# --------------------------------------------------------------------- Globals
#

#
# ------------------------------------------------------------------- Functions
#

def get_random_move(board):
    '''
    
    Routine Description:
    
        This routine returns a random move.
    
    Arguments:
    
        board - Supplies the current board.
    
    Return Value:
    
        A row, col tuple for the coordinates of the random move.
    
    '''
    
    board_dimension = len(board)
    while True:
        row = int(random() * board_dimension);
        col = int(random() * board_dimension);
        if board[row][col] == EMPTY_CHAR:
            break;
            
    return row, col
    
def get_row_col(board, player, row):
    '''
    
    Routine Description:
    
        This routine gets a row or column index from the user.
        
    Arguments:
    
        board - Supplies the current game board.
        
        player - Supplies the token of the current player.
        
        row - Supplies a boolean indicating whether the input is for a row 
            (True) or a column (False).
            
    Return Value:
    
        Returns the row or column index between 0 and the dimension of the 
        board, not inclusive.
    
    '''

    board_dimension = len(board)
    if row:
        prompt = 'row'
    
    else:
        prompt = 'column'
        
    prompt = player + ', enter a ' + prompt
    prompt += ' [1, ' + str(board_dimension) + ']:'
    valid = False
    while not valid:
        index = raw_input(prompt)
        try:    
            index = int(index)
            valid = index in range(1, board_dimension + 1)
                        
        except ValueError:
            pass
            
    return index - 1

def get_human_move(board, player):
    '''
    
    Routine Description:
    
        This routine gets a move from a human player.
        
    Arguments:
    
        board - Supplies the current game board.
        
        player - Supplies the token identifier for the current player.
    
    Return Value:
    
        A row, col tuple for the coordinates of the human's next move.
    
    '''
    
    while True:
        row = get_row_col(board, player, True)
        col = get_row_col(board, player, False)                
        if board[row][col] == EMPTY_CHAR:
            break;
                    
        print 'Space is already occupied by ' + board[row][col]
        
    return row, col
            
def create_board(dimension):
    '''
    
    Routine Description:
    
        This routine creates and initializes a Tic-Tac-Toe board with the given
        dimension. Tic-Tac-Toe boards are always square.        
    
    Arguments:

        dimension - Supplies the dimension of the Tic-Tac-Toe board.
        
    Return Value:
    
        Returns the newly created board.
    
    '''

    return [[EMPTY_CHAR for x in range(dimension)] for y in range(dimension)]
    
def has_won(board, player):
    '''
    
    Routine Description:
    
        This routine determins if the given player has won the game.
    
    Arguments:
    
        board - Supplies the board to test for a winning condition.
    
        player - Supplies the player whose winning condition is being detected.
    
    Return Value:
    
        True if the player has one. False otherwise.
    
    '''
    
    #
    # Search the rows for a victory.
    #
    
    for row in board:
        if all(value == player for value in row):
            return True
    
    #
    # Search the columns for a victory.
    #
    
    for i in range(len(board)):
        if all(value == player for value in [row[i] for row in board]):
            return True
    
    #
    # Search the diagonals for a victory.
    #
    
    diagonal = [row[i] for i, row in enumerate(board)]
    if all(value == player for value in diagonal): 
        return True
        
    diagonal = [row[~i] for i, row in enumerate(board)]
    if all(value == player for value in diagonal): 
        return True
        
    return False

def print_board(board):
    '''

    Routine Description:

        This routine prints the Tic-Tac-Toe game board.

    Arguments:

        board - Supplies the board to print.

    Return Value

        None.

    '''
    
    row_separator = '\n' + '|'.join('---' for i in range(len(board))) + '\n' 
    print '\n'
    print(row_separator.join(['|'.join([' ' + token + ' ' for token in row]) 
                             for row in board]))
                               
    print '\n'

def get_opponent(player):
    '''
    
    Routine Description:
    
        This routine returns the token of the given player's opponent.
    
    Arguments:
    
        player - Supplies the token of a player.
    
    Return Value:
    
        Returns the token of the given player's opponent.
    
    '''
    
    if player == X_CHAR:
        return O_CHAR
        
    return X_CHAR

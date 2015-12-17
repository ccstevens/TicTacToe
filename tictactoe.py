'''

Copyright (c) 2015 Chris Stevens. All Rights Reserved.

Module Name:

    tictactoe.py
    
Abstract:

    This module implements the main game engine for Tic-Tac-Toe.
    
Author:

    Chris Stevens 13-Dec-2015

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
# Define the array of available opponent (AI) types.
#

ai_types = [(AI_HUMAN, 0, 'Human (find a friend)'),
            (AI_RANDOM, 0, 'Random (you better win)')]

#
# ------------------------------------------------------------------- Functions
#

def get_ai_move(board, ai_type, moves, current_player):
    '''
    
    Routine Description:
    
        This routine gets the next move for the computer (AI) player.
        
    Arguments:
    
        board - Supplies the current game board.
        
        moves - Supplies the total number of moves that have been made in the
            game, including the current move.
            
        current_player - Supplies the token of the player making the move.
        
    Return Value:
    
        A row, col tuple for the coordinates of the AI's next move.
        
    '''    

    if ai_type is AI_RANDOM:
        while True:
            row = int(random() * len(board));
            col = int(random() * len(board));
            if board[row][col] == EMPTY_CHAR:
                break;
                
    else:
        row, col = get_human_move(board, current_player)        
        
    return row, col
    
def get_row_col(board, current_player, row):
    '''
    
    Routine Description:
    
        This routine gets a row or column index from the user.
        
    Arguments:
    
        board - Supplies the current game board.
        
        current_player - Supplies the token of the current player.
        
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
        
    prompt = current_player + ', enter a ' + prompt
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

def get_human_move(board, current_player):
    '''
    
    Routine Description:
    
        This routine gets a move from a human player.
        
    Arguments:
    
        board - Supplies the current game board.
        
        current_player - Supplies the token identifier for the current player.
    
    Return Value:
    
        A row, col tuple for the coordinates of the human's next move.
    
    '''
    
    while True:
        row = get_row_col(board, current_player, True)
        col = get_row_col(board, current_player, False)                
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
    
    board_separator = '\n' + '|'.join('---' for i in range(len(board))) + '\n'
    print '\n'
    print(board_separator.join(['|'.join([' ' + token + ' ' for token in row]) 
                               for row in board]))
                               
    print '\n'

def main():
    '''

    Routine Description:

        This routine implements the main handling for the Tic-Tac-Toe game.

    Arguments:

        None.

    Return Value

        None.

    '''

    print '\nWelcome to TicTacToe!'

    #
    # Get the board dimension.
    #
    
    prompt = '\nPick the board dimension (e.g. 3 = 3x3 board): '
    while True:
        dimension = raw_input(prompt)
        try:
            dimension = int(dimension)
            if dimension >= MINIMUM_DIMENSION:
                break;
                
        except ValueError:
            pass
            
        print 'Invalid dimension. Try again.\n'

    #
    # Get the desired AI type.
    #
    
    print '\nHere are the available opponents:\n'
    valid_ai_types = [type for type in ai_types 
                               if type[1] == 0 or type[1] >= dimension]
                      
    for ai_type in valid_ai_types:
        print '\t' + str(ai_type[0]) + ' - ' + ai_type[2]

    print ''        
    while True:
        ai_type = raw_input('Please pick an opponent: ')
        try:
            ai_type = int(ai_type)        
            if ai_type in [types[0] for types in valid_ai_types]:
                break
                
        except ValueError:
            pass
            
        print 'Invalid opponent. Try again.\n'
            
    #
    # Create the game board.
    #
            
    board = create_board(dimension)

    #
    # Run the game input the winning condition is found for the current player.
    #
    
    player_one = X_CHAR
    player_two = O_CHAR
    current_player = player_two
    moves = 0
    max_moves = dimension * dimension
    winner = False
    while not winner and moves < max_moves:        
    
        #
        # Switch players.
        #
    
        if current_player == player_one:
            current_player = player_two
            
        else:
            current_player = player_one

        #
        # Print the updated board.
        #
           
        print_board(board)        
        
        #
        # Try to collect valid input for the current player.
        #
        
        if current_player == player_one:
            row, col = get_human_move(board, current_player)
               
        #
        # Get the opponent's move.
        #
               
        else:
            row, col = get_ai_move(board, ai_type, moves, current_player)
            
        #
        # Fill in the space with the current character's value and check to
        # see if there is a winner.
        #
        
        board[row][col] = current_player
        winner = has_won(board, current_player)
        moves += 1
    
    print_board(board)
    if winner:
        print current_player + ' won the game!'
        
    else:
        print 'It is a tie!'
    
if __name__ == '__main__':
    main()

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
from tttlib import *
from minimax import *

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
            (AI_RANDOM, 0, 'Random (you better win)'),
            (AI_MINIMAX, 3, 'Minimax (you won\'t win)')]

#
# ------------------------------------------------------------------- Functions
#

def get_ai_move(board, ai_type, moves, player):
    '''
    
    Routine Description:
    
        This routine gets the next move for the computer (AI) player.
        
    Arguments:
    
        board - Supplies the current game board.
        
        ai_type - Supplies the opponent's AI type.
        
        moves - Supplies the total number of moves that have been made in the
            game, including the current move.
            
        player - Supplies the token of the player making the move.
        
    Return Value:
    
        A row, col tuple for the coordinates of the AI's next move.
        
    '''    

    if ai_type is AI_RANDOM:
        row, col = get_random_move(board)

    elif ai_type is AI_MINIMAX:
        row, col = get_minimax_move(board, moves, player)
                
    else:
        row, col = get_human_move(board, player)        
        
    return row, col

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

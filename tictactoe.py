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

#
# ----------------------------------------------------------------- Definitions
#

#
# --------------------------------------------------------------------- Globals
#

#
# ------------------------------------------------------------------- Functions
#

def create_board(width, height):
    '''
    
    Routine Description:
    
        This routine creates and initializes a width by height Tic-Tac-Toe 
        board.
    
    Arguments:
    
        width - Supplies the desired width of the board.
        
        height - Supplies the desired height of the board.
        
    Return Value:
    
        Returns the newly created board.
    
    '''

    return [[EMPTY_CHAR for x in range(width)] for y in range(height)]
    
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
    
    for i in range(BOARD_WIDTH):
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

    board = create_board(BOARD_WIDTH, BOARD_HEIGHT)
    player_one = X_CHAR
    player_two = O_CHAR
    current_player = player_two
    moves = 0
    max_moves = BOARD_WIDTH * BOARD_HEIGHT
    winner = False
    
    #
    # Run the game input the winning condition is found for the current player.
    #
    
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
        
        while True:   
            valid_row = False
            while not valid_row:
                prompt = ', enter a row [0, ' + str(BOARD_HEIGHT - 1) + ']:'
                row = raw_input(current_player + prompt)
                try:    
                    row = int(row)
                    valid_row = row in range(BOARD_HEIGHT)
                    
                except ValueError:
                    pass

            valid_col = False
            while not valid_col:
                prompt = ', enter a col [0, ' + str(BOARD_WIDTH - 1) + ']:'
                col = raw_input(current_player + prompt)
                try:    
                    col = int(col)
                    valid_col = col in range(BOARD_WIDTH)
                    
                except ValueError:
                    pass
            
            #
            # Make sure the space is empty.
            #
            
            if board[row][col] == EMPTY_CHAR:
                break;
                
            print 'Space is already occupied by ' + board[row][col]
            
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

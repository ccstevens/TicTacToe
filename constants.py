'''

Copyright (c) 2015 Chris Stevens. All Rights Reserved.

Module Name:

    constants.py
    
Abstract:

    This module stores constant values for Tic-Tac-Toe.
    
Author:

    Chris Stevens 13-Dec-2015

'''

#
# ----------------------------------------------------------------- Definitions
#

#
# Tic-Tac-Toe games less than 3x3 are trivial.
#

MINIMUM_DIMENSION = 3

#
# Define the characters used for the two players.
#

EMPTY_CHAR = ' '
X_CHAR = 'X'
O_CHAR = 'O'

#
# Define the various opponent (AI) types.
#

AI_HUMAN = 1
AI_RANDOM = 2
AI_MINIMAX = 3

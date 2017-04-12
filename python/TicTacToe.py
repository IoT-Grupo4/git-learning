"""To play Tic-Tac-Toe-Py you just have to type: python3 TicTacToe.py
Enjoy!
Created by: JSch"""

# Creating the Tic Tac Toe table registor. I am using dictionaries to keep track of the plays. 
# Each slot will have a key for the column and a key for the line. This way will be easy to verify
# victory or draw.
# 
#       (1) |  (2)  |  (3)
#      ---------------------
#       (4) |  (5) |   (6)
#      ---------------------
#       (7) |  (8) |   (9)
#
# Created by: Jsch

# Creating a function that prints the refreshed Tic-Tac-Toe-Py table.
# INPUT: None
# OUTPUT: None

def print_table():
    print("                \n\
                                    (1) | (2) | (3) \n\
                                   -----------------\n\
                                    (4) | (5) | (6) \n\
                                   -----------------\n\
                                    (7) | (8) | (9) ")
    
    print('                 \n\
                                       {a} | {b} | {c} \n\
                                      -----------\n\
                                       {d} | {e} | {f} \n\
                                      -----------\n\
                                       {g} | {h} | {i} '.format(a = Play_Registor[1], b = Play_Registor[2],
                                                              c = Play_Registor[3], d = Play_Registor[4],
                                                              e = Play_Registor[5], f = Play_Registor[6],
                                                              g = Play_Registor[7], h = Play_Registor[8],
                                                              i = Play_Registor[9]))

# Creating function to register X play and O play at the '''Play_registor'''.
# INPUT: Slot to enter users input
# OUTPUT: Slot was assigned <- True
#         Slot was NOT assigned <- False

def register_x_play():
    slot = verify_valid_slot('X')
    while True:
        if Play_Registor[slot] == ' ':
            Play_Registor[slot] = 'X'
            break
        else:
            print('Slot already ocupied. Please enter an empity slot')
            slot = verify_valid_slot('X')
            continue

def register_o_play():
    slot = verify_valid_slot('O')
    while True:
        if Play_Registor[slot] == ' ':
            Play_Registor[slot] = 'O'
            break
        else:
            print('Slot already ocupied. Please enter an empity slot')
            slot = verify_valid_slot('O')
            continue

# Creating a function to verify if the slot inserted by the user is valid
# INPUT: Player check, i.e: either 'X' or 'O'
# OUTPUT: Valid slot number <- int

def verify_valid_slot(check):
    while True:
        slotnum = input('{p} turn: '.format(p = check))
        if slotnum.isnumeric():
                slotnum = int(slotnum)
                if slotnum in list(range(1,10)):
                    return slotnum
                    break
                else:
                    print('Please enter a valid slot number!')
        else:
             print('Please enter a number!')

# Creating function to verify victory or draw
# INPUT: None
# OUTPUT: If victory or draw is detected <- True
#         If neither are detected <- False

def verify_victory_draw(last):
    if ((Play_Registor[1] == Play_Registor[2] == Play_Registor[3] != ' ') or 
        (Play_Registor[4] == Play_Registor[5] == Play_Registor[6] != ' ') or
        (Play_Registor[7] == Play_Registor[8] == Play_Registor[9] != ' ') or
        (Play_Registor[1] == Play_Registor[4] == Play_Registor[7] != ' ') or 
        (Play_Registor[2] == Play_Registor[5] == Play_Registor[8] != ' ') or
        (Play_Registor[5] == Play_Registor[6] == Play_Registor[9] != ' ') or
        (Play_Registor[1] == Play_Registor[5] == Play_Registor[9] != ' ') or
        (Play_Registor[7] == Play_Registor[5] == Play_Registor[3] != ' ')
        ):
        print('{p} is victorious.\nGame over.'.format(p = last))
        return True
    elif ' ' not in Play_Registor.values():
        print('Draw.\nGame over.')
        return True
    else:
        return False

# Creating the loop that contains the game.

import os

while True:
    # Initializing for the first time the dictionary that will keep the marks 'X' and 'O'
    Play_Registor = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
    
    print("       Welcome to Tic-Tac-Toe-Py. Let's start with the X player!\n\
       Please enter the slot where you want to insert the X.\n\
       After it, it's O time. Enter accordingly to the following table:\n\
       \n\
                            (1) | (2) | (3) \n\
                           -----------------\n\
                            (4) | (5) | (6) \n\
                           -----------------\n\
                            (7) | (8) | (9) ")

    while True:
        # Register the input
        register_x_play()
        os.system('clear')

        # Function to show the refreshed table
        print_table()

        # Verify victory from X
        if verify_victory_draw('X'):
            break
    
        # Register the input
        register_o_play()
        os.system('clear')

        # Function to show the refreshed table
        print_table()

        # Verify victory from O
        if verify_victory_draw('O'):
            break

    # Setting all values back to whitespace at the table
    Play_Registor = Play_Registor.fromkeys(Play_Registor)
    answer = input('Would you like to play again?(y/n) ')
    if answer == 'y':
        os.system('clear')
        continue
    else:
        os.system('clear')
        break


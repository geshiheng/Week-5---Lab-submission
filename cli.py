# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    while winner == None:
        print("TODO: take a turn!")
      
        winner = 'X'  # FIXME

from logic import TicTacToe
from logic import play
from player import HumanPlayer, RandomComputerPlayer


if __name__ == '__main__':
    x_player = RandomComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
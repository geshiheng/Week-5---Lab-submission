
from logic import TicTacToe
from logic import play
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


if __name__ == '__main__':
    mode = input("Please choose the game mode (pve1, pve2 or pvp): ")
    if mode == "pve1":
        x_player = SmartComputerPlayer('X')
        o_player = HumanPlayer('O')
    elif mode == "pve2":
        x_player = RandomComputerPlayer('X')
        o_player = HumanPlayer('O')
    else:
        x_player = HumanPlayer('X')
        o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
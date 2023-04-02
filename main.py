import random
import os
from tkinter import BOTTOM, Button, Frame, Menu, Tk, Label, Entry
from colorama import init, Fore, Back, Style
import sys

os.system("cls")
print()


board = [
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
]


def prepare_board():
    our_board = """
    {}|{}|{}
    {}|{}|{}
    {}|{}|{}
    """.format(
        *board
    )
    print(our_board)


def make_move(
    place,
    sign,
):

    if place < -1 or place > 8:
        print(Fore.Blue + "wrong number you dzban")
        return False
    elif board[place] == "_":
        board[place] = sign
        return True
    print("It's a wrong move")
    return False


def make_move_com(sign):
    for combination in WINING_COMBINATION:

        if (
            board[combination[0]] == "x"
            and board[combination[1]] == "x"
            and board[combination[2]] == "_"
        ):
            board[combination[2]] = "x"
            return
        elif (
            board[combination[1]] == "x"
            and board[combination[2]] == "x"
            and board[combination[0]] == "_"
        ):
            board[combination[0]] = "x"
            return
        elif (
            board[combination[2]] == "x"
            and board[combination[0]] == "x"
            and board[combination[1]] == "_"
        ):
            board[combination[1]] = "x"
            return
    for combination in WINING_COMBINATION:
        if (
            board[combination[0]] == "o"
            and board[combination[1]] == "o"
            and board[combination[2]] == "_"
        ):
            board[combination[2]] = "x"
            return
        elif (
            board[combination[1]] == "o"
            and board[combination[2]] == "o"
            and board[combination[0]] == "_"
        ):
            board[combination[0]] = "x"
            return
        elif (
            board[combination[2]] == "o"
            and board[combination[0]] == "o"
            and board[combination[1]] == "_"
        ):
            board[combination[1]] = "x"
            return

    place = random.randint(0, 8)
    if board[place] == "o" or board[place] == "x":
        make_move_com(sign)
    elif board[place] == "_":
        board[place] = sign
        return


def make_wining_board():
    for combination in WINING_COMBINATION:

        if (
            board[combination[0]] == "x"
            and board[combination[1]] == "x"
            and board[combination[2]] == "x"
        ):
            board[combination[0]] = "*"
            board[combination[1]] = "*"
            board[combination[2]] = "*"
            return
        elif (
            board[combination[1]] == "x"
            and board[combination[2]] == "x"
            and board[combination[0]] == "x"
        ):
            board[combination[0]] = "*"
            board[combination[1]] = "*"
            board[combination[2]] = "*"

            return
        elif (
            board[combination[2]] == "x"
            and board[combination[0]] == "x"
            and board[combination[1]] == "x"
        ):
            board[combination[0]] = "*"
            board[combination[1]] = "*"
            board[combination[2]] = "*"
            return
    for combination in WINING_COMBINATION:
        if (
            board[combination[0]] == "o"
            and board[combination[1]] == "o"
            and board[combination[2]] == "o"
        ):
            board[combination[0]] = "#"
            board[combination[1]] = "#"
            board[combination[2]] = "#"
            return
        elif (
            board[combination[1]] == "o"
            and board[combination[2]] == "o"
            and board[combination[0]] == "o"
        ):
            board[combination[0]] = "#"
            board[combination[1]] = "#"
            board[combination[2]] = "#"
            return
        elif (
            board[combination[2]] == "o"
            and board[combination[0]] == "o"
            and board[combination[1]] == "o"
        ):
            board[combination[0]] = "#"
            board[combination[1]] = "#"
            board[combination[2]] = "#"

            return


WINING_COMBINATION = (
    (0, 1, 2),
    (0, 3, 6),
    (0, 4, 8),
    (1, 4, 7),
    (2, 5, 8),
    (3, 4, 5),
    (6, 7, 8),
    (2, 4, 6),
)


def did_you_win(sign, player):

    for combination in WINING_COMBINATION:

        if (
            board[combination[0]]
            == board[combination[1]]
            == board[combination[2]]
            == (sign)
        ):
            print(Fore.BLUE + f" Game over and WINNER it is player  : {player}")
            make_wining_board()
            return True

    return False


def human_game():
    player1 = input("first player name, type here o  -->  ")
    print("Started", player1)
    player2 = input("second player name, type here x  -->  ")
    print("game man against man")
    print("player 1", player1, "player 2", player2)
    it_remis = True
    runda = 1
    counter = 1

    while counter != 10:

        pole = int(input("enter the field 0 - 8 "))
        if counter % 2 == 0:
            if make_move(pole, "x"):
                counter += 1
                info_for_players()
                if did_you_win("x", player2):
                    it_remis = False
                    break

        else:
            if make_move(pole, "o"):
                counter += 1
                info_for_players()
                if did_you_win("o", player1):
                    it_remis = False
                    break

        runda += 1
    if it_remis:
        print(" <<<  remis  >>>")


def chat_game(a):
    player1 = input(" player name, type here o  -->  ")
    number_of_counters = 10
    if a == 1:

        counter = 1
        print(f"Started: { player1} next - computer")
    if a == 2:

        counter = 2
        number_of_counters = 11
        print(Fore.RED + f"Started  computer: next { player1} ")
    print("game with  CHAT  played  x")

    it_remis = True

    while counter != number_of_counters:

        if counter % 2 == 0:
            make_move_com("x")
            counter += 1
            if did_you_win("x", "CHAT is much better then you "):

                it_remis = False
                break

        else:
            info_for_players()
            pole = int(input("enter the field 0 - 8 "))
            if make_move(pole, "o"):
                counter += 1

                if did_you_win("o", player1):

                    it_remis = False
                    break

    if it_remis:

        print(Fore.Pink + " <<<  remis  >>>")
    prepare_board()
    new_game()


def game_option():

    print("game board structure")
    print("0  1  2")
    print("3  4  5")
    print("6  7  8")
    ("o started, x next ")
    game_input = input(" game with human 1, or with computer 2 --> ")

    if game_input == "1":
        human_game()

    elif game_input == "2":

        a = random.randint(1, 2)

        chat_game(a)

    else:
        print("wrong option ")
        game_option()


def info_for_players():

    print("     0  1  2")
    print("     3  4  5")
    print("     6  7  8")
    print("     next turn")
    prepare_board()


def new_game():
    print(Fore.WHITE)
    new_game_option = input(" next game 1, or exit 2 --> ")

    if new_game_option == "1":
        clear_board()
        game_option()

    elif new_game_option == "2":
        sys.exit()


def clear_board():
    global board
    board = [
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
    ]


game_option()

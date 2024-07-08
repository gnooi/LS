""" 
    This file contains a Tic Tac Toe Game. 

 """

import random
import os

SPACE_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
TOTAL_WINS = 3
WINNING_SQUARES = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                        [1, 4, 7], [2, 5, 8], [3, 6, 9],
                        [1, 5, 9], [3, 5, 7]]

FIRST_TO_PLAY = 'choose'

# <===== FUNCTIONS =====>

def prompt(message):
    """ Prints message with indentation """
    print((f'=> {message}'))

def display_instructions():
    """ Prints game instructions """
    prompt("Welcome to Tic Tac Toe! "
           "First player to win 3 rounds, wins the match.")
    prompt("Let's begin!")

def decide_first_to_play():
    """ Returns player who will make the first move """
    if FIRST_TO_PLAY == 'choose':
        while True:
            prompt('Who goes first? (player or computer)')
            choice = input().lower().strip()
            if choice in ['player', 'computer']:
                return choice
    else:
        return FIRST_TO_PLAY

def initialize_board():
    """ Returns an empty board """
    return {number: SPACE_MARKER for number in range(1, 10)}

def display_board(board):
    """ Prints the empty board """
    prompt(f'You are {HUMAN_MARKER}, Computer is {COMPUTER_MARKER}')
    first_row = f'  {board[1]}  |  {board[2]}  |  {board[3]}  '
    second_row = f'  {board[4]}  |  {board[5]}  |  {board[6]}  '
    third_row = f'  {board[7]}  |  {board[8]}  |  {board[9]}  '
    horizontal_line = f"{'-' * 5}+{'-' * 5}+{'-' * 5}"
    print()
    print(first_row)
    print(horizontal_line)
    print(second_row)
    print(horizontal_line)
    print(third_row)
    print()

def clear_screen():
    """ Clear screen """
    os.system('clear')

def join_or(lst, separator=', ', word='or'):
    """ Returns a new string with delimiters """
    match (len(lst)):
        case 0:
            return ''
        case 1:
            return str(lst[0])
        case 2:
            return f"{lst[0]} {word} {lst[1]}"
        case _:
            new_str = separator.join((element) for element in lst[:-1])
            return f'{new_str}{separator}{word} {lst[-1]}'

def player_chooses_square():
    """ Returns player's choice of square """
    player_choice = input('Choose a number from (1-9): ').strip()
    return player_choice

def empty_squares(board):
    """ Returns remaining empty squares on the board """
    return [key
            for key, value in board.items()
            if value == SPACE_MARKER]

def validate_players_choice(board, number):
    """ Returns player's choice after validation """
    grid_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    valid_choices = [str(num) for num in empty_squares(board)]

    while True:
        if number.isdigit():
            number = int(number)
            if number not in grid_squares:
                prompt("Please choose from (1-9): ")
                number = input()
            elif number not in empty_squares(board):
                prompt(f"Choose from empty squares: "
                       f"({join_or(valid_choices)})")
                number = input()
            else:
                break
        else:
            prompt("Please choose from (1-9): ")
            number = input()

    return int(number)

def mark_players_choice(board, number):
    """ Update player's choice on board """
    board[number] = HUMAN_MARKER

def find_at_risk_square(line, board, marker):
    """ Returns square at risk of winning"""
    current_line = [board[square] for square in line]

    if current_line.count(marker) == 2:
        for square in line:
            if board[square] == SPACE_MARKER:
                return square
    return None

def computer_chooses_square(board):
    """ Update computer's choice on board """
    square = None

    for line in WINNING_SQUARES:
        square = find_at_risk_square(line, board, COMPUTER_MARKER)
        if square:
            break

    if not square:
        for line in WINNING_SQUARES:
            square = find_at_risk_square(line, board, HUMAN_MARKER)
            if square:
                break

    if not square and board[5] == SPACE_MARKER:
        square = 5

    if not square:
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER

def reset_scoreboard():
    """ Returns empty scoreboard """
    return {'You': 0, 'Computer': 0}

def board_full(board):
    """ Returns boolean for board full or not """
    return len(empty_squares(board)) == 0

def someone_won(board):
    """ Returns boolean for winner or not """
    return bool(get_winner(board))

def get_winner(board):
    """ Returns winner """
    for line in WINNING_SQUARES:
        sq1, sq2, sq3 = line
        if all(board[sq] == HUMAN_MARKER for sq in [sq1, sq2, sq3]):
            return 'You'
        if all(board[sq] == COMPUTER_MARKER for sq in [sq1, sq2, sq3]):
            return 'Computer'
    return None

def play_again():
    """ Returns answer to play again """
    while True:
        prompt(('Play again? (y or n)'))
        answer = input().lower()

        if answer in ['y', 'n', 'yes', 'no']:
            return answer

def update_round_score(board, scoreboard):
    """ Updates scoreboard """
    winner = get_winner(board)
    if winner == 'You':
        scoreboard['You'] += 1
        prompt('You won this round!')
    elif winner == 'Computer':
        scoreboard['Computer'] += 1
        prompt('Computer won this round!')
    elif winner is None:
        prompt("This round was a tie! Let's continue.")

def display_round_score(scoreboard):
    """ Prints scoreboard for each round """
    prompt(f"Your score: {scoreboard['You']}")
    prompt(f"Computer's score: {scoreboard['Computer']}")

def display_grand_winner(scoreboard):
    """ Prints winner for match """
    if scoreboard['You'] == TOTAL_WINS:
        prompt('Congrats, you won this match!')
    elif scoreboard['Computer'] == TOTAL_WINS:
        prompt('Computer won this match, good game!')

def choose_square(board, current_player):
    """ Player to choose square """
    if current_player == 'player':
        player_square = player_chooses_square()
        number = validate_players_choice(board, player_square)
        mark_players_choice(board, number)
    elif current_player == 'computer':
        computer_chooses_square(board)

def alternate_player(current_player):
    """ Player to go next """
    if current_player == 'player':
        return 'computer'
    return 'player'

def play_1_round(first_to_play, scoreboard):
    """ One round of Tic Tac Toe """
    board = initialize_board()
    current_player = first_to_play

    display_board(board)
    while True:
        choose_square(board, current_player)
        clear_screen()
        display_board(board)
        if someone_won(board) or board_full(board):
            clear_screen()
            display_board(board)
            update_round_score(board, scoreboard)
            display_round_score(scoreboard)
            break
        current_player = alternate_player(current_player)


def first_to_win_match(scoreboard):
    """ Play a match; consists of multiple rounds """
    first_to_play = decide_first_to_play()
    while TOTAL_WINS not in (scoreboard['You'], scoreboard['Computer']):
        play_1_round(first_to_play, scoreboard)


def play_game():
    """ Play multiple matches until told otherwise """
    while True:
        display_instructions()
        scoreboard = reset_scoreboard()
        first_to_win_match(scoreboard)
        display_grand_winner(scoreboard)
        answer = play_again()
        if answer in ['n', 'no']:
            break

    prompt('Thanks for playing Tic Tac Toe!')

play_game()

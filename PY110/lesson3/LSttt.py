import random
import os

SPACE_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
TOTAL_WINS = 5
WINNING_SQUARES = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                   [1, 4, 7], [2, 5, 8], [3, 6, 9],
                   [1, 5, 9], [3, 5, 7]]

FIRST_TO_PLAY = 'choose'

def prompt(message):
    print(f'=> {message}')

def display_instructions():
    prompt("Welcome to Tic Tac Toe! "
           "First one to win 5 rounds, wins the match.")
    prompt("Let's begin!")

def decide_first_to_play():
    if FIRST_TO_PLAY == 'choose':
        while True:
            prompt('Who goes first? (player or computer)')
            choice = input().lower().strip()
            if choice in ['player', 'computer']:
                return choice
    else:
        return FIRST_TO_PLAY

def initialize_board():
    return {number: SPACE_MARKER for number in range(1, 10)}

def display_board(board):
    # os.system('clear')

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

def join_or(lst, separator=', ', word='or'):
    match len(lst):
        case 0:
            return ''
        case 1:
            return str(lst[0])
        case 2:
            return f"{lst[0]} {word} {lst[1]}"
        case _:
            new_str = separator.join((element) for element in lst[:-2])
            return f'{new_str}{separator}{word} {lst[-1]}'

def player_chooses_square():
    player_choice = input('Choose a number from (1-9): ').strip()
    return player_choice

def empty_squares(board):
    return [key for key, value in board.items() if value == SPACE_MARKER]

def validate_players_choice(board, number):
    grid_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    valid_choices = [str(num) for num in empty_squares(board)]

    while True:
        if number.isdigit():
            number = int(number)
            if number not in grid_squares:
                prompt("Please choose from (1-9): ")
                number = input()
            elif number not in empty_squares(board):
                prompt(f"Choose from empty squares: ({join_or(valid_choices)})")
                number = input()
            else:
                break
        else:
            prompt("Please choose from (1-9): ")
            number = input()

    board[number] = HUMAN_MARKER

def find_at_risk_square(line, board, marker):
    current_line = [board[square] for square in line]

    if current_line.count(marker) == 2:
        for square in line:
            if board[square] == SPACE_MARKER:
                return square

    return None

def computer_chooses_square(board, move_count):
    square = None

    # Check for winning move
    for line in WINNING_SQUARES:
        square = find_at_risk_square(line, board, COMPUTER_MARKER)
        if square:
            break

    # Check for defensive move
    if not square:
        for line in WINNING_SQUARES:
            square = find_at_risk_square(line, board, HUMAN_MARKER)
            if square:
                break

    # Pick square #5 if it's the second move and it's available
    if move_count == 1 and not square and board[5] == SPACE_MARKER:
        square = 5

    # Pick a random square
    if not square:
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER
    return move_count + 1

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(get_winner(board))

def get_winner(board):
    for line in WINNING_SQUARES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'You'
        elif (board[sq1] == COMPUTER_MARKER
              and board[sq2] == COMPUTER_MARKER
              and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def update_round_score(board, scores):
    winner = get_winner(board)
    if winner == 'You':
        scores['You'] += 1
    elif winner == 'Computer':
        scores['Computer'] += 1
    return scores

def display_round_score(scores):
    prompt(f"Your score: {scores['You']}")
    prompt(f"Computer's score: {scores['Computer']}")

def display_grand_winner(scores):
    if scores['You'] == TOTAL_WINS:
        prompt('Congrats, you won this match!')
    elif scores['Computer'] == TOTAL_WINS:
        prompt('Computer won this match, good game!')

def play_1_round(first_to_play, scores):
    board = initialize_board()
    move_count = 0

    if first_to_play == 'computer':
        move_count = computer_chooses_square(board, move_count)

    while True:
        display_board(board)
        player_square = player_chooses_square()
        validate_players_choice(board, player_square)
        if someone_won(board) or board_full(board):
            display_board(board)
            scores = update_round_score(board, scores)
            display_round_score(scores)
            break
        move_count = computer_chooses_square(board, move_count)
        if someone_won(board) or board_full(board):
            display_board(board)
            scores = update_round_score(board, scores)
            display_round_score(scores)
            break
    return scores

def first_to_win_5_rounds():
    scores = {'You': 0, 'Computer': 0}
    while scores['You'] < TOTAL_WINS and scores['Computer'] < TOTAL_WINS:
        first_to_play = decide_first_to_play()
        scores = play_1_round(first_to_play, scores)
    return scores

def play_game():
    while True:
        display_instructions()
        scores = first_to_win_5_rounds()
        display_grand_winner(scores)
        answer = play_again()
        if answer == 'no':
            break

    prompt('Thanks for playing Tic Tac Toe!')

play_game()


# import os
# import random

# INITIAL_MARKER = ' '
# HUMAN_MARKER = 'X'
# COMPUTER_MARKER = 'O'

# def prompt(message):
#     print(f"==> {message}")

# def display_board(board):
#     os.system('clear')
#     prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
#     print('')
#     print('     |     |')
#     print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
#     print('     |     |')
#     print('-----+-----+-----')
#     print('     |     |')
#     print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
#     print('     |     |')
#     print('-----+-----+-----')
#     print('     |     |')
#     print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
#     print('     |     |')
#     print('')

# def initialize_board():
#     return {square: INITIAL_MARKER for square in range(1, 10)}

# def empty_squares(board):
#     return [key for key, value in board.items() if value == INITIAL_MARKER]

# def player_chooses_square(board):
#     while True:
#         valid_choices = [str(num) for num in empty_squares(board)]
#         prompt(f"Choose a square ({', '.join(valid_choices)}):")
#         square = input().strip()
#         if square in valid_choices:
#             break

#         prompt("Sorry, that's not a valid choice.")

#     board[int(square)] = HUMAN_MARKER

# def board_full(board):
#     return len(empty_squares(board)) == 0

# def detect_winner(board):
#     winning_lines = [
#         [1, 2, 3], [4, 5, 6], [7, 8, 9],
#         [1, 4, 7], [2, 5, 8], [3, 6, 9],
#         [1, 5, 9], [3, 5, 7]
#     ]

#     for line in winning_lines:
#         sq1, sq2, sq3 = line
#         if (board[sq1] == HUMAN_MARKER 
#                 and board[sq2] == HUMAN_MARKER
#                 and board[sq3] == HUMAN_MARKER):
#             return 'Player'
#         elif (board[sq1] == COMPUTER_MARKER
#                 and board[sq2] == COMPUTER_MARKER
#                 and board[sq3] == COMPUTER_MARKER):
#             return 'Computer'

#     return None

# def someone_won(board):
#     return bool(detect_winner(board))

# def computer_chooses_square(board):
#     if len(empty_squares(board)) == 0:
#         return
#     square = random.choice(empty_squares(board))
#     board[square] = COMPUTER_MARKER

# def play_tic_tac_toe():
#     while True:
#         board = initialize_board()

#         while True:
#             display_board(board)

#             player_chooses_square(board)

#             if someone_won(board) or board_full(board):
#                 break

#             computer_chooses_square(board)
#             if someone_won(board) or board_full(board):
#                 break

#         if someone_won(board):
#             prompt(f"{detect_winner(board)} won!")
#         else:
#             prompt("It's a tie!")

#         prompt("Play again? (y or n)")
#         answer = input().lower()[0]

#         if answer != 'y':
#             break

#         prompt('Thanks for playing Tic Tac Toe!')

# # Call the main game function
# play_tic_tac_toe()
import random
import json
import os

with open('rpsmessages.json', 'r') as file:
    MESSAGES = json.load(file)

# <===== CONSTANTS =====>
VALID_CHOICES = {'r' : 'rock',
                 'p' : 'paper', 
                 'sc': 'scissors',
                 'l' : 'lizard', 
                 'sp': 'spock'} 

WINNING_COMBOS = {
    'rock':     ['scisors', 'lizard'],
    'paper':    ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard':   ['paper', 'spock'],
    'spock':    ['rock', 'scissors']
}

# <===== FUNCTIONS =====>

# Function welcomes player to the game.
def display_welcome():
    prompt(access_msg_from_json('welcome'))

# Function displays game overview.
def display_game_overview():
    prompt(access_msg_from_json('game_overview'))

# Function asks player if they're ready to play
# or needs more information to continue.
def ready_to_start():
    prompt(access_msg_from_json('start'))
    answer = input().lower().strip()
    while True:
        match answer:
            case 'help':
                display_game_overview()
                break
            case 'yes':
                break
            case _:
                prompt(access_msg_from_json('invalid_choice'))
                answer = input().lower().strip()

# Function prints a message.
def prompt(message):
    print(f'=> {message}')

# Function accesses a message in a json file.
def access_msg_from_json(message):
    return MESSAGES[message]

# Function instructs player how to select a game character.
def display_instructions():
    prompt(access_msg_from_json('instructions'))

# Function prints all game characters.
def display_game_characters():
    for abbreviation, character in VALID_CHOICES.items():
        print(f"=> '{abbreviation}' for {character}")

# Function asks player to select a character and
# returns the character if it's a valid character.
def validate_player_selection():
    while True:
        player_choice = input().lower().strip()
        formatted_player_selection = format_player_selection(player_choice)
        if formatted_player_selection:
            return format_player_selection(player_choice)

        prompt(access_msg_from_json('invalid_choice'))

# Function checks player's character abbreviation selection
# and returns the character's full name.
def format_player_selection(abbreviation):
    match abbreviation:
        case 'r':
            return VALID_CHOICES['r']
        case 'p':
            return VALID_CHOICES['p']
        case 'sc':
            return VALID_CHOICES['sc']
        case 'l':
            return VALID_CHOICES['l']
        case 'sp':
            return VALID_CHOICES['sp']

# Function returns a random character from the constant VALID_CHOICES.
def computer_selection():
    return random.choice(list(VALID_CHOICES.values()))

# Function displays player's character selection and
# the computer's character selection.
def display_selections(player_pick, computer_pick):
    prompt(f'You chose {player_pick},' +
           f' computer chose {computer_pick}.')

# Function returns a boolean value by
# checking if the computer choice is a value in the
# constant WINNING_COMBOS.
def player_wins(player_choice, computer_choice):
    return computer_choice in WINNING_COMBOS[player_choice]

# Function returns the winner of the round.
def display_winner_round(player, computer):
    winner = ''
    if player_wins(player, computer):
        winner = 'player'
    elif player == computer:
        return winner
    else:
        winner = 'computer'
    return winner

# Function updates scoreboard based on
# the winner of the round.
def update_scoreboard(scores, winner):
    if winner == 'player':
        scores['player'] += 1
        scores['rounds'] += 1
    elif winner == 'computer':
        scores['computer'] +=1
        scores['rounds'] += 1
    elif winner == '':
        scores['rounds'] += 1

# Function prints the grand winner of the game
# based on a scoreboard.
def display_grand_winner(scores):
    if scores['player'] > scores['computer']:
        prompt(access_msg_from_json('player_grand_winner'))
    else:
        prompt(access_msg_from_json('computer_grand_winner'))

# Function asks player if they want to play again.
def play_again():
    answer_options = ('yes', 'no')
    prompt(access_msg_from_json('another_game'))
    answer = input().lower().strip()

    while True:
        if answer in answer_options:
            return answer

        prompt(access_msg_from_json('invalid_choice'))
        answer = input().lower().strip()

# Function clears screen.
def clear_screen():
    os.system('clear')

# <===== MAIN PROGRAM =====>

display_welcome()
print()
ready_to_start()

# Nest main program of the game to provide player with option
# to play more than once.
while True:

    scoreboard = {'player' : 0,
                  'computer' : 0,
                  'rounds' : 0}

# Nest main program of the game to end when whoever wins 3
# rounds first.
    while scoreboard['player'] != 3 and scoreboard['computer'] != 3:

        display_instructions()

        display_game_characters()

        player_character_selection = validate_player_selection()

        computer_character_selection = computer_selection()

        display_selections(player_character_selection,
                           computer_character_selection)
        print()

        winner_of_round = display_winner_round(player_character_selection,
                                          computer_character_selection)

        update_scoreboard(scoreboard, winner_of_round)

        prompt(f'Scoreboard: {scoreboard}')
        print()

    display_grand_winner(scoreboard)
    print()

    if play_again() == 'no':
        break

clear_screen()
prompt(access_msg_from_json('goodbye'))
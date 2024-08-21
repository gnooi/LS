""" Twenty-One Game w/ Bonus Features """
import random
import os

SUITS = ["\u2663", "\u2665",
         "\u2666", "\u2660"] 
RANKS = ['A', '2', '3', '4', '5',
         '6', '7', '8', '9', '10', 
         'J', 'Q', 'K'] 
TOTAL_WINS = 3
TARGET_SCORE = 21
DEALER_HIT_UNTIL = 17

def prompt(message):
    """ Print a message """
    print(f'=> {message}')

def clear_screen():
    """ Clear screen """
    os.system('clear')

def display_scoreboard(text):
    """ Print the scoreboard """
    prompt(f"*{'-' * (len(text) + 2)}*")
    prompt(f'| {text} |')
    prompt(f"*{'-' * (len(text) + 2)}*")

def display_cards(cards):
    """ Print a card combination """
    buffer = ' ' * 3
    card_line = (buffer + '+-----+') * len(cards)
    rank_line = suit_line = rank_line2 = ''

    for rank, suit in cards:
        space = ' ' * (4 if rank != '10' else 3)
        rank_line += f"{buffer}|{rank}{space}|"
        suit_line += f"{buffer}|  {suit}  |"
        rank_line2 += f"{buffer}|{space}{rank}|"

    print(card_line)
    print(rank_line)
    print(suit_line)
    print(rank_line2)
    print(card_line)

def initialize_deck():
    """ Return all card combinations shuffled """
    cards = [(rank, suit)
             for suit in SUITS
             for rank in RANKS]

    random.shuffle(cards)
    return cards

def get_total_value(cards):
    """ Return total value of cards"""
    total = sum(11 if rank == 'A' else 10
            if rank in ['J', 'Q', 'K'] else int(rank)
            for rank, suit in cards)

    aces = sum(1 for rank, suit in cards if rank == 'A')

    while total > TARGET_SCORE and aces:
        total -= 10
        aces -= 1
    return total

def cards_busted(cards):
    """ Return boolean for value greater than target score """
    return get_total_value(cards) > TARGET_SCORE

def get_results(player_total, dealer_total):
    """ Returns results for the turn """
    if player_total > TARGET_SCORE:
        return 'PLAYER BUSTED'
    if dealer_total > TARGET_SCORE:
        return 'DEALER BUSTED'
    return ('PLAYER' if player_total > dealer_total else 'DEALER'
            if dealer_total > player_total else 'TIE')

def update_round_score(result, scoreboard):
    """ Updates scoreboard based on results """
    if result in ['PLAYER', 'DEALER BUSTED']:
        scoreboard['You'] += 1
    elif result in ['DEALER', 'PLAYER BUSTED']:
        scoreboard['Dealer'] += 1

def display_results(result):
    """ Prints the result for the round or turn"""
    results = {'PLAYER BUSTED': 'Busted! Dealer wins this round!',
               'DEALER BUSTED': 'Busted! You win this round!',
               'PLAYER': 'You win!', 
               'DEALER': 'Dealer wins!', 
               'TIE': "It's a tie!"}

    prompt(results[result])

def end_round(player_total, dealer_total, scoreboard):
    """ Calculates the results and ends the round """
    clear_screen()
    prompt(f"Dealer's total: {dealer_total}")
    prompt(f'Your total: {player_total}')
    result = get_results(player_total, dealer_total)
    update_round_score(result, scoreboard)
    display_results(result)
    display_round_score(scoreboard)

def display_grand_winner(scoreboard):
    """ Prints winner for match """
    if scoreboard['You'] == TOTAL_WINS:
        prompt('Congrats, you won this game!')
    elif scoreboard['Dealer'] == TOTAL_WINS:
        prompt('Dealer won this game, good game!')

def pop_two_from_deck(deck):
    """ Removes and returns 2 cards from the deck"""
    return [deck.pop(), deck.pop()]

def play_again():
    """ Prompts user if they wish to play again """
    while True:
        prompt('Play again? (y or n)')
        response = input().strip().lower()

        if response in ['y', 'n', 'yes', 'no']:
            return response

def reset_scoreboard():
    """ Returns a new scoreboard """
    return {'You': 0, 'Dealer': 0}

def display_round_score(scoreboard):
    """ Prints scoreboard for each round """
    text = f"Your score: {scoreboard['You']} | Dealer's score: {scoreboard['Dealer']}"
    display_scoreboard(text)

def player_turn(deck, player_cards):
    """ Returns player cards and its total after taking a turn """
    while True:
        prompt('Enter (h) for hit or (s) for stay: ')
        player_choice = input().strip().lower()
        if player_choice not in ['h', 's', 'hit', 'stay']:
            continue

        if player_choice in ['h','hit']:
            player_cards.append(deck.pop())
            player_total = get_total_value(player_cards)
            prompt('You chose to hit!')
            display_cards(player_cards)
            prompt(f'Your total is: {player_total}')

        if player_choice in ['s','stay'] or cards_busted(player_cards):
            break

    player_total = get_total_value(player_cards)
    return player_cards, player_total

def dealer_turn(deck, dealer_cards):
    """ Returns dealer's cards and its total after taking a turn """
    dealer_total = get_total_value(dealer_cards)
    prompt("Dealer's turn...")

    while dealer_total < DEALER_HIT_UNTIL:
        prompt('Dealer hits!')
        dealer_cards.append(deck.pop())
        dealer_total = get_total_value(dealer_cards)
        display_cards(dealer_cards)

    if cards_busted(dealer_cards):
        prompt(f"Dealer's total is now: {dealer_total}")

    return dealer_cards, dealer_total

def play_one_round(scoreboard):
    """ Play one round of the game """
    deck = initialize_deck()
    player_cards = pop_two_from_deck(deck)
    dealer_cards = pop_two_from_deck(deck)
    player_total = get_total_value(player_cards)
    dealer_total = get_total_value(dealer_cards)

    prompt('Dealer has: ')
    display_cards([dealer_cards[0], ('?', '?')])
    prompt('You have: ')
    display_cards(player_cards)
    prompt(f'Your total: {player_total}')

    player_cards, player_total = player_turn(deck, player_cards)

    if player_total > TARGET_SCORE:
        end_round(player_total, dealer_total, scoreboard)
        return

    prompt(f'You chose to stay at {player_total}')

    dealer_cards, dealer_total = dealer_turn(deck, dealer_cards)

    if dealer_total > TARGET_SCORE:

        end_round(player_total, dealer_total, scoreboard)
        return

    prompt(f'Dealer stays at {dealer_total}')
    end_round(player_total, dealer_total, scoreboard)

def best_of_five(scoreboard):
    """ Play multiple rounds of the game """
    while TOTAL_WINS not in (scoreboard['You'], scoreboard['Dealer']):
        play_one_round(scoreboard)

def play_game():
    """ Play until someone wins all rounds of the game """
    while True:
        prompt(f'Welcome to {TARGET_SCORE}!')
        scoreboard = reset_scoreboard()
        best_of_five(scoreboard)
        display_grand_winner(scoreboard)
        if play_again() in ['n', 'no']:
            break
        clear_screen()

play_game()

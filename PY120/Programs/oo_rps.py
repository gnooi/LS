"""Rock Paper Scissors Game"""

import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self):
        self.move = None

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = 'Please choose rock, paper, or scissors: '

        while True:
            choice = input(prompt).lower()
            if choice in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move = choice

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors!")

    def _display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors. Goodbye!")

    def _display_winner(self):
        winning_combinations = {
            'rock': 'scissors', 
            'paper': 'rock', 
            'scissors': 'paper'
        }

        human_move = self._human.move
        computer_move = self._computer.move

        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if human_move == computer_move:
            print("It's a tie")
        elif winning_combinations[human_move] == computer_move:
            print("You win!")
        else:
            print('Computer wins!')

    def _play_again(self):
        answer = input('Would you like to play again? (y/n)')
        return answer.lower().startswith('y')

    def play(self):
        self._display_welcome_message()

        while True:

            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break

        self._display_goodbye_message()

RPSGame().play()

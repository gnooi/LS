
import random
import os

def clear_screen():
    """Clear screen"""
    os.system('clear')

class Player:
    """Player class"""
    def __init__(self, marker) -> None:
        self.marker = marker
        self.score = 0


    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score

    def increment_score(self):
        self.score += 1

class Computer(Player):
    def __init__(self) -> None:
        super().__init__(Square.COMPUTER_MARKER)

class Human(Player):
    def __init__(self) -> None:
        super().__init__(Square.HUMAN_MARKER)

class Board:
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def display(self):
        row_1 = f'  {self.squares[1]}  |  {self.squares[2]}  |  {self.squares[3]}  '
        row_2 = f'  {self.squares[4]}  |  {self.squares[5]}  |  {self.squares[6]}  '
        row_3 = f'  {self.squares[7]}  |  {self.squares[8]}  |  {self.squares[9]}  '
        horizontal_line = f"{'-' * 5}+{'-' * 5}+{'-' * 5}"
        print()
        print(row_1)

        print(horizontal_line)
        print(row_2)

        print(horizontal_line)
        print(row_3)
        print()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

    def is_unused_square(self, key):
        return self.squares[key].is_unused()

class Square:
    INITIAL_MARKER = ' '
    HUMAN_MARKER = 'X'
    COMPUTER_MARKER = 'O'

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER


class TTTGame:
    MATCH_GOAL = 3
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7)
    )

    @staticmethod
    def _join_or(choices, separator=', ', word='or'):
        match len(choices):
            case 0:
                return ''
            case 1:
                return str(choices[0])
            case 2:
                return f"{choices[0]} {word} {choices[1]}"
            case _:
                new_str = separator.join(str(choice) for choice in choices[:-1])
                return f'{new_str}{separator}{word} {choices[-1]}'
        
    def __init__(self) -> None:
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.first_player = self.human

    def play(self):
        self.display_welcome_message()
        self.play_match()
        self.display_goodbye_message()

    def play_match(self):
        print(f"The first player to win {TTTGame.MATCH_GOAL} "
              "games wins the match. ")

        while True:
            self.play_one_game()
            self.update_match_score()
            self.display_match_score()

            if self.match_over():
                break 
            if not self.play_again():
                break

            self.first_player = self.toggle_player(self.first_player)

        self.display_match_results()

    def play_one_game(self):
        current_player = self.first_player

        self.board.reset()
        self.board.display()

        while True:
            self.player_moves(current_player)

            if self.is_game_over():
                break

            self.board.display_with_clear()
            current_player = self.toggle_player(current_player)

        self.board.display_with_clear()
        self.display_results()
    
    def play_again(self):
        while True:
            answer = input("Play again? (y/n) ").lower()

            if answer in ["y", "n", "yes", "no"]:
                break

            print("Sorry, that's not a valid choice. \n")

        clear_screen()
        return answer in ["y", "yes"]

    def player_moves(self, current_player):
        if current_player == self.human:
            self.human_moves()
        else:
            self.computer_moves()

    def human_moves(self):
        while True:
            valid_choices = self.board.unused_squares()
            printable_choices = TTTGame._join_or(valid_choices)
            prompt = f"Choose a square ({printable_choices}): "
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break

            except ValueError:
                print(f"Invalid input! Please enter one of these: {printable_choices}.")
            print("Sorry, that's not a valid choice. ")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        choice = self.offensive_computer_move()

        if not choice:
            choice = self.defensive_computer_move()

        if not choice:
            choice = self.pick_center_square()

        if not choice:
            choice = self.pick_random_square()


        self.board.mark_square_at(choice, self.computer.marker)

    def find_critical_square(self, player):
        for row in self.POSSIBLE_WINNING_ROWS:
            key = self.critical_square(row, player)
            if key:
                return key
            
        return None
    
    def critical_square(self, row, player):
        if self.board.count_markers_for(player, row) == 2:
            for key in row:
                if self.board.is_unused_square(key):
                    return key 
                
        return None
    
    def offensive_computer_move(self):
        return self.find_critical_square(self.computer)
    
    def defensive_computer_move(self):
        return self.find_critical_square(self.human)
    
    def pick_center_square(self):
        return 5 if self.board.is_unused_square(5) else None
    
    def pick_random_square(self):
        valid_choices = self.board.unused_squares()
        return random.choice(valid_choices)
    
    def match_over(self):
        return (self.is_match_winner(self.human) or
                self.is_match_winner(self.computer))
    
    def is_match_winner(self, player):
        return player.score >= TTTGame.MATCH_GOAL
    
    def update_match_score(self):
        if self.is_winner(self.human):
            self.human.increment_score()
        elif self.is_winner(self.computer):
            self.computer.increment_score()

    def display_match_score(self):
        human = self.human.score
        computer = self.computer.score
        heading = "Current match score: "
        match_status = (f"Your score: {human} | Computer's Score: {computer}")
        
        print(f"*{'-' * (len(match_status) + 2)}*")
        print(f'| {heading}{' ' * (len(match_status) - len(heading))} |')
        print(f'| {match_status} |')
        print(f"*{'-' * (len(match_status) + 2)}*")

            
    def display_match_results(self):
        if self.human.score > self.computer.score:
            print("You won this match! Congratulations!")
        elif self.human.score < self.computer.score:
            print("Oh, boo hoo. You lost the match!")

    def display_welcome_message(self):
        clear_screen()
        print("Welcome to Tic Tac Toe!")
        print()

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("I won! I won! Take that, human!")
        else:
            print("A tie game. How boring.")

    def toggle_player(self, player):
        return self.computer if player == self.human else self.human

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

    def at_risk_square(self, row):
        if self.board.count_markers_for(self.human, row) == 2:
            for key in row:
                if self.board.is_unused_square(key):
                    return key 
                
        return None

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return (self.is_winner(self.human) or 
                self.is_winner(self.computer))

game = TTTGame()
game.play()

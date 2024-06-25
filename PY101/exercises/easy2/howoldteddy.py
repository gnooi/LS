# Build a program that randomly generates and prints Teddy's age. 
# To get the age, you should generate a random number between 
# 20 and 100, inclusive.

import random

# def get_age():
#     age = random.randrange(20, 101)
#     return age

# def display_output():
#     age = get_age()
#     print(f'Teddy is {age} years old!')

# display_output()

# Example Output
# Teddy is 69 years old!

# Further Exploration
# Modify this program to ask for a name, then print the age for that 
# person. For an extra challenge, use "Teddy" as the name if no name 
# is entered.

def get_age():
    age = random.randrange(20, 101)
    return age

def get_name():
    name = input('What is your name? ')
    if name == '':
        name = 'Teddy'
    return name 

def display_output():
    age = get_age()
    name = get_name()
    print(f'{name} is {age} years old!')

display_output()
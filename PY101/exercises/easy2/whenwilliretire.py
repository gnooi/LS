# When Will I Retire?
# Build a program that displays when the user will retire and 
# how many years she has to work till retirement.

import datetime

def get_age():
    age = input('What is your age? ')
    return age

def get_retirement_age():
    retirement_age = input('At what age would you like to retire? ')
    return retirement_age

def calculate_current_year():
    current_year = datetime.datetime.today().year
    return current_year
    
def calculate_remaining_years(retirement_age, age):
    remaining_years = int(retirement_age) - int(age)
    return remaining_years

def calculate_retirement_year(current_year, remaining_years):
    retirement_year = int(current_year) + int(remaining_years)
    return retirement_year

def display_output():
    age = get_age()
    retirement_age = get_retirement_age()
    current_year = calculate_current_year()
    remaining_years = calculate_remaining_years(retirement_age, age)
    retirement_year = calculate_retirement_year(current_year, remaining_years)
    print(f"It's {current_year}. You will retire in "
          f"{retirement_year}.\nYou have only {remaining_years}"
          f" years of work to go!")

display_output()

# Example
# What is your age? 30
# At what age would you like to retire? 70

# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!
# Pseudocode:
# Welcome user to mortgage calculator:

# Nest main program of mortgage calculator in order
# to perform more than 1 calculation:

# Allow loan amount part of program to always execute
# until it breaks out of loop to move on to the next part.

# Allow interest_rate part of program to always execute
# until it breaks out of loop to move on to the next part.

# Allow yearly_loan_duration part of program to always execute
# until it breaks out of loop to move on to the next part.

# Allow monthly_payment part of program to always execute
# until it breaks out of loop to move on to the next part.

# Ask user to perform another calculation in the main program loop:

# Allow user's answer to be checked until it breaks out of loop:

# Break out of main program loop if user does not wish to
# perform another calculation:

# <======= CODE REFACTOR ========>

import json

with open('mortgagemessages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'=> {message}')

def invalid_number(number_str):
    try:
        if number_str == 'nan':
            raise ValueError
        elif number_str == 'inf':
            raise ValueError
        
        number = float(number_str)

        if number <=0: # To prevent a negative and zero edge case
            raise ValueError

    except ValueError:
        return True
    
    return False


def messages(message, additional_message=''):
    return MESSAGES[message] + additional_message

def get_loan_amount():
    prompt(messages('loan_amount'))
    loan_amount = input()

    return loan_amount

def validate_loan_amount(loan_amount):
    if invalid_number(loan_amount):
        prompt(messages('invalid_number'))

def get_interest_rate():
    prompt(messages('interest_rate'))
    interest_rate = input()

    return interest_rate

def validate_interest_rate(interest_rate):
    if invalid_number(interest_rate):
        prompt(messages('invalid_number'))


def get_loan_duration():
    prompt(messages('yearly_loan_duration'))
    yearly_loan_duration = input()

    return yearly_loan_duration

def validate_loan_duration(yearly_loan_duration):
    if invalid_number(yearly_loan_duration):
        prompt(messages('invalid_number'))

def calculate_monthly_payment():
    annual_interest_rate = float(interest_rate) / 100
    monthly_interest_rate = float(annual_interest_rate) / 12
    months = float(yearly_loan_duration) * 12

    monthly_payment = (float(loan_amount) *
                           ((monthly_interest_rate) /
                            (1 - (1 + monthly_interest_rate) ** ((-months)))))
    
    return monthly_payment

def display_payment(monthly_payment):
    prompt(messages('monthly_payment', f'${round(monthly_payment,2)}'))


def calculate_again():
    prompt(messages('another_calculation'))
    answer = input().lower()

    return answer
    
def validate_response(answer):
    while True:
        if answer in ['y', 'yes'] or answer in ['n','no']:
            break

        prompt(messages('another_calculation'))
        answer = input().lower()

print()
prompt(messages('welcome'))
print()

while True:

    loan_amount = get_loan_amount()
    validate_loan_amount(loan_amount)

    interest_rate = get_interest_rate()
    validate_interest_rate(interest_rate)

    yearly_loan_duration = get_loan_duration()
    validate_loan_duration(yearly_loan_duration)

    monthly_payment = calculate_monthly_payment()
    display_payment(monthly_payment)

    print()
    answer = calculate_again()

    validate_response(answer)

    if answer in ['n','no']:
        break


# <======= CODE SKELETON ========>

# print()
# prompt(messages('welcome'))
# print()

# while True:

#     while True:
#         prompt(messages('loan_amount'))
#         loan_amount = input()

#         if not invalid_number(loan_amount):
#             break

#         prompt(messages('invalid_number'))

#     while True:
#         prompt(messages('interest_rate'))
#         interest_rate = input()

#         if not invalid_number(interest_rate):
#             break

#         prompt(messages('invalid_number'))

#     while True:
#         prompt(messages('yearly_loan_duration'))
#         yearly_loan_duration = input()

#         if not invalid_number(yearly_loan_duration):
#             break

#         prompt(messages('invalid_number'))

#     while True:
#         annual_interest_rate = float(interest_rate) / 100
#         monthly_interest_rate = float(annual_interest_rate) / 12
#         months = float(yearly_loan_duration) * 12

#         monthly_payment = (float(loan_amount) *
#                            ((monthly_interest_rate) /
#                             (1 - (1 + monthly_interest_rate) ** ((-months)))))

#         prompt(messages('monthly_payment', f'${round(monthly_payment,2)}'))
#         break

#     print()
#     prompt(messages('another_calculation'))
#     answer = input().lower()

#     while True:
#         if answer.startswith('n') or answer.startswith('y'):
#             break

#         prompt(messages('another_calculation'))
#         answer = input().lower()

#     if answer[0] =='n':
#         break
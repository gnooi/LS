# Question 1:
# Write a program named greeter.py. 
# The program should ask for your name, 
# then output Hello, NAME! where NAME is the name you entered

#NAME = input('What is your name? ')
#print(f'Hello, {NAME} !')

# Question 2:
# Modify the greeter.py program to ask for the user's first and last names separately, 
# then greet the user with their full name.

#first_name = input('What is your first name? ')
#last_name = input('What is your last name? ')
#full_name = first_name + ' ' + last_name

#print(f'Hello, {full_name}!')

# Question 3:
# Write a program named age.py that asks the user to enter their age, 
# then calculates and reports the future age 10, 20, 30, and 40 years from now. 
# Here's the output for someone who is 27 years old.

age = int(input('How old are you? '))
print(f'\nYou are {age} years old.')
age += 10
print(f'In 10 years, you will be {age} years old.')
age += 10
print(f'In 20 years, you will be {age} years old.')
age += 10
print(f'In 30 years, you will be {age} years old.')
age += 10
print(f'In 40 years, you will be {age} years old.')
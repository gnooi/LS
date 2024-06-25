# Question 1:
# Classify the following potential non-constant variable names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.

#index Idiomatic
#CatName Non-idiomatic
#lazy_dog Idiomatic
#quick_Fox Non-idiomatic 
#1stCharacter Illegal, starts with digit
#operand2 Idiomatic
#BIG_NUMBER Non-idiomatic
#π Non-idiomatic, not an ASCII character


# Question 2:
# Classify the following potential function names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.
# Answer will be same as above

#index
#CatName
#lazy_dog
#quick_Fox
#1stCharacter
#operand2
#BIG_NUMBER
#π

# Question 3:
# Classify the following potential constant names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.

#index Non-idiomatic, should not use lowercase letters
#CatName Non-idiomatic, should not use lowercase letters
#snake_case Non-idiomatic, should not use lowercase letters
#LAZY_DOG3 Idiomatic
#1ST Illegal, begins with a digit
#operand2 Non-idiomatic, should not use lowercase letters
#BIG_NUMBER Idiomatic
#Π Non-idiomatic, pi is not an ASCII character


# Question 4:
# Classify the following potential class names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.

#index, Non-idiomatic, no uppercase letter
#CatName, Idiomatic
#lazy_dog, Non-idiomatic, no uppercase letter
#quick_Fox, Idiomatic
#1stCharacter Illegal, should not begin with a digit
#operand2, Non-idiomatic, no uppercase letter
#BIG_NUMBER, Idiomatic
#π Non-idiomatic, pi is not an ASCII character

# Question 5:
# Write a program named greeter.py that greets 'Victor' three times. 
# Your program should use a variable and not hard code the string value 'Victor' in each greeting. 

name_Victor = 'Victor'
greeting_1 = 'Good Morning'
greeting_2 = 'Good Afternoon'
greeting_3 = 'Good Evening'

print(f'{greeting_1}, {name_Victor}.')
print(f'{greeting_2}, {name_Victor}.')
print(f'{greeting_3}, {name_Victor}.')

# Question 6: 
# Write a program named age.py that includes someone's age and then calculates 
# and reports the future age 10, 20, 30, and 40 years from now. 
# Here's the output for someone who is 22 years old.

age_now = 22
age_10yrs = age_now + 10
age_20yrs = age_now + 20
age_30yrs = age_now + 30
age_40yrs = age_now + 40

print("You are " f'{age_now}' " years old.")
print("In 10 years, you will be " f'{age_10yrs}' " years old.")
print("In 20 years, you will be " f'{age_20yrs}' " years old.")
print("In 30 years, you will be " f'{age_30yrs}' " years old.")
print("In 40 years, you will be " f'{age_40yrs}' " years old.")

# Correct Solution Below: 
# age = 22
# print(f'You are {age} years old.')
# print(f'In 10 years, you will be {age + 10} years old.')
# print(f'In 20 years, you will be {age + 20} years old.')
# print(f'In 30 years, you will be {age + 30} years old.')
# print(f'In 40 years, you will be {age + 40} years old.')


# Question 7:
# What happens when you run the following code? Why?
#   NAME = 'Victor'
#   print('Good Morning, ' + NAME)
#   print('Good Afternoon, ' + NAME)
#   print('Good Evening, ' + NAME)

#   NAME = 'Nina'
#   print('Good Morning, ' + NAME)
#   print('Good Afternoon, ' + NAME)
#   print('Good Evening, ' + NAME)

# Solution:
# Good Morning, Victor
# Good Afternoon, Victor
# Good Evening, Victor

# Good Morning, Nina
# Good Afternoon, Nina
# Good Evening, Nina

# Question 8:
# Challenge: This program uses a bit of math. Don't let that scare you away -- try it anyway.

# Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays 
# you 5% (this is a wish-fulfillment fantasy) compounded interest every year. After one year, 
# you will have $1,050 ($1,000 times 1.05). After two years, you will have $1,050 times 1.05, or $1102.50. 
# Create a variable named balance that contains the amount of money you will have after 5 years, then print the result. 
# Use a single expression if you can to set balance to the correct value.

balance_5yrs = (1000 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05)
print(balance_5yrs)

# Question 9:
# Repeat the previous question but, this time, use augmented assignment
# to compute the final result, one year at a time.

balance = 1000
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05

print(balance)


# Question 10:
# Assume that obj already has a value of 42 when the code below starts 
# running. Which of the subsequent statements reassign the variable? 
# Which statements mutate the value of the object that obj references? 
# Which statements do neither? If necessary, you can read the documentation.

obj = 'ABcd' # Reassigns
obj.upper() # Neither
obj = obj.lower() # Reassigns
print(len(obj)) # Neither
obj = list(obj) # Reassigns
obj.pop() # Mutates
obj[2] = 'X' # Mutates
obj.sort() # Mutates
set(obj) # Neither
obj = tuple(obj) # Reassigns
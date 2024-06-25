# Question 1:
# What happens when you run the following program? Why do we get that result?

#def set_foo(): # An error because foo variable is defined within a function.
    #foo = 'bar'

#set_foo()
#print(foo)

# Question 2:
# Take a look at this code snippet:

#foo = 'bar' # global scope

#def set_foo(): # local scope
    #foo = 'qux'

#set_foo() # variable foo = 'qux' is intialized; there are two foo variables, one in global scope and one in local scope. 
#print(foo) # prints bar only, foo in the global scope


# Question 3:
# Write a program that uses a multiply function to multiply two numbers and returns the result. 
# Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

number1 = float(input('Enter the first number: '))
number2 = float(input('Enter the second number: '))

def multiply(number1, number2):
    return number1 * number2

print(f'{number1} * {number2} =',multiply(number1,number2))

# Question 4:
# Consider this code:

def multiply_numbers(num1, num2, num3): # function definition & parameters
    result = num1 * num2 * num3 # body
    return result 

product = multiply_numbers(2, 3, 4) # function name, function arguments, function invocation

Identify the following items in that code:

Item
function name
function arguments
function definition
function body
function parameters
function invocation
function return value # 24
all identifiers # multiply_numbers, num1, num2, num3, result, and product

# Question 5: 
# What does the following code print?

def scream(words):
    return words + '!!!!'

scream('Yipeee') 

# Does not print anything because print() function is not invoked. However, return value is 'Yipeee!!!!'

# Question 6:
# What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

# Does not print anything because return terminates the function before it can print anything.

# Question 7:
# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# Does not print, will raise an error because it's missing an argument for parameter 'qux'

# Question 8:
# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# Raise an error due to extra argument)


# Question 9:
# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# Prints 42, 3.141592, 2.718 because Python ignores the default since 3 arguments are provided. 
# Default values are used when no arguments are provided for the second & third numbers.

# Question 10:
# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# Prints 42, 3.141592, 2

# Question 11:
# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# Prints 42, 3, 2

# Question 12:
# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# Does not print because it is missing an argument for the first parameter

# Question 13:
# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# Does not print because it is missing an argument for the third parameter...default values need to be defined at the end of the list


# Question 14:
# Identify all of the identifiers on each line of the following code.

def multiply(left, right): # multiply, left, right
    return left * right # left, right

def get_num(prompt): # get_num, prompt 
    return float(input(prompt)) # float, prompt 

first_number = get_num('Enter the first number: ') # first_number, get_num
second_number = get_num('Enter the second number: ') # second_number, get num
product = multiply(first_number, second_number) # product, multiply
print(f'{first_number} * {second_number} = {product}') # print, first_number, second_number, product

# Question 15:
# Using the code below, classify the identifiers as global, local, or built-in. 
# For our purposes, you may assume this code is the entire program.

def multiply(left, right): 
    return left * right 

def get_num(prompt): 

    return float(input(prompt)) 

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Global: multiply, get_num, first_number, second_number, product

# Local: left, right, prompt

# Built-in: input, float, print

# Question 16:
# In the code shown below, identify all of the function names and parameters present in the code. 
# Include the line numbers for each item identified.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Function names: multiply(), get_num(), float(), input() print()
# Parameters: left, right, prompt

# Question 17:
# Which of the identifiers in the following program are function names? 
# Which are method names? Which are built-in functions?

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# Function names: say(), print(), input(), max()
# Method names: string1.upper(), string2.lower()


# Question 18: 
# The following function returns a list of the remainders of dividing the numbers in numbers by 3:

def remainders_3(numbers):
    return [number % 3 for number in numbers]

#Use this function to determine which of the following lists contains at least one number that 
# is not evenly divisible by 3 (that is, the remainder is not 0):

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(any(remainders_3(numbers_1))) # True
print(any(remainders_3(numbers_2))) # True
print(any(remainders_3(numbers_3))) # False
print(any(remainders_3(numbers_4))) # False


# Question 19:
# The following function returns a list of the remainders of dividing the numbers in numbers by 5:

def remainders_5(numbers):
    return [number % 5 for number in numbers]

#Use this function to determine which of the following lists do not contain any numbers 
# that are divisible by 5:

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainders_5(numbers_1))) # False
print(all(remainders_5(numbers_2))) # True
print(all(remainders_5(numbers_3))) # False
print(all(remainders_5(numbers_4))) # True
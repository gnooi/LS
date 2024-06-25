# Question 1:

False or (True and False) # False
True or (1 + 2) # True 
(1 + 2) or True # 3
True and (1 + 2) # 3
False and (1 + 2) # False
(1 + 2) and True # True
(32 * 4) >= 129 # False
False != (not True) # False
True == 4 # False
False == (847 == '847') # True


# Question 2:

def even_or_odd(number)
    if even_or_odd % 2 == 0:
        print('even')
    else:
        print('odd')

# Question 3:
# Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113') # prints Product2
bar_code_scanner(142) # prints Product not found!


# Question 4:
# Refactor this statement to use a regular if statement instead.

return('bar' if foo() else qux())

if foo():
    return 'bar'
else:
    return qux()

# Question 5: 
# What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

# prints Empty...because the argument empty collection [] is falsy based on the table with built-in falsy values.

# Question 6:
# Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer than 10 characters. 
# Otherwise, it should return the original string. Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

def string_10(prompt):
    if len(prompt) > 10:
        return prompt.upper()
    else:
        return prompt

print(string_10('hello world'))
print(string_10('goodbye'))

# Question 7:
# Write a function that takes a single integer argument and prints a message that describes whether:

# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0

def number_range(number):
    if 0 <= number <= 50:
        print(number, 'is between 0 and 50')
    elif 51 <= number <= 100:
        print(number, 'is between 51 and 100')
    elif number > 100:
        print(number, 'is greater than 100')
    elif number < 0:
        print(number, 'is less than 0')

number_range(0)    # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0
# Truthy vs. Falsy:
# Built-in Falsy values: 
# Empty collections: [], (), {}, set(), frozenset(), and range(0)
# False, None, all number 0 values (integers, floats, complex, 
# Empty Strings: ''
# Custom data types can also define additional falsy value(s)

# Yes? No? Part 1
# The code provided below randomly initializes random_number to either 0 or 1 each time it is executed.

# Write an if statement that prints Yes! if random_number is 1, and No. if random_number is 0.

# import random
# random_number = random.randint(0, 1)

# if random_number == 1:
#     print('Yes!')
# else:
#     print('No.')

# Yes? No? Part 2 (conditional expression)

# print('Yes!') if random_number == 1 else print('No.')

# Check the Weather, Part 1
# Initialize a variable weather with a string value being 'sunny', 'rainy', or whatever weather condition you choose. Then, write an if statement that prints:

# It's a beautiful day! if weather's value is 'sunny'
# Grab your umbrella. if weather's value is 'rainy'
# Let's stay inside. if weather's value is anything else
# Test your code with different values for weather.

# weather = 'sunny'

# if weather == 'sunny':
#     print("It's a beautiful day!")
# elif weather == 'rainy':
#     print('Grab your umbrella')
# else:
#     print("Let's stay inside.")

# Match-Case
# Examine the code shown below. 
# Without running it, determine what it will print. If you're not sure, refer to our Python book.
# It will print neigh
# animal = 'horse'

# match animal:
#     case 'duck':
#         print('quack')
#     case 'squirrel':
#         print('nook nook')
#     case 'horse':
#         print('neigh')
#     case 'bird':
#         print('tweet tweet')
#     case _:
#         print('*cricket*')

# Check the Weather, Part 2
# Take your code from the previous Check the Weather exercise and 
# rewrite it as a match-case statement. Feel free to add more cases besides 'sunny' and 'rainy'.

# weather = 'ggg'

# match weather:
#     case 'sunny':
#         print("It's a beautiful day.")
#     case 'rainy':
#         print('Grab your umbrella')
#     case 'snowy':
#         print('Come out and play!')
#     case _:
#         print("Let's stay inside.")

# Logical Conditions 1
# Predict the output of the following code:

# if False or True:
#     print('Yes!')
# else:
#     print('No...')

# # Prints Yes! since the condition will always evaluate to be Truthy

# Logical Conditions 2
# Predict the output of the following code:

# if True and False:
#     print('Yes!')
# else:
#     print('No...')

# Prints No... since the condition will always evaluate to be Falsy

# Logical Conditions 3
# Without running the following code, determine what will be printed.
# sale = True
# admission_price = 5.25 if not sale else 3.99

# print(f"${admission_price}")

# Prints 3.99

# Are we moving?
# Determine what the following code snippet prints. 
# First solve it in your head or on paper, then run it in your Python environment to check the result.

# speed = 0
# acceleration = 24
# braking_force = 19
# is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
# print(is_moving)

# True


# Bonus question: Do we need the parentheses in the boolean expression or could we have written the following?:

# is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
# Parentheses are needed, despite and having a higher precedence than or...the values for speed, acceleration, and braking_force variables may change, 
# affecting the output. 
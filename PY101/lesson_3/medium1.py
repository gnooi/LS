# Question 1:
# Let's do some "ASCII Art": a stone-age form of nerd artwork 
# from back in the days before computers had video screens.

# For this practice problem, write a program that outputs 
# The Flintstones Rock! 10 times, with each line prefixed 
# by one more hyphen than the line above it. The output should
# start out like this:

# -The Flintstones Rock!
# --The Flintstones Rock!
# ---The Flintstones Rock!
#     ...

# old_flintstones = "The Flintstones Rock!"

# for number in range(0,10):
#     old_flintstones = '-' + old_flintstones
#     print(old_flintstones)

# for padding in range(1, 11):
#     print(f'{"-" * padding}The Flintstones Rock!')

# <=================>

# Question 2:
# Alan wrote the following function, which was intended 
# to return all of the factors of number:

# def factors(number):
#     divisor = number
#     result = []
#     while divisor > 0: # additional expression
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result

# Alyssa noticed that this code would fail when the input 
# is a negative number, and asked Alan to change the loop. 
# How can he make this work? Note that we're not looking to 
# find the factors for negative numbers, but we want to handle
# it gracefully instead of going into an infinite loop.

# Bonus Question: What is the purpose of number % divisor == 0 
# in that code?

# The purpose of number % divisor == 0 is to check whether the result
# of the divison is an integer -- if the number has no remainder, 
# the result is an integer, so the number divided by the divisor
# is a factor. 

# factors_of_9 = factors(-9)
# print(factors_of_9)

# <=================>

# Question 3:
# Alyssa was asked to write an implementation of a rolling
# buffer. You can add and remove elements from a rolling buffer.
# However, once the buffer becomes full, any new elements 
# will displace the oldest elements in the buffer.

# She wrote two implementations of the code for adding 
# elements to the buffer:


# def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
#     buffer.append(new_element)
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer

# def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
#     buffer = buffer + [new_element]
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer

# Is there a difference between these implementations, 
# other than the way she is adding an element to the buffer?

# Yes, the difference between the two functions is that add_to_rolling_buffer1
# mutates the original buffer list with the .append method to add the new element. 
# However, add_to_rolling_buffer2 does not mutate the original list, but instead 
# creates a new list and assigns it to buffer, whose value ultimately
# gets returned by the function. 

# <=================>

# Question 4:
# What will the following two lines of code output?

# print(0.3 + 0.6)
# print(0.3 + 0.6 == 0.9)

# Don't look at the solution before you answer.

# 0.8999999999999999
# False

# Python uses floating point numbers for all numeric operations. 
# Most floating point representations used on computers lack a 
# certain amount of precision and can yield unexpected results like
# these. In order to product 0.9 and True, use the math.isclose function
# to do so. 

# <=================>

# Question 5:
# What do you think the following code will output?

# nan_value = float("nan")

# print(nan_value == float("nan"))

# False. nan -- not a number is a special numeric value that indicates
# that an operation that was intended to return a number failed. 
# Python doesn't let you use == to determine whether a value is nan. 

# Bonus Question
# How can you reliably test if a value is nan?

# Use math.isnan() function to test for NaNs. 

# <=================>

# Question 6
# What is the output of the following code?

# answer = 42

# def mess_with_it(some_number):
#     return some_number + 8

# new_answer = mess_with_it(answer)

# print(answer - 8)

# The output is 34. There is no answer variable in the mess_with_it function
# so, therefore answer -  8, references the global variable answer 42.

 # <=================>

# Question 7:
# One day, Spot was playing with the Munster family's home 
# computer, and he wrote a small program to mess with their 
# demographic data:

# munsters = {
#     "Herman": {"age": 32, "gender": "male"},
#     "Lily": {"age": 30, "gender": "female"},
#     "Grandpa": {"age": 402, "gender": "male"},
#     "Eddie": {"age": 10, "gender": "male"},
#     "Marilyn": {"age": 23, "gender": "female"},
# }

# def mess_with_demographics(demo_dict):
#     for key, value in demo_dict.items():
#         value["age"] += 42
#         value["gender"] = "other"

# After writing this function, he typed the following code:

# mess_with_demographics(munsters)

# Before Grandpa could stop him, Spot hit the Enter key 
# with his tail. Did the family's data get ransacked? Why or why not?

# Yes, the family's data get ransacked. In Python, dictionaries
# are mutable, and when passed to a function, a reference to the dictionary
# is passed, not a copy. The parameter demo_dict starts off pointing to
# the munsters object, and as a result changes made within the function
# directly affect the munsters dictionary. The nested dictionaries are
# the ones being mutated, so each family member's dictionary age and gender
# is accessed and modified. Since the nested dictionaries are part of the larger
# munsters dictionary, the changes are reflected in the original data structure. 

 # <=================>

# Question 8:
# Function and method calls can take expressions as arguments. 
# Suppose we define a function named rps as follows, which follows 
# the classic rules of the rock-paper-scissors game, but with a 
# slight twist: in the event of a tie, it just returns the choice 
# made by both players.

# def rps(fist1, fist2):
#     if fist1 == "rock":
#         return "paper" if fist2 == "paper" else "rock"
#     elif fist1 == "paper":
#         return "scissors" if fist2 == "scissors" else "paper"
#     else:
#         return "rock" if fist2 == "rock" else "scissors"
    
# What does the following code output?

# print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

# paper

 # <=================>

# Question 9:
# Consider these two simple functions:


def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"

# What will the following function invocation return?

print(bar(foo())) 

# prints no because and and or are short circuit operators, so
# when the left side of or evaluates to False, Python returns the right 
# side of the or, which is "no"

 # <=================>

# Question 10:
# In Python, every object has a unique identifier that 
# can be accessed using the id() function. This function 
# returns the identity of an object, which is guaranteed to 
# be unique for the object's lifetime. For certain basic immutable
# data types like short strings or integers, Python might 
# reuse the memory address for objects with the same value. 
# This is known as "interning".

# Given the following code, predict the output:

a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# True, a and c reference the same object in memory, so their ids
# are the sam. b will, in this case have the same if as a and c
# due to interning. Therefore, the code will output True. 


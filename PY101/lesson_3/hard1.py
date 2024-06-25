# Question 1:
# Will the following functions return the same results?

# def first():
#     return {
#         'prop1': "hi there",
#     }

# def second():
#     return
#     {
#         'prop1': "hi there",
#     }

# print(first()) # prop1: hi there, returns expected value
# print(second()) # None, the return block is AFTER the return statement
# # Try to answer without running the code or looking at the solution.

 # <=================>

# Question 2
# What does the last line in the following code output?

# dictionary = {'first': [1]}
# num_list = dictionary['first']
# num_list.append(2)

# print(num_list) # [1, 2], num_list is a reference to the original list
# # in dictionary, appending to num_list modifies the list. Thus, the original
# # dictionary is also updated. 

# print(dictionary) # {'first': [1, 2]}, since dictionary is a mutable
# # data type, when dictionary['first']'s value is mutated, the original
# # object is changed as well. 

# Try to answer without running the code or looking at the solution.


 # <=================>

# Question 3:
# Given the following similar sets of code, what 
# will each code snippet print?

# Local variables inside the function overshadow the variables
# outside the function with the same names

# A) Since variables one, two, and three in the mess_with_vars function
# are local, reassigning them does not affect the original lists.

# def mess_with_vars(one, two, three):
#     one = two
#     two = three
#     three = one

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three) 

# print(f"one is: {one}") # one is: ['one']
# print(f"two is: {two}") # two is: ['two']
# print(f"three is: {three}") # three is: ['three']

# B) Again, the local variables in the mess_with_vars function are being
# reassigned by this doesn't change the original lists.

# def mess_with_vars(one, two, three):
#     one = ["two"]
#     two = ["three"]
#     three = ["one"]

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}") # one is: ['one']
# print(f"two is: {two}") # two is: ['two']
# print(f"three is: {three}") # three is: ['three']

# C) mess_with_vars function modifies the content of the lists directly.
# Since lists in Python are mutable and passed by reference, the 
# changes are reflected outside the function

# def mess_with_vars(one, two, three):
#     one[0] = "two"
#     two[0] = "three"
#     three[0] = "one"

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}") # one is: ['two']
# print(f"two is: {two}") # two is: ['three']
# print(f"three is: {three}") # three is: ['one']

 # <=================>

# Question 4:
# Ben was tasked to write a simple Python function to
# determine whether an input string is an IP address using 
# 4 dot-separated numbers, e.g., 10.4.5.11.

# Alyssa supplied Ben with a function named is_an_ip_number.
# It determines whether a string is a numeric string between 0 
# and 255 as required for IP numbers and asked Ben to use it. 
# Here's the code that Ben wrote:

# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".")
#     while len(dot_separated_words) == 4:
#         word = dot_separated_words.pop()
#         if not is_an_ip_number(word):
#             break
#         else:
#             return True
#     return False
         

# Alyssa reviewed Ben's code and said, "It's a good start, 
# but you missed a few things. You're not returning a false 
# condition, and you're not handling the case when the input 
# string has more or less than 4 components, e.g., 4.5.5 or 
# 1.2.3.4.5: both those values should be invalid."

# Help Ben fix his code.

# def is_an_ip_number(str):
#     if str.isdigit():
#         number = int(str)
#         return 0 <= number <= 255
#     return False

# print(is_dot_separated_ip_address('10.4.5.11'))
# print(is_dot_separated_ip_address('4.5.5'))
# print(is_dot_separated_ip_address('1.2.3.4.5:'))
# print(is_dot_separated_ip_address('257'))

 # <=================>
# Question 5: 
# What do you expect to happen when the greeting variable 
# is referenced in the last line of the code below?

# if False:
#     greeting = "hello world"

# print(greeting)

# The print line will output an NameError because the if conditional
# will never execute since False is a falsy value, and therefore, 
# the greeting variable defined in the block is never initialized.
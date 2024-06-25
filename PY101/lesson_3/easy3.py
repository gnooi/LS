# Question 1:
# Write two different ways to remove all of the elements
# from the following list:

# numbers = [1, 2, 3, 4]

# numbers.clear()
# del numbers[:]

# while numbers:
#     numbers.pop()

# <=================>

# Question 2:
# What will the following code output?

# print([1, 2, 3] + [4, 5])

# Try to answer without running the code.
# [1, 2, 3, 4, 5] # List concatenation, produces a new combined list

# <=================>

# Question 3:
# What will the following code output?

# str1 = "hello there"
# str2 = str1
# str2 = "goodbye!"
# print(str1)

# Try to answer without running the code.
# hello there # str1 remains as is. In Python, strings are 
# immutable, so there is no way to change str1 unless it is
# reassigned. Wehn str2 = str2, str2 variable is pointing to
# the same memory location as str1. Once str2 is reassigned, 
# it changes what memory location it points to but not the value
# of str1. 


# <=================>

# Question 4:
# What will the following code output?

# my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
# my_list2 = my_list1.copy()
# my_list2[0]['first'] = 42
# print(my_list1)

# Try to answer without running the code.
# {"first": "42"}, {"second": "value2"}, 3, 4, 5] # When my_list2 is 
# assigned to a shallow copy of my_list1, my_list1 and my_list2
# point to the same dictionary in memory. Although, they are 2 different
# lists, they still point to one occurence of the outermost
# values in an object. So when my_list2[0]['first'] is replaced with
# 42, it shows up in my_list1 as well. A deep copy would have 2 different
# lists and 4 separate dictionaries. A shallow copy only makes
# a duplicate of the outermost values in an object. 

# <=================>

# Question 5:
# The following function unnecessarily uses two return 
# statements to return boolean values. Can you rewrite this 
# function so it only has one return statement and does not 
# explicitly use either True or False?

# def is_color_valid(color):
#     if color == "blue" or color == "green":
#         return True
#     else:
#         return False
    
# def is_color_valid(color):
#     return "blue" in color or "green" in color
    
# def is_color_valid(color):
#     return color == "blue" or color == "green"
        
    
# print(is_color_valid('yellow'))
# # Try to come up with two different solutions.


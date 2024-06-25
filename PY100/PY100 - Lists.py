# First Element
# Write a function that returns the first element of a list provided as an argument. For example:

# def first(list):
#     if list:
#         return list[0]
#     else:
#         return None
# print(first(['Earth', 'Moon', 'Mars']))  # Earth
# Be sure to handle the case where the input list is empty.

# Last Element
# Write a function that returns the last element of a list provided as an argument. For example:

# def last(list):
#     if list:
#         return list[-1]
#     else:
#         return None

# print(last(['Earth', 'Moon', 'Mars']))  # Mars
# Be sure to handle the case where the input list is empty.

# Add + Delete
# We are given the following list of energy sources.


# energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
# energy.remove('fossil')
# energy.append('geothermal')
# print(energy)
# Write some code to remove 'fossil' from the list, then add 'geothermal' to the end of the list

# Split the string alphabet into a list of characters.

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# lst = list(alphabet)
# print(lst)

# Filter
# Count the number of elements in scores that are 100 or above.

# scores = [96, 47, 113, 89, 100, 102]
# count = 0
# for number in scores:
#     if number >= 100:
#         count += 1
#     else:
#         continue
# print(count)

# You've been given a list of vocabulary words grouped into sub-lists, 
# by meaning. This is a two-dimensional list or a nested list. 
# Write some code that iterates through and prints all the words, 
# one per line.

# vocabulary = [
#     ['happy', 'cheerful', 'merry', 'glad'],
#     ['tired', 'sleepy', 'fatigued', 'drained'],
#     ['excited', 'eager', 'enthused', 'animated'],
# ]

# for lst in vocabulary:
#     for sublst in lst:
#         print(sublst)

# Equality
# Predict the output of the code shown below. 
# When you run the code, do you see what you expected? 
# Why or why not?
# Will print true because the values are equal, however the lists point to two different objects so the is operator will return False.

# list1 = [2, 6, 4]
# list2 = [2, 6, 4]

# print(list1 == list2)

# Type
# How can you check if a variable holds a value that is a list? 
# Given two variables, verify whether the values they hold are lists.
# To check if a variable holds a value that is a list, use isinstance()

# some_value1 = [0, 1, 0, 0, 1]
# some_value2 = 'I leave you my Kingdom, take good care of it.'

# print(isinstance(some_value1,list))
# print(isinstance(some_value2,list))

# Travel
# The destinations list contains a list of travel destinations.

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

# Write a function that, without using the built-in in operator,
# checks whether a specific destination is included within destinations. 
# For example: When checking whether 'Barcelona' is contained in 
# destinations, the expected output is True, whereas the expected 
# output for 'Nashville' is False.


# def contains(str,lst):
#     for city in destinations:
#         if city == str:
#             return 'True'
        
#     return 'False'

# print(contains('Barcelona', destinations))  # True
# print(contains('Nashville', destinations))  # False


# Passcode
# We generated parts of a passcode and now want to combine 
# them into a string. Write some code that returns a string, 
# with each portion of the passcode separated by a hyphen (-).

# passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
# str = '-'.join(passcode)
# print(str)

# Expected return value: '11-jZ5-hQ3f*-8!7g3-p3Fs'

# Checking items off the grocery list
# We have a grocery list. As we check off items on that list, we want to remove them from the list.

# Write code that removes the items from grocery_list, 
# one by one, until it is empty. If you print the elements you remove,
# the expected behavior would look as follows.

# grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
#                 'carrots', 'broccoli', 'hummus']

# # Your code.

# while grocery_list:
#     checked_item = grocery_list.pop(0)
#     print(checked_item)

# print(grocery_list)




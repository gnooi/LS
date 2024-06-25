# Question 1:
# The following code causes an infinite loop (a loop that never stops iterating). Why?

# counter = 0

# while counter < 5:
    # print(counter)

# The block is missing a conditional expression for counter that would make the loop condition falsy, and therefore trigger it to end. 

# Question 2:
# Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. The updated code should use a for loop to display the future ages.

# age = int(input('How old are you? '))
# print(f'\nYou are {age} years old.')
# print()

# for future_age in range(10,50,10):
#     print(f'In {future_age} years, you will be'
#           f'{age + future_age} years old')


# Question 3:
# Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a for loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

# counter = 0
# while counter < len(my_list):
#     print(my_list[counter])
#     counter += 1

# for number in my_list:
#     print(number)

# Question 4:
# Use a while loop to print all numbers in my_list with even values, one number per line. Then, print the odd numbers using a ' for' loop.

# index = 0
# while index < len(my_list):
#     if my_list[index] % 2 == 0:
#         print(my_list[index])
#     index += 1

# for number in my_list: 
#     if not number % 2 == 0:
#         print(number)

# Question 5:
# Print all of the even numbers in the following list of nested lists. Don't use any while loops.

# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]

# for nested_list in my_list:
#     for number in nested_list:
#         if number % 2 == 0:
#             print(number)

# Question 6:
# Let's try another variation on the even/odd-numbers theme.

# We'll return to the simpler one-dimensional version of my_list. 
# In this problem, you should write code that creates a new list with one element for each number in my_list. 
# If the original number is an even, then the corresponding element in the new list should contain the string 'even'; 
# otherwise, the element should contain 'odd'.

# my_list = [
#     1, 3, 6, 11,
#     4, 2, 4, 9,
#     17, 16, 0,
# ]

# result = []
# for number in my_list:
#     if number % 2 == 0 :
#         result.append('even')
#     else:
#         result.append('odd')

# print(result)

# Question 7:
# Write a find_integers function that returns a list of all the integers from my_tuple:


# my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#             -4, None, {1, 2, 3}, False)

# def find_integers(things):
#     return [element 
#             for element in things
#             if type(element) is int ]

# integers = find_integers(my_tuple)
# print(integers)    

# Question 8:
# Write a comprehension that creates a dict object whose keys are strings and whose values are the length of the corresponding key. 
# Only keys with odd lengths should be in the dict. 
# Use the set given by my_set as the source of strings.

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}
# # for key in my_set:
# #     if len(key) % 2 != 0:
# #         result = (key, len(key))

# result = {key : len(key)
#           for key in my_set
#           if (len(key) % 2 != 0)}

# print(result)

# Question 9:
# Write a function that computes and returns the factorial of a number by using a for or while loop. The factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n, inclusive:

# n!	Expansion	Result
# 1!	1	1
# 2!	1 * 2	2
# 3!	1 * 2 * 3	6
# 4!	1 * 2 * 3 * 4	24
# 5!	1 * 2 * 3 * 4 * 5	120
# You may assume that the argument is always a positive integer.

# print(factorial(1))   # 1
# print(factorial(2))   # 2
# print(factorial(3))   # 6
# print(factorial(4))   # 24
# print(factorial(5))   # 120
# print(factorial(6))   # 720
# print(factorial(7))   # 5040
# print(factorial(8))   # 40320
# print(factorial(25))  # 15511210043330985984000000

# def factorial(n):
#     result = 1
#     for n in range(n, 0, -1):
#         result *= n
#     return result

# def factorial(n):
#     result = 1
#     while n > 0:
#         result *= n
#         n -= 1
#     return result

# print(factorial(1))

# Question 10:
# import random

# highest = 10

# while True:
#     number = random.randrange(highest + 1)
#     print(number)
#     if number == highest:
#         break

# Question 11:
# Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer_index = 0
while outer_index < len(my_list):
    inner_index = 0
    while inner_index < len(my_list[outer_index]):
        number = my_list[outer_index][inner_index]
        if number % 2 == 0:
            print(number)

        inner_index += 1
    outer_index += 1

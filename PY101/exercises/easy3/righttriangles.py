# Write a function that takes a positive integer, n, as an argument 
# and prints a right triangle whose sides each have n stars. 
# The hypotenuse of the triangle (the diagonal side in the images below)
# should have one end at the lower-left of the triangle, and the other
# end at the upper-right.

# <=== LS ANSWER ===>

def triangle(height):
    for num in range(1, height + 1):
        spaces = height - num
        stars = num
        print(f'{" " * spaces}{"*" * stars}')


# <=== MY ANSWER ===>

# def triangle(n):
#     result = ''
#     char = '*'
#     space = ' '
#     counter = 1
#     for index in range(n, 0, -1):
#         result = (space * index) + (char * counter)
#         counter += 1
#         print(result)

# range(n - 1, 1, -1)
# Example 1
triangle(5)

# Output for Example 1
#     *
#    **
#   ***
#  ****
# *****

# Example 2
triangle(9)

# Output for Example 2
#         *
#        **
#       ***
#      ****
#     *****
#    ******
#   *******
#  ********
# *********
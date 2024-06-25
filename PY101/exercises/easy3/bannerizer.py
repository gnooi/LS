# Bannerizer
# Write a function that takes a short line of text and prints it 
# within a box.

# <=== LS ANSWER ===>

# def print_in_box(message):
#     horizontal_rule = f'+-{"-" * len(message)}-+'
#     empty_line = f'| {" " * len(message)} |'

#     print(horizontal_rule)
#     print(empty_line)
#     print(f'| {message} |')
#     print(empty_line)
#     print(horizontal_rule)

# <=== MY ANSWER ===>

# def print_in_box(text):
#         if not len(text):
#             print('+' + '--' + '+')
#             print('|' + '  ' + '|')
#             print('|' + '  ' + '|')
#             print('|' + '  ' + '|')
#             print('+' + '--' + '+')
#         else:
#             print('+' + '-' * len(text) + '+')
#             print('|' + ' ' * len(text) + '|')
#             print('|' + text + '|')
#             print('|' + ' ' * len(text) + '|')
#             print('+' + '-' * len(text) + '+')


# Further Exploration
# Modify this function so that it truncates the message if it doesn't 
# fit inside a maximum width provided as a second argument (the width 
# is the width of the box itself). You may assume no maximum if the 
# second argument is omitted.


def print_in_box(message, max_width=0):
    if max_width > 0:
        message = message[:max_width]
        horizontal_rule = f'+-{"-" * len(message)}-+'
        empty_line = f'| {" " * len(message)} |'
    else:
        horizontal_rule = f'+-{"-" * len(message)}-+'
        empty_line = f'| {" " * len(message)} |'

    print(horizontal_rule)
    print(empty_line)
    print(f'| {message} |')
    print(empty_line)
    print(horizontal_rule)


# For a challenging but fun exercise, try word wrapping messages that 
# are too long to fit, so that they appear on multiple lines but are
# still contained within the box. This isn't an easy problem, but it's
# doable with basic Python.


# Example 1
print_in_box('To boldly go where no one has gone before.')

# Output for Example 1
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

# Example 1
print_in_box('')
# Output for Example 2
# +--+
# |  |
# |  |
# |  |
# +--+
# You may assume the output will always fit in your terminal window.
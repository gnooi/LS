# Write a function that takes one argument, a positive integer, and 
# returns a string of alternating '1's and '0's, always starting
# with a '1'. The length of the string should match the given 
# integer.

# <=== LS ANSWER ===>

def stringy(size):
    result = ""
    for idx in range(size):
        digit = '1' if idx % 2 == 0 else '0'
        result += digit

    return result

# def stringy(size):
#     result = ""
#     for index in range(size):
#         if index % 2 == 0:
#             digit = '1'
#             result += digit
#         else:
#             digit = '0'
#             result += digit
#     return result 

# <=== MY ANSWER ===>

# def stringy(number):
#     new_string = '1'
#     for index in range(1, number):
#         if new_string[-1] == '0':
#             new_string += '1'
#         elif new_string[-1] == '1':
#             new_string += '0' 

#     return new_string

# Examples
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
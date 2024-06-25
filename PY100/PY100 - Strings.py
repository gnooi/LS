# Determine the length of the string "These aren't the droids you're looking for.".
# print(len("These aren't the droids you're looking for."))

# ALL CAPS
# Convert the string 'confetti floating everywhere' to all upper case.
# str1 = 'confetti floating everywhere'
# print(str1.upper)

# Ignoring Case
# Using the following code, compare the value of name with the 
# string 'RoGeR' while ignoring the case of both strings. 
# Print true if the values are the same; print false if they aren't. 
# Next, perform a case-insensitive comparison between the value of name and the string 'DAVE'.

# str1 = 'RoGeR'
# name = 'Roger'

# if str1.casefold() == name.casefold():
#     print('True')
# else:
#     print('False')

# str2 = 'DAVE'

# print(name is str2)

# Multiline String
# How can you assign the following rhyme to a single variable 
# while preserving the line break?

# str1 = 'A pirate I was meant to be!\nTrim the sails and roam the sea!'
# print(str1)
# A pirate I was meant to be!
# Trim the sails and roam the sea!


# Write code that checks whether the string char_sequence contains the character x.

# char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

# print('x' in char_sequence)

# Is Empty?
# Write a function that checks whether a string is empty or not. For example:

# def is_empty(str):
#     return len(str) == 0

# print(is_empty('mars'))  # False
# print(is_empty('  '))    # False
# print(is_empty(''))    

# Is Empty or Blank?
# Write an is_empty_or_blank function to determine whether a string is either empty or consists entirely of spaces. For example:

# def is_empty_or_blank(str):
#     return len(str) == 0 or str.isspace()

# print(is_empty_or_blank('mars'))  # False
# print(is_empty_or_blank('  '))    # True
# print(is_empty_or_blank(''))      # True

# Capitalize Words
# Write code that capitalizes the words in the string 'launch school 
# tech & talk', so that you get the string 'Launch School Tech & Talk'.

# str1 = 'launch school tech & talk'
# print(str1.title())

# Check Prefix
# Write a function that checks whether a string starts with a 
# specific prefix.

# def starts_with(str1, str2):
#     return str1.startswith(str2)


# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True

# Count Substrings
# Write a function that counts the number of occurrences of a substring in a string.

# def count_substrings(string,substring):
#     return string.count(substring)

# print(count_substrings("lemon lemon lemon", "lemon")) # 3
# print(count_substrings("laLAlaLA", "la")) # 2
# print(count_substrings("launch", "uno")) # 0
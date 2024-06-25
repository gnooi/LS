# Short Long Short
# Write a function that takes two strings as arguments, 
# determines the length of the two strings, and then 
# returns the result of concatenating the shorter string, 
# the longer string, and the shorter string once again. 
# You may assume that the strings are of different lengths.

def short_long_short(str1, str2):
    str1_length = len(str1)
    str2_length = len(str2)

    if str1_length >= str2_length:
        return str2 + str1 + str2
    elif str1_length <= str2_length:
        return str1 + str2 + str1

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")


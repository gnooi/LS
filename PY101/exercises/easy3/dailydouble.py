# Write a function that takes a string argument and returns a 
# new string that contains the value of the original string with 
# all consecutive duplicate characters collapsed into a single 
# character.

def crunch(text):
    if not text:
        return text

    new_text = text[0]
    for ch in text:
        if ch == new_text[-1]:
            continue

        new_text += ch

    return new_text

# Examples
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')


# Further Exploration
# Regular expressions are also available in Python through the re 
# module. If you're familiar with regular expressions, you can try 
# to solve this problem using that module. Additionally, can you 
# think of any other solutions that don't involve regular expressions,
# perhaps using Python's built-in string or list methods?


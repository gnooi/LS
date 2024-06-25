# Question 1:
# Write Python code to print the seventh number of range(0, 25, 3).

my_range = (range(0,25,3))
print(my_range[6])

# Question 2: 
# Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

string_str = 'Launch School'
print(string_str[4:10])

# Question 3:
# Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from the original. It should also exclude the first and last members of the original. The result should be the tuple (4, 3, 2).

tuple_a = (1, 2, 3, 4, 5)
tuple_a = list(tuple_a)
print(tuple_a.reverse())
print(tuple(tuple_a[1:len(tuple_a)-1]))

# Question 4:
# This is a 3-part question. Consider the following dictionary:

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}
# Part 1: Write some code to print Bark by accessing the element associated with the key Dog.

print(pets['Dog'])

#Part 2: Write some code to print None when you try to print the value associated with the non-existent key, Lizard.

print(pets.get('Lizard'))

#Part 3: Write some code to print <silence> when you try to print the value associated with the non-existent key, Lizard.

print(pets.get('Lizard', '<silence>'))

# Question 5:

# Which of the following values can't be used as a key in a dict object, and why?

'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b'] # Cannot be used because lists are mutable 
{'a': 1, 'b': 2} # Cannot be used because dicts are mutable
range(5)
{1, 4, 9, 16, 25} # Cannot be used because sets are mutable
3
0.0
frozenset({1, 4, 9, 16, 25}) 

# All remaining items are immutable built-in objects that are acceptable dict keys.

# Question 6:
# What will the following code print?

print('abc-def'.isalpha()) # False: '-' is not a letter
print('abc_def'.isalpha()) # False: '_' is not a letter
print('abc def'.isalpha()) # False: space is not a letter
print('abc def'.isalpha() and # False
      'abc def'.isspace())
print('abc def'.isalpha() or # False
      'abc def'.isspace())
print('abcdef'.isalpha()) # True
print('31415'.isdigit()) # True
print('-31415'.isdigit()) # False: '-' is not a digit
print('31_415'.isdigit()) # False: '_' is not a digit
print('3.1415'.isdigit()) # False: '.' is not a digit
print(''.isspace()) # False: string is empty

# Question 7:
# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

parts = info.split(':')
result = '+'.join(parts)
print(result)

print(info.replace(':', '+'))

# Question 8:
# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# First print extracts a slice from text ranging from index 21 through index 35. 
# It returns a string 'for the fjords', but rfind searches on the right most side (back of the string)

# Second print searches the same range, however, we're searching the original string which has previous indices in the string. 

# Question 9:
# Write some code to replace the value 6 in the following nested list with 606:

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606

print(stuff)

# Question 10:
# Consider the following nested collection:

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

# Question 11:
# Without running the following code, determine what each line should print.

print('johnson' in 'Joe Johnson') # False
print('sen' not in 'Joe Johnson') # True
print('Joe J' in 'Joe Johnson') # True
print(5 in range(5)) # False
print(5 in range(6)) # True
print(5 not in range(5, 10)) # False
print(0 in range(10, 0, -1)) # False
print(4 in {6, 5, 4, 3, 2, 1}) # True
print({1, 2, 3} in {1, 2, 3}) # False: There is no set on the left in the set on the right because it is holding integers...not sets. If there was, then there would be a nested set.
print({3, 2} in {1, frozenset({2, 3})}) # True

# Question 12:
# Write some code that determines and prints whether the number 3 appears inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1) # True
print(3 in numbers2) # False
print(3 in numbers3) # False
print(3 in numbers4) # False
print(3 in numbers5) # True: considered equal when using value of quality, depsite being different data types

# You should print True or False depending on each result.

# Question 13:
# Without running the following code, determine what each print statement should print.

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats) # True
print('Butter' in cats) # False
print('Butter' in cats[3]) # True
print('cheddar' in cats) # False

# Question 14:
# Assume you have the following sequences:

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

# Write some code that combines the sequences into a list of tuples. Each tuple should contain one member of each sequence. Print the final result so you can see all the values, which should look like this:

[('a', 'Alpha', None, 10),
 ('b', 'Bravo', True, 20),
 ('c', 'Charlie', False, 30)]

zipped_iterables = zip(my_str, my_list, my_tuple, my_range)
print(list(zipped_iterables))

# Question 15:
# Without running the following code, what values will be printed by line 10?

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys() # Returns a dictionary view object
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# dict_keys(['Cat','Bird','Snake'])

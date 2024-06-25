# Multiply:
# Examine the function invocation below. Write the function multiply, such that it accepts two arguments and returns the product of its arguments. 
# You may assume that the function arguments will always be numbers.

# def multiply(num1,num2):
#     return (num1 * num2)

# print(multiply(12, 4))    # 48

# Print Quote
# Write a function that prints Bruce Eckel's quote 'Python is executable pseudocode.'. 
# What is the return value of the function?

# def bruce_eckel_quote():
#     print('Python is executable pseudocode.')

# bruce_eckel_quote()

# Return value of the function is None since there is no return statement

# Cite the Author
# Let's generalize the function from the previous exercise. 
# Implement a function named cite that takes two string arguments: the author of the quote and what they said. 
# It then prints the quote, as shown below.

# def cite(author,quote):
#     print(f'{author} said: "{quote}"')

# cite('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."

# Squared Number
# Write a function that accepts a single argument, a number, 
# and returns the result of multiplying its argument by an exponent of 2 
# (also known as squaring the number or raising the number to the power of 2).

# def squared_number(number):
#     return number**2
# print(squared_number(3))  # 9

# Display Division
# Without running the following code, determine what it will print:

# def multiples_of_three():
#     divisor = 1

#     for dividend in range(3, 31, 3):
#         print(f'{dividend} / {divisor} = 3')
#         divisor += 1

# multiples_of_three

#Error...function is not being invocated correctly.

#Three-way Comparison
# Write a function that compares the length of two strings. 
# It should return -1 if the first string is shorter, 1 if the second string 
# is shorter, and 0 if they're of equal length. For example:

# compare_by_length('patience', 'perseverance') # -1
# compare_by_length('strength', 'dignity')      #  1
# compare_by_length('humor', 'grace')           #  0

# def compare_by_length(str1,str2):
#     if len(str1) < len(str2):
#         return -1
#     elif len(str2) < len(str1):
#         return 1
#     else:
#         return 0
    
# print(compare_by_length('patience', 'perseverance'))
# print(compare_by_length('strength', 'dignity'))
# print(compare_by_length('humor', 'grace'))

# Transformation
# Use Python's string methods on the string 
# 'Captain Ruby' to create a string with the value 'Captain Python'.

# str1 = 'Captain Ruby'
# print(str1.replace('Ruby','Python'))

# Internationalization 1
# Use Python's control structures to create a function that 
# takes an ISO 639-1 language code and returns a greeting in that language. 
# You can take the examples below or add whatever languages you like.

# def greet(language_code):
#     match language_code:
#         case 'en':
#             return 'Hi!'
#         case 'fr':
#             return 'Salut!'
#         case 'pt':
#             return 'Ola!'
#         case 'de':
#             return 'Hallo!'
#         case 'sv':
#             return 'Hej!'
#         case 'af':
#             return 'Haai!'

# Locale Part 1
# Write a function that extracts the language code from a locale. 
# A locale is a combination of a language code, a region, and usually 
# also a character set, e.g en_US.UTF-8.

# def extract_language(locale):
#     return locale.split('_')[0]

# print(extract_language('en_US.UTF-8'))      # en
# print(extract_language('en_GB.UTF-8'))      # en
# print(extract_language('ko_KR.UTF-16'))     # ko


# print(greet('en'))         # Hi!
# print(greet('fr'))         # Salut!
# print(greet('pt'))         # Olá!
# print(greet('de'))         # Hallo!
# print(greet('sv'))         # Hej!
# print(greet('af'))         # Haai!

# Locale Part 2
# Similar to the previous exercise, 
# write a function that extracts the region code from a locale. For example:

# def extract_region(region):
#     return region.split('.')[0].split('_')[1]
# print(extract_region('en_US.UTF-8'))    # US
# print(extract_region('en_GB.UTF-8'))    # GB
# print(extract_region('ko_KR.UTF-16'))   # KR


def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case 'en','US':
            return 'Hey!'
        case 'en', 'GB':
            return 'Hello!'
        case 'en', 'AU':
            return 'Howdy!'
        case _:
            return greet(language)

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!


# Distinguish greetings for English speaking countries like the US, UK, Canada, 
# or Australia in your implementation, and feel free to fall back on the language-specific 
# greetings in all other cases, for example:

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!

# When implementing local_greet, make sure you re-use your extract_language, extract_region, and 
# greet functions from the previous exercises.


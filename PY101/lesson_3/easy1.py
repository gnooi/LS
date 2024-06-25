# Question 1:
# Will the code raise an error?

# numbers = [1, 2, 3]
# numbers[6] = 5

# Yes, the code will raise an IndexError, 
# as index 6 is out of bounds of the indices in 
# the numbers list. 

# <===============>

# Question 2:
# How can you determine whether a given string ends with
# an exclamation mark (!)? Write some code that prints 
# True or False depending on whether the string ends with 
# an exclamation mark.

# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False

# str1.endswith('!')
# str2.endswith('!')

# <=================>

# Question 3:
# Starting with the string:
# famous_words = "seven years ago..."

# Show two different ways to create a new string with 
# "Four score and " prepended to the front of the string.

# new_famous_words = "Four score and " + famous_words
# new_famous_words2 = f'Four score and  + {famous_words}'

# <=================>

# Question 4:
# Using the following string, print a string that contains the 
# same value, but using all lowercase letters except for the 
# first character, which should be capitalized.

# munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

# new_description = munsters_description.capitalize()

# <=================>

# Question 5:
# Starting with the string:

# munsters_description = "The Munsters are creepy and spooky."
# print the string with the case of all letters swapped:


# "tHE mUNSTERS ARE CREEPY AND SPOOKY."
# That is, lowercase letters are converted to uppercase, 
# and uppercase letters are converted to lowercase"

# print(munsters_description.swapcase())

# <=================>

# Question 6:
# Determine whether the name Dino appears in the strings below 
# -- check each string separately:


# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."

# 'Dino' in str1
# 'Dino' in str2

# <=================>

# Question 7:
# How can we add the family pet, "Dino", to the following list?

# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

# flintstones.append('Dino')

# <=================>

# Question 8:
# In the previous problem, our first answer added 'Dino' 
# to the list like this:

# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.extend(["Dino", "Hoppy"])

# How can we add multiple items to our 
# list (e.g., 'Dino' and 'Hoppy')? Replace the call to 
# append with another method invocation.


# <=================>

# Question 9:

# Print a new version of the sentence given by advice that 
# ends just before the word house. Don't worry about spaces or
# punctuation: remove everything starting from the beginning of
# house to the end of the sentence.

# advice = "Few things in life are as important as house training your pet dinosaur."

# Expected output:
# Few things in life are as important as

# print(advice.split('house')[0]) # Splits sentence at house, then prints first part of sentence.

# <=================>

# Question 10:
# Print the following string with the word 
# important replaced by urgent:

# advice = "Few things in life are as important as house training your pet dinosaur."

# advice = advice.replace('important', 'replace')

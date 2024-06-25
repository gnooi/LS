# String Formatting:

# name = "Victor"
# profession = "programmer"

# message = 'Hello, {}. You are a {}.'
# print(message.format(name,profession))

# print(f'Hello, {name}. You are a {profession}.')
# How can you print the string Hello, Victor. You are a programmer. using the str.format method? You should fill in the name and profession in a string literal that contains the rest of the text.
# How can you achieve the same result using an f-string?

# Style Guide:

# iceCreamDensity = 10

# while iceCreamDensity > 0:
#     print('Drip...')
#     iceCreamDensity -= 1

# print('The ice cream melted.')

# Date: 
# from datetime (module) import datetime (class), date, time, timezone
# print(datetime.now())

# Which Year is This?
# isocalendar(): returns a named tuple with three components: year, week and weekday. 
# year: returns a value between MINYEAR and MAXYEAR inclusive.

# Argument Signatures:
# It expects one argument, which would be an iterable such as a list. An error will show if fewer/more arguments are called.

# Find Substring:
# Use "ashjgnbg" in "ggjnfdgjd", by using the IN keyword.

# SyntaxError:

# The following code raises a SyntaxError: SyntaxError indicates a missing token before the indicated token. 
# In this example, the if statement was missing a colon. 

# speed_limit = 60
# current_speed = 80

# if current_speed > speed_limit:
#     print('"People are so bad at driving cars that '
#           "computers don\'t have to be that good to be "
#           'much better." -- Marc Andreessen')
    
# TypeError:

# The following code raises a TypeError:

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

# TypeError indicates when an operation or function is applied to an object of an inappropriate type. 
# In this case, len(tweet + 5) will raise an error because a string and a int cannot be added.

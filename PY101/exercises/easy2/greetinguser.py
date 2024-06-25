# Write a program that asks for user's name, then greets the user. 
# If the user appends a ! to their name, the computer will yell 
# the greeting (print it using all uppercase).

# <=== LS ANSWER ===>:

name = input("What is your name? ")

if name.endswith("!"):
    print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
else:
    print(f"Hello {name}.")


# <=== MY ANSWER ===>

def prompt_name():
    name = input('What is your name? ')
    return name

def validate_name():
    name = prompt_name()
    if '!' in name:
        name = name.upper()
    return name

def greet_user():
    validated_name = validate_name()
    if validated_name.isupper():
        return f'HELLO {validated_name} WHY ARE WE YELLING?'
    else:
        return f'Hello {validated_name}.'
    

print(greet_user())

# Example 1:
# What is your name? Sue
# Hello Sue.

# Example 2:
# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?
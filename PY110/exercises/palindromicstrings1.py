# Pseudocode:
# Define a function with 1 parameter
# Return an expression that evaluates whether or not 
# the reverse equals the current argument: argument == argument [::-1]

def is_palindrome(text):
    return text == text[::-1]

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)
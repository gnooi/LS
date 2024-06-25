# Pseudocode: 
# Define a function with 1 parameter
# Set a stripped_text variable to ''
# Iterate through argument
# If character isalnum(), concatenate character.casefold() to stripped_text
# Return stripped_text passed in is_palindrome function

def is_palindrome(text):
    return text == text[::-1]

def is_real_palindrome(text):
    stripped_text = ''

    for ch in text:
        if ch.isalnum():
            stripped_text += ch.casefold()
    
    return is_palindrome(stripped_text)


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True
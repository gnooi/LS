# Write a function that returns the next to last word in the string 
# argument.

# Words are any sequence of non-blank characters.

# You may assume that the input string will always contain at 
# least two words.

def penultimate(sentence):
    new_sentence = sentence.split()
    return new_sentence[-2]

# Examples
# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# Further Exploration:
# Our solution ignored two edge cases since we explicitly stated that
# you didn't have to handle them: strings that contain no words or 
# just one word.

# Suppose we need a function that retrieves the middle word of a 
# phrase/sentence. What edge cases need to be considered? How would 
# you handle those edge cases without ignoring them? Write a function 
# that returns the middle word of a phrase or sentence. It should 
# handle all of the edge cases you thought of.

def middle(sentence):
    sentence_lst = sentence.split()
    word_count = len(sentence_lst)
    while word_count > 1:
        if word_count % 2 != 0:
            return sentence_lst[int(word_count / 2)]
        else:
            return f"Uh-oh, '{sentence}' has no middle word."
    
    return f"The '{sentence}' needs to have more than 1 word."

    
print(middle("Launch School is so great!"))
print(middle('food'))
print(middle('last word'))
print(middle('cheesecake best cake'))
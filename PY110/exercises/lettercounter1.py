# All of these examples should print True

# Pseudocode:
# Define a function with 1 parameter
# Use split method on argument
# Set a counts variable to empty dictionary
# Iterate through words, length = len(word)
# If length is not in counts, append value = 0
# 


def word_sizes(text):
        words = text.split()
        counts = {}

        for word in words:
            length = len(word)
            if length not in counts:
                counts[length] = 0
            
            counts[length] += 1

        return counts

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
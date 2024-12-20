"""

- define a class Anagram:
    - define an init method that accepts a string
        - initialize self.word to string 

    - define an instance method match that accepts a list
        - initialize result to an empty list
        - initialize sorted_word to self.word sorted

        - iterate over list
            - if word is not equal to self.word
                - initialize sorted_value to word sorted
                - if sorted_word is equal to sorted_value
                    - append word to result list

        - return result list

"""
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        result = []

        for word in words:
            if word.lower() != self.word and self._is_anagram(self.word, word.lower()):
                    result.append(word)
        return result 
    
    def _is_anagram(self, word1, word2):
        return sorted(word1) == sorted(word2)
    
# class Anagram:
#     def __init__(self, word):
#         self.word = word.lower()

#     def match(self, words):
#         sorted_word = sorted(self.word)
#         result = []

#         for word in words:
#             if word.lower() != self.word:
#                 sorted_value = sorted(word.lower())
#                 if sorted_word == sorted_value:
#                     result.append(word)

#         return result 
    
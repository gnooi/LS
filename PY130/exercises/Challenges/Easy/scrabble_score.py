"""
- define a class Scrabble
    - define a class constant dictionary 
        - initialize letters as a string and value as a key

    - define an init method to accept 1 string
        - initialize self.word to string uppercase
  

    - define an instance method score
        - initialize result to 0
        - if self.word is truthy
            - iterate over word
                - iterate over dictionary 
                    - if letter in list value
                        - increment result by key 

        - return result
        
    - define a class method calculate_score that accepts a word
        - create an instance of the class with word passed in 
        - return the score method on the instance
"""

class Scrabble:
    SCORE = {
            1: 'AEIOULNRST', 
            2: 'DG',
            3: 'BCMP',
            4: 'FHVWY', 
            5: 'K', 
            8: 'JX',
            10: 'QZ'
    }

    def __init__(self, word):
        self.word = word

    def score(self):
        result = 0

        if self.word:
            for ch in self.word.upper():
                for score, letters in self.SCORE.items():
                    if ch in letters:
                        result += score

        return result 
    
    @classmethod
    def calculate_score(cls, word):
        scrabble = cls(word)
        return scrabble.score()


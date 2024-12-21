"""

- define a class Diamond
    
    - define a class method make_diamond to accept 1 letter
        - join top and bottom with new line

    - define a helper method to create the top half to accept 1 letter
        - find the index of the letter in string.ascii.uppercase
        - initialize external space to index
        - initialize internal space to 1 
        - initialize rows to list of string external space, letter, external space
        - decrement external space by 1

        - iterate over range of 2, index plus 1, accessing indexes
            - append and concatenate external space, letter, internal space, letter, external space

        - return rows
            

    - define a helper to create the bottom half
        - call on top half, reverse and slice at 1:
        - return rows


- first and last row is A
- 
"""
import string 

class Diamond:
    @classmethod
    def make_diamond(cls, letter):
        return '\n'.join(cls.top_half(letter) + cls.bottom_half(letter)) + '\n'
        
    @staticmethod
    def top_half(letter):
        letter_idx = string.ascii_uppercase.find(letter)
        external_space = letter_idx 
        internal_space = 1

        rows = [f'{' ' * external_space}{'A'}{' ' * external_space}']
        external_space -= 1
        
        for idx in range(1, letter_idx + 1):
            rows.append(f'{' ' * external_space}{string.ascii_uppercase[idx]}{' ' * internal_space}{string.ascii_uppercase[idx]}{' ' * external_space}')
            external_space -= 1
            internal_space += 2

        return rows

    @staticmethod
    def bottom_half(letter):
        rows = Diamond.top_half(letter)[::-1][1:]
        return rows

        
# print(Diamond.make_diamond('E'))

"""
- define a class RomanNumeral
    - define a class constant dictionary
        - 1000, 500, 100, 50, 10, 5, 1

    - define an init method to accept a number
        - initialize self.number to number

    - define an instance method to_roman
        - initialize roman_numeral to empty list
        - iterate over dictionary
            - determine how many times number can be divided by current roman numeral
            - append value of key * quotient to roman_numeral list
            - reassign remainder to number 
            
        - return roman_numeral joined as a string
"""

class RomanNumeral:
    ROMAN_NUMERALS = {
                1000: 'M',
                900: 'CM',
                500: 'D',
                400: 'CD', 
                100: 'C',
                90: 'XC',
                50: 'L',
                40: 'XL',
                10: 'X',
                9: 'IX',
                5: 'V', 
                4: 'IV',
                1: 'I'
    }

    def __init__(self, number):
        self.number = number

    def to_roman(self):
        result = []

        for value, symbol in self.ROMAN_NUMERALS.items():
            if self.number >= value:
                quotient, remainder = divmod(self.number, value)
                result.append(quotient * symbol)
                self.number = remainder 

        return ''.join(result)

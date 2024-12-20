"""
- define a class Octal
    - define an init method to accept 1 string
        - initialize self.number to string 

    - define an instance method to_decimal
        - initialize a result to 0
        - if all digits are digits and between 0 and 7

        - initialize octal to 0
        - iterate over number reversed
            - add number * 8 to octal power
            - increment octal 

        - return result 

"""

class Octal:
    def __init__(self, number):
        self.number = number

    def to_decimal(self):
        result = 0
        if all(ch.isdigit() and 0 <= int(ch) <= 7 for ch in self.number):
            octal = 0

            for ch in self.number[::-1]:
                result += int(ch) * (8 ** octal)
                octal += 1

        return result 
    
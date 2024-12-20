"""
- define a class Series:
    - define an init method that accepts 1 string
        - initialize self.digits to string
    - define a slices instance method that accepts 1 number
        - if number is greater than length of self.digits
            - raise ValueError

        - initialize result to empty list
        - iterate over self.digits, accessing indexes
            - initialize current slice to idx: idx + number
            - convert each digit to an integer in slice and convert to list
            - append digits

        - return result 


"""

class Series:
    def __init__(self, digits):
        self.digits = digits

    def slices(self, number):
        if number > len(self.digits):
            raise ValueError("Not enough digits for slice.")
        
        result = []

        for idx in range(len(self.digits) - number + 1):
            current_slice = self.digits[idx: idx + number]
            digits = list(int(digit) for digit in current_slice)
            result.append(digits)

        return result
    

# print(Series("98273463").slices(2))

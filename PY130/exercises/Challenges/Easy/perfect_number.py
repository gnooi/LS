"""

- define a class PerfectNumber
    - define a class method classify that accepts a number
        - if number is prime
            - return deficient 

        - if aliquot sum of number is greater 
            - return abundant
        - if aliquot sum of number is equal
            - return perfect
        - if aliquot sum of number is less than
            - return deficient 

    - define a helper method aliquot that accepts a number
        - initialize a set 
        - iterate over range of 1, number
            - if number is divisible by current value
                - add to the set

        - return sum of the set

    - define a helper method is_prime
        - iterate over range of 3, square root of number + 1, increment by 2
            - if number is divisible by current value
                - return False

        - return True
"""
import math

class PerfectNumber:
    @classmethod
    def classify(cls, number):
        if number < 1:
            raise ValueError("Input must be a positive integer")
        
        if cls.is_prime(number):
            return "deficient"

        if cls.aliquot(number) == number:
            return "perfect"
        elif cls.aliquot(number) > number:
            return "abundant"
        elif cls.aliquot(number) < number:
            return "deficient"

    @staticmethod
    def aliquot(number):
        divisors = set()
        for num in range(1, number):
            if number % num == 0:
                divisors.add(num)

        return sum(divisors)

    @staticmethod
    def is_prime(number):
        if number == 2:
            return True 

        for num in range(3, int(math.sqrt(number) + 1), 2):
            if number % num == 0:
                return False

# import math 

# class PerfectNumber:
#     @classmethod
#     def classify(cls, number):
#         if number > 0:
#             if cls.is_prime(number):
#                 return "deficient"
            
#             if cls.aliquot(number) == number:
#                 return "perfect"
#             elif cls.aliquot(number) > number:
#                 return "abundant"
#             elif cls.aliquot(number) < number:
#                 return "deficient"
#         else:
#             raise ValueError("Input must be a positive integer")
        
#     @staticmethod
#     def aliquot(number):
#         divisors = set()
#         for num in range(1, number):
#             if number % num == 0:
#                 divisors.add(num)

#         return sum(divisors)
    
#     @staticmethod
#     def is_prime(number):
#         if number == 2:
#             return True 
        
#         for num in range(3, int(math.sqrt(number) + 1), 2):
#             if number % num == 0:
#                 return False
            
    

"""
- define a class SumOfMultiples
    - define an init method to accept any number of positional arguments
        if args is truthy
            - initialize self.numbers to args(tuple)

        - initialize self.numbers to set of 3, 5

    - define a class method sum_up_to to accept 1 number
        - reutrn instance method 

    - define an instance method to to accept 1 number
        - initialize multiples to empty list
        - iterate over numbers
            - extend a list where we collect the multiples for each number

        - filter the multiples to be less than the limit
        - return sum of the filtered_multiples 


"""
class SumOfMultiples:
    def __init__(self, *args):
        self.numbers = args if args else (3, 5)

    @classmethod
    def sum_up_to(cls, limit):
        return cls().to(limit)

    def to(self, limit):
        multiples  = set()
        
        for number in self.numbers:
            multiples.update(range(number, limit, number))

        return sum(multiples)
    
# class SumOfMultiples:
#     def __init__(self, *args):
#         if args:
#             self.numbers = args
#         else:
#             self.numbers = (3, 5)

#     @classmethod
#     def sum_up_to(cls, limit):
#         return cls().to(limit)

#     def to(self, limit):
#         multiples = []
#         for number in self.numbers:
#             multiples.extend([number * num for num in range(1, limit)])

#         filtered_multiples = set(filter(lambda num: num < limit, multiples))
#         return sum(filtered_multiples)
    
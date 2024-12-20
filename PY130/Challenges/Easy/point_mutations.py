"""
- define a DNA class
    - define an init method that accepts 1 string
        - initialize self.dna to string
    - define an instance method hamming_distance that accepts 1 string
        - initialize count to 0
        - iterate over self.dna and argument
            - if one is not equal to another
                - increment count 

        - return count 

"""

class DNA:
    def __init__(self, dna):
        self.dna = dna

    def hamming_distance(self, other_strand):
        count = sum(1 for strand1, strand2 in zip(self.dna, other_strand) if strand1 != strand2)
        return count

# class DNA:
#     def __init__(self, dna):
#         self.dna = dna

#     def hamming_distance(self, other_strand):
#         count = 0
#         for strand1, strand2 in zip(self.dna, other_strand):
#             if strand1 != strand2:
#                 count += 1

#         return count
    

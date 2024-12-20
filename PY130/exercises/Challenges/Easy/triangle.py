"""
- all sides greater than 0
- sum of any 2 sides greater than the length of the 3rd side

- define a class
    - define an init method that takes 3 sides
        - if all sides are valid and make up a triangle
            - initialize self.sides to a list of 3 sides 
    - define a property kind 
        - if length of set of sides is 1
            - return equilateral
        - if length of set of sides is 2
            - return isosceles
        - if length of set of sides is 3
            - return scalene
        - return triangle kind as corresponding string

    - define is_positive helper method
        - return if all sides are positive

    - define is_valid helper method
        - return if any 2 sides are greater than the 3rd
    -

"""

class Triangle:
    def __init__(self, side1, side2, side3):
        if self.is_positive(side1, side2, side3) and self.is_valid(side1, side2, side3):
            self.sides = [side1, side2, side3]
        else:
            raise ValueError("Not a valid triangle")

    @property
    def kind(self):
        triangle_type = {
            1: "equilateral",
            2: "isosceles",
            3: "scalene"
        }

        return triangle_type.get(len(set(self.sides)), len(set(self.sides)))

    def is_positive(self, a, b, c):
        return all(side > 0 for side in [a, b, c])

    def is_valid(self, a, b, c):
        return (a + b > c) and (a + c > b) and (b + c > a)

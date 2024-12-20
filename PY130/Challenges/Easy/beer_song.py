"""
- define a BeerSong class
    - define a class method verse to accept 1 number
        - if number is 1 
            - assign bottles to "bottle"
        
        - return f-string with new line character
    - define a class method verses to accept 2 numbers
        - initialize result to empty list
        - iterate over range os start, end, decrement
            - append call on class method with number passed in 

        - return result joined as string 

    - define a class method lyrics
        - call on class method verses with 99 and 0 as arguments

- 1 bottle
- 0 bottles

"""

class BeerSong:

    @classmethod
    def verse(cls, number):
        if number > 1:
            return (f"{number} bottles of beer on the wall, {number} bottles of beer.\n"
                    f"Take one down and pass it around, {number - 1} bottle{'s' if number != 2 else ''} of beer on the wall.\n")
        elif number == 1:
            return (f"{number} bottle of beer on the wall, {number} bottle of beer.\n"
                    f"Take it down and pass it around, no more bottles of beer on the wall.\n")
        else:
            return ("No more bottles of beer on the wall, no more bottles of beer.\n"
                    f"Go to the store and buy some more, 99 bottles of beer on the wall.\n")

    @classmethod
    def verses(cls, end, start):
        result = []

        for num in range(end, start - 1, -1):
            result.append(cls.verse(num))

        return '\n'.join(result)

    @classmethod
    def lyrics(cls):
        return cls.verses(99, 0) 
    
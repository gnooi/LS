"""
- define a class Clock
    - define an init method
        - initialize self.minutes to # of minutes in a day: 1440

    - define a class method at to accept 2 numbers, hours, minutes
        - default vaue for minutes
        - convert the hours to minutes by multiplying 60
        - add to minutes
        - assign self.minutes to total minutes

    - define an add method to add minutes
        - add minutes to self.minutes
        - return new clock object
    - define a subtract method to subtract minutes 
        - subtract minutes from self.minutes
        - return new clock object

    - define a str method to print the time in hours and minutes
        - if absolute value of self.minutes is greater than 1440
            - divide self.minutes by 1440
            - assign self.minutes to remainder
        - otherwise   
            - divide self.minutes by 60
            - assign quotient to hours
            - assign remainder to self.minutes

        - return a new clock object

    - define a eq method to compare two string values of clocks

"""
class Clock:
    def __init__(self, hours, minutes):
        self.minutes = (hours * 60 + minutes) % 1440

    @classmethod
    def at(cls, hours=0, minutes=0):
        return cls(hours, minutes)   

    def __add__(self, minutes):
        return Clock.at(0, self.minutes + minutes)
    
    def __sub__(self, minutes):
        return Clock.at(0, self.minutes - minutes)
    
    def __str__(self):
        hours, minutes = divmod(self.minutes, 60)
        return f"{self.pad_zeroes(hours)}:{self.pad_zeroes(minutes)}"
    
    def __eq__(self, clock):
        if not isinstance(clock, Clock):
            return NotImplemented
        
        return self.minutes == clock.minutes
    
    def pad_zeroes(self, number):
        return f"{number:02}"
        

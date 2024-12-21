"""
- import random 
- import string

- define class Robot
    - define a class variable set to keep track of all names

    - define an init method
        - initialize self._name to None

    - define a property name
        - if self._name is truthy 
            - while True
                - generate new name
                - if new name is not in class set
                    - break 

                - add new name to set
                - set self._name to new name

        - return self._name

    - define a reset instance method 
        - discard name in set
        - initialize self._name to None

    - define a generator isntance method 
        - generate the letters and digits
        - return combination

"""
import random
import string 

class Robot:
    previous_names = set()

    def __init__(self):
        self._name = None

    @property
    def name(self):
        if not self._name:
            while True:
                new_name = self.generate_name()
                if new_name not in Robot.previous_names:
                    break
            self._name = new_name
            Robot.previous_names.add(new_name)
        return self._name

    def reset(self):
        Robot.previous_names.discard(self._name)
        self._name = None

    def generate_name(self):
        digits = ''
        letters = ''
        
        for _ in range(2):
            letters += random.choice(string.ascii_uppercase)

        for _ in range(3):
            digits += random.choice(string.digits)

        new_name = letters + digits
        return new_name

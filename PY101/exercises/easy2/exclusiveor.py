# The or operator returns a truthy value if either or both of its 
# operands are truthy, a falsy value if both operands are falsy. 
# The and operator returns a truthy value if both of its operands 
# are truthy, and a falsy value if either operand is falsy. This 
# works great until you need only one of two conditions to be truthy, 
# the so-called exclusive or, also known as xor (pronounced "ECKS-or").

# In this exercise, you will write an xor function that takes two 
# arguments, and returns True if exactly one of its arguments is 
# truthy, False otherwise.

def xor(value1, value2):
    if (bool(value1) == True) and (bool(value2) == False):
        return True
    elif (bool(value1) == False) and (bool(value2) == True):
        return True
    elif (bool(value1) == True) and (bool(value2) == True):
        return False
    elif (bool(value1) == False) and (bool(value2) == False):
        return False

# Further Exploration
# Can you think of a situation in which a boolean xor function would 
# be useful? Suppose you were modeling a light at the top of a flight 
# of stairs wired in such a way that the light can be turned on or off 
# using either the switch at the bottom of the stairs or the switch at 
# the top of the stairs. Think of some additional examples.

# or and and are so-called short circuit operators in that the second 
# operand is not evaluated if its value is not needed. Does the xor 
# function perform short-circuit evaluation of its operands? Why or 
# why not? Does short-circuit evaluation in xor operations even make 
# sense?   

# Examples
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
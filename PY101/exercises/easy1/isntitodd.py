
def odd_function(integer1): # DEFINE function with 1 parameter
    if abs(int(integer1)) % 2 != 0: # IF the absolute value of the int argument is odd
        return True # RETURN true
    else: # Otherwise
        return False # RETURN false
    

x = odd_function(4) # Intialize x to call on odd_function with argument 
print(x) # Call print function on variable x

# Solution provided:
def is_odd(number): # Define function with 1 parameter
    return abs(number) % 2 == 1 # Return absolute value of argument modulo 2 equals 1
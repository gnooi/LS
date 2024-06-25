# A double number is an even-length number whose left-side digits 
# are exactly the same as its right-side digits. For example, 44, 
# 3333, 103103, and 7676 are all double numbers, whereas 444, 334433, 
# and 107 are not.

# Write a function that returns the number provided as an argument 
# multiplied by two, unless the argument is a double number. If 
# the argument is a double number, return the double number as-is.

# <=== LS ANSWER ===>

def is_double_number(number):
    string_number = str(number)
    center = len(string_number) // 2
    left_number = string_number[:center]
    right_number = string_number[center:]

    return left_number == right_number

def twice(number):
    if is_double_number(number):
        return number
    else:
        return number * 2



# <=== MY ANSWER ===>

def twice(number):
    
    number = str(number)

    if len(number) % 2 == 0:
        half_num = len(number) // 2
        left_side = number[:half_num]
        right_side = number[half_num:]

        if left_side == right_side:
            return int(number)

    return int(number) * 2


# Examples
print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True

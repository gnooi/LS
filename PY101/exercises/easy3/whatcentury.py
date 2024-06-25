# Write a function that takes a year as input and returns the century. 
# The return value should be a string that begins with the century 
# number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for 
# that number.

# New centuries begin in years that end with 01. So, the years 
# 1901 - 2000 comprise the 20th century.


# def get_century(year):
#     if year % 100 == 0:
#         century = year // 100
#     else:
#         century = (year // 100) + 1
#     return century

# def get_suffix(century):
#     if 10 <= century % 100 <= 20:
#         return "th"
#     last_digit = century % 10
#     if last_digit == 1:
#         return "st"
#     elif last_digit == 2:
#         return "nd"
#     elif last_digit == 3:
#         return "rd"
#     else:
#         return "th"

# def century(year):
#     century_number = get_century(year)
#     suffix = get_suffix(century_number)
#     return f'{century_number}{suffix}'


# print(century(2000) == "20th")          # True
# print(century(2001) == "21st")          # True
# print(century(1965) == "20th")          # True
# print(century(256) == "3rd")            # True
# print(century(5) == "1st")              # True
# print(century(10103) == "102nd")        # True
# print(century(1052) == "11th")          # True
# print(century(1127) == "12th")          # True
# print(century(11201) == "113th")        # True

# Example usage
# print(century(1905))  # Output: '20th'
# print(century(2000))  # Output: '20th'
# print(century(2001))  # Output: '21st'
# print(century(2100))  # Output: '21st'
# print(century(1700))  # Output: '17th'
# print(century(1121))  # Output: '12th'


# Pseudocode:
# Define 2 functions 
# get_century function (1 parameter):
# Century = 100 years
# If year % 100 == 0
# Set variable century = year // 100
# Else:
# Set variable century = year // 100 + 1
# Return century

# match_suffix function(1 parameter):
# Set variable length to length of century
# If length is less than 2: set a variable last_two to century[-1], match the ones cases 
# Else: set a variable last_two to century [-2], match the tens cases
# last_two = str(century)[-2:]
# match last_two:
# case 1:
# case 2
# case 3:
# case 4| 5| 6| 7| 8| 9| 10 | 11 | 12 | 13:
# return f'{century}{th}

def get_century(year):
    if year % 100 == 0:
        century = year // 100
    else:
        century = (year // 100) + 1
    
    return century

def century(year):
    century = (get_century(year))

    last_two = century % 100
    last_digit = century

    match last_two:
        case '1':
            return (f'{century}st')
        case '02':
            return (f'{century}nd')
        case '3':
            return (f'{century}rd')
        case '21':
            return (f'{century}st')
        case '22':
            return (f'{century}nd')
        case '23':
            return (f'{century}rd')
        case '4'| '5'| '6'| '7'| '8'| '9'| '10'| '11' | '12' | '13' | '20':
            return (f'{century}th')


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
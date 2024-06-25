# Searching 101
# Write a program that solicits six (6) numbers from the user and 
# prints a message that describes whether the sixth number appears 
# among the first five.

# Pseudocode:
# For loops 6 times, taking the input of a number, and returns a list
# If statement to check if the last element is in the list, print message

#<==== PROGRAM =====>

def get_first_number():
    first_number = input('Enter the 1st number: ')
    return first_number

def get_second_number():
    second_number = input('Enter the 2nd number: ')
    return second_number

def get_third_number():
    third_number = input('Enter the 3rd number: ')
    return third_number

def get_fourth_number():
    fourth_number = input('Enter the 4th number: ')
    return fourth_number

def get_fifth_number():
    fifth_number = input('Enter the 5th number: ')
    return fifth_number

def get_sixth_number():
    sixth_number = input('Enter the 6th number: ')
    return sixth_number

def main_program():
    first_number = get_first_number()
    second_number = get_second_number()
    third_number = get_third_number()
    fourth_number = get_fourth_number()
    fifth_number = get_fifth_number()
    sixth_number = get_sixth_number()

    num_lst = [first_number, second_number, third_number, fourth_number, fifth_number]

    if sixth_number in num_lst:
        print(f'{sixth_number} is in {num_lst}.')
    else:
        print(f"{sixth_number} isn't in {num_lst}")

main_program()

# <===== SKELETON =======>

# num_lst = []

# first_number = input('Enter the 1st number: ')
# second_number = input('Enter the 2nd number: ')
# third_number = input('Enter the 3rd number: ')
# fourth_number = input('Enter the 4th number: ')
# fifth_number = input('Enter the 5th number: ')
# sixth_number = input('Enter the 6th number: ')

# num_lst.append(first_number)
# num_lst.append(second_number)
# num_lst.append(third_number)
# num_lst.append(fourth_number)
# num_lst.append(fifth_number)

# if sixth_number in num_lst:
#     print(f'{sixth_number} is in {first_number},{second_number},{third_number},{fourth_number},{fifth_number}.')
# else:
#     print(f"{sixth_number} isn't in {first_number},{second_number},{third_number},{fourth_number},{fifth_number}.")

# Example 1
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17

# 17 is in 25,15,20,17,23.

# Example 2
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 18

# 18 isn't in 25,15,20,17,23.
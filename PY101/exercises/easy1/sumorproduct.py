# Sum or Product of Consecutive Integers
# Write a program that asks the user to enter an integer
# greater than 0, then asks whether the user wants to determine 
# the sum or the product of all numbers between 1 and the entered 
# integer, inclusive.

# Suppose the input was a list of space separated integers instead 
# of just a single integer? How would your compute_sum and 
# compute_product functions change?

def prompt_integers_list():
        integers_list = list(map(str, 
                        input('Please enter multiple integers greater '
                              'than 0 separated by a space: ').split()))
        return integers_list

# def get_integers_list():
#     while True:
#         validated_integers_list = []
#         integers_list = prompt_integers_list()
#         for element in integers_list:
#             if element.isnumeric():
#                 int_element = int(element)
#                 validated_integers_list.append(int_element)
#             else:
#                 integers_list.remove(element)
#         return validated_integers_list
        # print('Please try again.')

def prompt_operation():
    operation = input("Enter 's' to compute the sum, or 'p' to" 
                      " compute the product. ").strip()
    return operation

def get_operation():
    while True:
        operation = prompt_operation()
        if operation == 's' or operation == 'p':
            return operation
        print('Please try again.')
        
def compute_sum(integer_list):
    sum = 0
    for number in integer_list:
        sum += number
    return sum

def compute_product(integer_list):
    product = 1
    for number in integer_list:
        product *= number
    return product

def display_sum(integer_list, sum):
    print(f'The sum of the integers between 1 and {integer_list}' 
              f' is {sum}.')
    
def display_product(integer_list, product):
    print(f'The product of the integers between 1 and {integer_list}' 
              f' is {product}.')

while True:

    integers_list = prompt_integers_list()

    operation = get_operation()

    sum = compute_sum(integers_list)      

    product = compute_product(integers_list)

    if operation == 's':
        display_sum(integers_list, sum)

    elif operation == 'p':
        display_product(integers_list, product)

    break

# <=== ORIGINAL PROBLEM ===>:

# def prompt_integer():
#     integer = input('Please enter an integer greater than 0: ').strip()
#     return integer

# def prompt_operation():
#     operation = input("Enter 's' to compute the sum, or 'p' to" 
#                       " compute the product. ").strip()
#     return operation

# def get_integer():
#     while True:
#         integer = prompt_integer()
#         if integer.isnumeric():
#             integer = int(integer)
#             return integer
#         print('Please try again.')

# def get_operation():
#     while True:
#         operation = prompt_operation()
#         if operation == 's' or operation == 'p':
#             return operation
#         print('Please try again.')
        
# def sum_operation(integer_input):
#     sum = 0
#     range_end = integer_input + 1
#     for number in range(1, range_end):
#         sum += number

#     return sum

# def product_operation(integer_input):
#     sum = 1
#     for number in range(1, integer_input + 1):
#         sum *= number
#     return sum

# def display_sum(integer_input, sum_input):
#     print(f'The sum of the integers between 1 and {integer_input}' 
#               f' is {sum_input}.')
    
# def display_product(integer_input, product_input):
#     print(f'The product of the integers between 1 and {integer_input}' 
#               f' is {product_input}.')

# while True:

#     integer = get_integer()

#     operation = get_operation()

#     sum = sum_operation(integer)      

#     product = product_operation(integer)

#     if operation == 's':
#         display_sum(integer, sum)

#     elif operation == 'p':
#         display_product(integer, product)

#     break
        

# Example 1:
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.


# Example 2:
# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.

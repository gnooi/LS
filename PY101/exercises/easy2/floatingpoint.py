# Write a program that prompts the user for two positive numbers 
# (floating-point), then prints the results of the following 
# operations on those two numbers: addition, subtraction, product, 
# quotient, floor quotient, remainder, and power. Do not worry about 
# validating the input.


# <=== LS ANSWER ===> 

first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))

def calculate(first, second, operator):
    match operator:
        case '+':
            return first + second
        case '-':
            return first - second
        case '*':
            return first * second
        case '/':
            return first / second
        case '//':
            return first // second
        case '**':
            return first ** second
        
operators = ['+', '-', '*', '/', '//', '%', '**']


for operator in operators:
    operation = f'{first_number} {operator} {second_number}' 
    result = calculate(first_number, second_number, operator)
    print(f'==> {operation} = {result}')

# <=== MY ANSWER ===>

first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))

# addition_operation = first_number + second_number
# subtraction_operation = first_number - second_number
# multiplication_operation = first_number * second_number
# division_operation = first_number / second_number
# int_division_operation = first_number // second_number
# modulus_operation = first_number % second_number
# power_operation = first_number ** second_number

# print(f'==> {first_number} + {second_number} = {addition_operation}')
# print(f'==> {first_number} - {second_number} = {subtraction_operation}')
# print(f'==> {first_number} * {second_number} = {multiplication_operation}')
# print(f'==> {first_number} / {second_number} = {division_operation}')
# print(f'==> {first_number} // {second_number} = {int_division_operation}')
# print(f'==> {first_number} % {second_number} = {modulus_operation}')
# print(f'==> {first_number} ** {second_number} = {power_operation}')


# Examples:
# ==> Enter the first number:
# 3.141529
# ==> Enter the second number:
# 2.718282
# ==> 3.141529 + 2.718282 = 5.859811
# ==> 3.141529 - 2.718282 = 0.42324699999999993
# ==> 3.141529 * 2.718282 = 8.539561733178
# ==> 3.141529 / 2.718282 = 1.1557038600115808
# ==> 3.141529 // 2.718282 = 1.0
# ==> 3.141529 % 2.718282 = 0.42324699999999993
# ==> 3.141529 ** 2.718282 = 22.45792517468373
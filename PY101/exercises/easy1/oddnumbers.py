# Odd Numbers
# Print all odd numbers from 1 to 99, inclusive, 
# with each number on a separate line.
# for number in range(1,100):
#     if number % 2 == 1:
#         print(number)

# Bonus Question: Can you solve the problem by iterating 
# over just the odd numbers?

# for number in range(1,100,2):
#     print(number)

# Further Exploration
# Consider adding a way for the user to specify the starting 
# and ending values of the odd numbers printed.

def odd_numbers(num1, num2):
    for number in range(int(num1), int(num2 + 1)):
        if number % 2 != 0:
            print(number)

(odd_numbers(5, 9))

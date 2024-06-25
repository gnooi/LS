# First Car
# Create a dictionary that contains the following data, and assign it to a variable named car.

# type	color	mileage
# sedan	blue	80000

# car = {'type' : 'sedan', 
#        'color' : 'blue', 
#        'mileage' : 80000}


# Adding the Year
# Add some code below the following code to define a 
# year key with a value of 2003. Don't update the dictionary 
# literal; instead, add some code after lines 1-5:


# car = {
#     'type':    'sedan',
#     'color':   'blue',
#     'mileage': 80_000,
# }

# car['year'] = 2003
# print(car)

# Broken Odometer
# Using the following code, delete the 'mileage' key and its 
# associated value from car.

# car = {
#     'type':    'sedan',
#     'color':   'blue',
#     'mileage': 80_000,
#     'year':    2003,
# }

# del car['mileage']
# print(car)

# What Color?
# Using the following code, select and print the value 'blue' 
# from the car object:


# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

# print(car['color'])

# What's My Length?
# Calculate and print the number of key/value pairs in the 
# following dictionary:

# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

# print(len(car))

# Checking Key Existence
# Check whether the keys 'name' and 'grade' exist in the 
# following dictionary:


# student = {
#     'id': 123,
#     'grade': 'B',
# }

# print('name' in student)
# print('grade' in student)

# Multiple Cars
# Create a nested dictionary that contains the following data.

# Car

# type	color	year
# sedan	blue	2003

# Truck

# type	color	year
# pickup	red	1998

# dict = {
#     'Car' : {
#         'type' : 'sedan',
#         'color' : 'blue',
#         'year' : '2003'},
#     'Truck' : {
#         'type' : 'pickup',
#         'color' : 'red',
#         'year' : '1998'}
#     }

# print(dict)

# Which Collection?
# Rewrite car as a nested list containing the same key/value pairs.

# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

# car = [
#     ['type','sedan'],
#     ['color', 'blue'],
#     ['year', '2003']

# ]
# print(car)

# Divided by Two
# Use a for loop to iterate over the numbers dictionary and 
# return a list containing each number divided by 2 as an integer. 
# If a number is odd, the result should be truncated to an integer. 
# Assign the returned list to a variable named half_numbers and 
# print its value using print.


# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    25,
# }
# half_numbers = []
# lst_values = numbers.values()
# for value in lst_values:
#     num = value // 2 
#     if value % 2 == 0:
#         half_numbers.append(num)
#     else:
#         half_numbers.append(num)
    
# print(half_numbers)

# half_numbers = []
# for value in numbers.values():
#     half_numbers.append(value // 2)

# print(half_numbers)


# Expected Output
# [50, 25, 12]

# Labeled Numbers
# Use a for loop to iterate over the numbers dictionary and 
# print each element's key/value pair.

# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    10,
# }


# for key,value in numbers.items():
#     print(f'A {key} number is {value}.')
    

# A high number is 100.
# A medium number is 50.
# A low number is 10.


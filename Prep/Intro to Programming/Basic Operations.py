# Concatenate two strings, one with your first name and one with your last, to create a new string with your full name as its value. 
# For example, if your name is John Doe, you should combine 'John' and 'Doe' to get 'John Doe'.
full_name = 'Lily' + ' Xiong'
print(full_name)

first_name = 'Lily'
last_name = 'Xiong'
print(f'{first_name} {last_name}')

# This question may be a little challenging if your math skills are rusty. Don't be afraid to take advantage of the hints. Try your best to solve the problem, but don't feel compelled to complete it if you become frustrated.

#Use the REPL and the arithmetic operators to extract the individual digits of 4936:

#One place is 6.
#Tens place is 3.
#Hundreds place is 9.
#Thousands place is 4.
#Each digit may require multiple Python statements.

number_value = 4936
one_place = number_value % 10 
number_value = number_value // 10
tens_place = number_value % 10
number_value = number_value // 10
hundreds_place = number_value % 10
number_value = number_value // 10
thousands_place = number_value % 10

print('One place is' + f' {one_place}')
print('Tens place is' + f' {tens_place}')
print('Hundreds place is' + f' {hundreds_place}')
print('Thousands place is' + f' {thousands_place}')

# What does the following code do and why?
# print('5' + '10')
# The following code produces the output 510 because two strings are being concatenated


# Refactor the code from the previous exercise to use coercion to print 15 instead.
print(int('5') + int('10'))

# Will an error occur if you try to access a list element with an index 
# greater than or equal to the list's length? For example:

foo = ['a', 'b', 'c']
print(foo[3])      # will this result in an error?

# Yes, this will result in an error since 
# indexing accounts for 1 less than the amount of elements in a list.

# To what value does the following expression evaluate?
# 'foo' == 'Foo'
# The following expression evaluates if string 'foo' is equal to string 'Foo'. 
# In this case, the evaluation is a boolean type, and is false due to case mismatch.

# What will the following code do? Why?
int('3.1415') # The following code will be an error
              # since the value within the parentheses 
              # is a string and not a valid integer.

# To what value does the following expression evaluate?
'12' < '9' # Two strings are compared, and in this case evaluates as True.
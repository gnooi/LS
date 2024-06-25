# Question 1:
# If you have a list named people, how can you determine the number of entries in that list?
# print(len(people)
# Use len(people) to determine the number of entries

# Question 2:
# Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')
my_list = list(stuff)
my_list[2] = 'goodbye'

print(my_list)

# Question 3:
# Identify at least 2 differences between lists and tuples. 
# Identify at least 2 ways that lists and tuples are similar.

# Lists are mutable, tuples are not mutable. Lists use [], tuples use ()
# Lists and tuples are both non-primitives. Lists and tuples are both sequences. 

# Question 4:
# Why can we treat strings as sequences?
# Strings are a form of sequence called a text sequence where you can access the individuals characters with indexing. 

# Question 5:
# How do the set types differ from the sequence types?
# Set types maintain an unordered collection of unique objects that cannot be indexed or have duplicate members. 
# Sequence types maintain an ordered collection that can be indexed and duplicate. 

# Question 6:
# Assuming you have the following assignment:

pi = 3.141592
# Write some code that converts the value of pi to a string and assigns it to a variable named str_pi.

str_pi = str(pi)
print(str_pi)

# Question 7:
# Without running the following code, identify the numbers that are included in each of the following ranges:

range(7) # [0, 1, 2, 3, 4, 5, 6]
range(1, 6) # [1, 2, 3, 4, 5]
range(3, 15, 4) # [3, 7, 11'
range(3, 8, -1) # empty range []
range(8, 3, -1) # [8, 7, 6, 5, 4]

# Question 8:
# How would you print all the numbers in the following range?

range(3, 17, 4)
a = range(3, 17, 4)
print(list(a))

# Question 9:
# my_list = [1, 2, 3, [4, 5, 6]]
# another_list = list(my_list)
# Given the above code, answer the following questions and explain your answers:

# Are the lists assigned to my_list and another_list equal? True, both lists with the same elements
# Are the lists assigned to my_list and another_list the same object? Two lists are not the same object, list() creates a new object
# Are the nested lists at index 3 of my_list and another_list equal? True, both lists are equal and have the same elements
# Are the nested lists at index 3 of my_list and another_list the same object? True, two nested lists are the same object, list() creates a shallow copy of the iterable passed as an argument. Shallow copies don't create new nested lists, only reference to the nested list gets copied. 

# Question 10:
# Bob expects the following code to print the names in alphabetical order. Without running the code, can you say whether it will? Explain your answer.

names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)

# The following code will not print the names in alphabetical order because it is a set, which is an unordered collection of unique objects. Thus, the order in which members are shown when printing or iterating is arbitrary. 

# Question 11:
# Consider the data in the following table:

# Name	    Country
# Alice	    USA
# Francois	Canada
# Inti	    Peru
# Monika	Germany
# Sanyu	    Uganda
# Yoshitaka	Japan
# You need to write some Python code to determine the country name associated with one of the listed names. Your code should include the data structure(s) you need and at least one test case to ensure the code works.

countries = {
    'Alice': 'USA',
    'Francois' : 'Canada', 
    'Inti' : 'Peru',
    'Monika' : 'Germany',
    'Sanyu' : 'Uganda',
    'Yoshitaka' : 'Japan'
}

print(countries['Monika'])
# Question 1:
# # Value Equality : my_object1 == my_object2 compares two objects to see whether they are equal. 
# They are considered equal when they have the same value or state. In the case of collections, two collections are equal when they have the same elements.
# # Object Equality : my_object1 is my_object2 checks two variables to see whether they reference the same object. 
# An object is the same as another object if both are stored at the same location in memory. In particular, that means we can say that my_object1 and my_object2 share the referenced object or that my_object1 and my_object2 are aliases for the same object.

# Question 2:
# Without running this code, what will it print? Why?

# set1 = {42, 'Monty Python', ('a', 'b', 'c')}
# set2 = set1
# set1.add(range(5, 10))
# print(set2)
# Don't worry about having an exact match for the output. The important part is to show something that accurately represents set2.

# set2 = {42, 'Monty Python', ('a', 'b', 'c'), range(5,10)}

# Question 3:
# Without running this code, what will it print? Why?

# dict1 = {
#     "Hitchhiker's Guide to the Galaxy": 42,
#     'Monty Python': 'The Life of Brian',
#     'Airplane!': "Don't call me Shirley!",
# }

# dict2 = dict(dict1)
# dict2['Monty Python'] = 'Holy Grail'
# print(dict1['Monty Python']) # 'The Life of Brian'

# Question 4:
# Without running this code, what will it print? Why?

# dict1 = {
#     'a': [1, 2, 3],
#     'b': (4, 5, 6),
# }

# dict2 = dict(dict1)
# dict1['a'][1] = 42
# print(dict2['a']) # [1,42,3]

# Question 5:
# Write some code to create a deep copy of the dict1 object and assign it to dict2. You should only modify the code where indicated.

# import copy

# dict1 = {
#     'a': [[7, 1], ['aa', 'aaa']],
#     'b': ([3, 2], ['bb', 'bbb']),
# }

# dict2 = copy.deepcopy(dict1)

# # All of these should print False
# print(dict1         is dict2)
# print(dict1['a']    is dict2['a'])
# print(dict1['a'][0] is dict2['a'][0])
# print(dict1['a'][1] is dict2['a'][1])
# print(dict1['b']    is dict2['b'])
# print(dict1['b'][0] is dict2['b'][0])
# print(dict1['b'][1] is dict2['b'][1])

# print(dict1['a'][0][0] is dict2['a'][0][0])
# print(dict1['a'][0][1] is dict2['a'][0][1])
# print(dict1['a'][1][0] is dict2['a'][1][0])
# print(dict1['a'][1][1] is dict2['a'][1][1])
# print(dict1['b'][0][0] is dict2['b'][0][0])
# print(dict1['b'][0][1] is dict2['b'][0][1])
# print(dict1['b'][1][0] is dict2['b'][1][0])
# print(dict1['b'][1][1] is dict2['b'][1][1])

# Question 6:
# The following program is nearly identical to that of the previous exercise. However, this time, it should create a shallow copy of dict1. Be careful: you're not allowed to use the copy module in this exercise.`

# In addition, before you run this code, can you predict the output values?

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1)

print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])
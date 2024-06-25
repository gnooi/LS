# What's my value? (Part 1)
# What will the following code do and why? Don't run it until you have tried to answer.
# 20
if True:
    my_value = 20

print(my_value)

# What's my value? (Part 2)
# What will the following code do and why? Don't run it until you have tried to answer.

# The code will raise an error because the x variable is intialized outside of the function scope. 
x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

# What's my value? (Part 3)
# What will the following code do and why? Don't run it until you have tried to answer.
# prints 1
def my_function():
    a = 1

    if True:
        print(a)

my_function()

# What's my value? (Part 4)
# What will the following code do and why? Don't run it until you have tried to answer.
# prints 1 because a is globally intialized but cannot be reassigned or make changes to it without getting an error. Right now, it's just being referenced. 
a = 1

def my_function():
    print(a)

my_function()


# What's my value? (Part 5)
# What will the following code do and why? Don't run it until you have tried to answer.

# Will give an error because a is not intialized within the function scope. 
a = 1

def my_function():
    print(a)
    a = 2

my_function()

# What's my value? (Part 6)
# What will the following code do and why? Don't run it until you have tried to answer.
# Will print 1 because the variable a intialized globally is referenced not the local variable a.
a = 1

def my_function():
    a = 2

my_function()
print(a)

# What's my value? (Part 7)
# What will the following code do and why? Don't run it until you have tried to answer.
# 2, a has been globally intialized within the function and changed to 2. 
a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# What's my value? (Part 8)
# What will the following code do and why? Don't run it until you have tried to answer.
# Will give an error because the variable greeting is not defined before the print function is invoked. 

print(greeting)

greeting = 'Hello world!'

# What's my value? (Part 9)
# What will the following code do and why? Don't run it until you have tried to answer.
# 7, integers are immutable and therefore cannot be changed, so a = 7 remains.  
a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# What's my value? (Part 10)
# What will the following code do and why? Don't run it until you have tried to answer.
# prints 10,2,3 because lists are mutable objects, can be modified in a function, affecting the original list in a global scope. 
b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)


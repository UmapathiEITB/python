# variables are containers for storing data values

#creating variables

x = 5
y = 'python'
print(x,y)
print(y)

# casting

# If we want to specify the data type to the variable, this can be done with casting

x = str(3)
y = int(3)
z = float(3)

# get the type --> type()

x = 5
y = 'john'
print(type(y))

# single or double quotes (string can be declared either by single or double)

x = 'string'
y = "string"

# case sensitive (variable names are case-sensitive Ex: a and A are different variables)

a = 'a'
A = 'a'

print(a,A)

#variable name rules

"""

A variable name must start with letter or underscore letter
A variable name cannot start start with a number
A variable name can contain only alphe-number and underscore letter
Variable names are case-sensitive
A variable name cannot be any of the python keywords 

"""

# multi words variable names

# Camel Case

myVariableName = 'test' #each word start with capital except first letter

# Pascal Case

MyVariableName = 'test' #each word start with letter

# Snake Case

my_variable_name = 'test' #each word is separated by underscore letter


# Assign multiple values

x, y, z = 5,5,[1,2,3]

print(x,y,z)

# Assing one value to multiple variables

x  = y = z = 5

print(x,y,z)

# Unpack a collection

# If we have a collection of values in list, tuples etc. Python will allow to extract the values into  variables. This is called unpacking

unpack = [1,2,3]

x,y,z = unpack

print(x,y,z)

# Output variables print()

x = "Python"
y = "new"

print(x)

print(x+y) #used for concatenate for str

x=5
y=5

print(x+y) # int will perform arithmetic operation

print(x,y) #print the variable will separate with commas

# Global Variables

# Variable that are created outside function is called as global variable, Global variable are used both inside and outsde function

x = 'Global'

def set():
    x = 'Local' #treated as like local variable not overwrite global variable value
    print(x)
set()

print(x)

x = 'Global'

def overGlobal():
    global x
    x = 'Local'
    print(x)
overGlobal()

print(x)


#refreshing topics

# variable names
# global varialble
# output variable
# assign multiple values




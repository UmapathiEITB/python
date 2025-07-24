# Python Strings - strings are defined by single or double quotes ('python', "python")

# How to display string literal

print("Python")
print('Python')

# How to assign string to a variable

x = 'python'
x = "python"

# Multiling Strings (By using three single or double quotes - (""" | '''))

x = """
    Hello world
    Hello
"""

x = '''
    Hello world
    Hellos
'''

print(x)


# Strings are Arrays - Squared brackets can ab  used to access elements of the string

x = "python"
print(x[1]) # output will be y

# Looping through strings

for x in "python":
    print(x)

# Length of a string (len())

x = 'python, sd'
print(len(x)) # output will be 10


# Check string if certain character or phrase in a string we can use the keyword "in"

x = 'python data'
print("python" in x) # output will be True
print("pdata" in x) # output will be False

# How to use it an if statement

if "py" in x:
    print("The character is already exists")

# How to check character or phrase is not exist by using keyword "not in"

print("pdata" not in x) # output will be True

if "pdata" not in x:
    print("Character not exist")


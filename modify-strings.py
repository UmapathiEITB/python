# Modify Strings

# Upper Case - the upper() method will returns the string in upper case

x = 'python'
print(x.upper()) # output will be PYTHON

# Lower Case - the lower() method will return the string in lower case

x = 'PYTHON'
print(x.lower()) # output will be python


# Remove white space - the whitespace is the space for actual text from start or the end using strip() method

x = "Hello World"
print(x) # output will be "Hello World"

x = " Hello World"
print(x) # output will be " Hello World"

#lets remove the white space

print(x.strip()) # output will be "Hello World"


# Replace string  - By using replace() method to replace one string to another string (replace will be case sensitive)

x = "Hello World"
print(x.replace("H", "h")) #output will be "hello world"
print(x.replace("Hello","welcome")) #output will "welcome world"

# Split string - the split method returns a list where the text between specified separator

print(x.split(" ")) # output will be ['Hello', 'World']





#String Methods

#Capitalize - Convert the first character to upper case

x = "hello"
print(x.capitalize()) #output will be "Hello"

#Casefold - Convert the string into lower case

"""
This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.
"""

print(x.casefold()) #output will be "hello"

#Center - Returns a centre string  - center(length, character)

print(x.center(7))

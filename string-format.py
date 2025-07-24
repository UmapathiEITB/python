# string Format

a = 36
b = 'txt'
#c = a + b # It wil  throw the error because string is not concatenate with number

# What is the alternate way to use combine by using f-strings or format()

c = f"{b} {a:.2f} {5*6}"
print(c) # output will be "txt 36.00 30"


# Escape Characters

# Single Quote

x = 'singe \'data\'' # output will be "single 'data'" provide (') single quotes
print(x)

# Double Quote

x = 'double \"quote\"'
print(x) # output will be 'double "quote"' provide(") double quotes

# Backslash

x = 'single \\data' #output will be "single \data" provide (\) single slash
print(x)

# New Line

x = "New \nLine"
print(x) #output will print one by one

# Tab

x = "New\tLine"
print(x) #output will be "New   Line"


# Backspace

x = "New \bLine"
print(x) #output will be "NewLine"

x = "New\fLine\ftest"
print(x)

#output will be
#New
#Line
#test

# Octal Value

x = "\110\145\154\154\157"
print(x) # output will be "Hello"

# Hex Value
x = "\x48\x65\x6c\x6c\x6f"
print(x) # output will be "Hello"

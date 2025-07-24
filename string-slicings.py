# Slicing - It will return a range of character by specify the start and the end index, separated by colon, to return the part of the string

# slice string from start to end [start:end]

x = 'python'
print(x[0:1]) # output will be "p"

# Slice from the start  - By leaving start index it will return the string from position 0 to end position [:end]

print(x[:2]) # output will be "py"


# Slice to the End - By leaving end index, the range will go to the end [start:]

print(x[2:]) # output will be "thon"


# negative index - total count of character will start from end position with negetive -1
# start with negative position [start:end:-1]

print(x[-2:-4:-1])
print(x[-4:-2])

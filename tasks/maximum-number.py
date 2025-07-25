#Find the maximum of three numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number:"))

max = a

if b > max:
    max = b
if c > max:
    max = c

print("Maximum value is: ", max)

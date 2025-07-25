#Swap two numbers without using a third variable.

a = int(input("Enter the number (a) : "))
b = int(input("Enter the number (b) : "))

a = a + b
b = a - b
a = a - b

print("a :", a)
print("b :", b)
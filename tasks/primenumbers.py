#Check if a number is prime

import math

a =  int(input("Enter the number: "))

if a < 2:
    print(a," is unqiue number")
else:
    is_prime = True
    for i in range(2,int(math.sqrt(a))+1):
        if(a%i == 0):
            is_prime = False
            break
    if is_prime:
        print(a,"is prime number")
    else:
        print(a, 'is not a prime number')
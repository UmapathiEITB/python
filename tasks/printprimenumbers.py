#Print all prime numbers between 1 and 100

import math

for i in range(1,101):
    if(i == 1):
        print(i,'is a unique number')
    else:
        is_prime = True
        for q in range(2,int(math.sqrt(i))+1):
            if(i%q == 0):
                is_prime = False
                break
        if(is_prime):
            print(i, " is prime number")
        else:
            print(i, " is not a prime number")
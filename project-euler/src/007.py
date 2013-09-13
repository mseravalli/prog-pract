#!/usr/bin/python
import math

def isPrime(num):
    fact = math.ceil(math.sqrt(num))
    while(num % fact != 0):
        fact = fact - 1
    if (fact == num or fact == 1):
        return True
    return False

prime = 1
num = 3
while(prime != 10001):
    if (isPrime(num)):
            prime = prime + 1
    num = num + 2
print (num - 2)

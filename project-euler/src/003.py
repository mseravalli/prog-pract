#!/usr/bin/python
import math

def isPrime(num):
    fact = math.ceil(math.sqrt(num))
    while(num % fact != 0):
        fact = fact - 1
    if (fact == num or fact == 1):
        return True
    return False

num = 600851475143
fact = math.ceil(math.sqrt(num))
isFound = False
while(not isFound):
    if (num % fact == 0):
        if (isPrime(fact)):
            isFound = True
    fact = fact - 1
print (fact + 1)

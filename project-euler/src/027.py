#!/usr/bin/python
import math

def isPrime(num):
    if(num < 2):
        return False
    if(num == 2 or num == 3):
        return True
    if(num % 2 == 0 or num % 3 == 0):
        return False

    isP = True
    for i in range(3, int(math.sqrt(num) + 2), 2):
        if(num % i == 0):
            isP = False
            break

    return isP

def numOfPrimes(a, b):
    primes = 0
    for n in range(0, max(a,b)):
        if(isPrime(n*n + a*n +b)):
            primes += 1
        else:
            break
    return primes

lim = 1000

max_p = 0
max_a = 0
max_b = 0
for a in range(-lim, lim):
    for b in range(-lim, lim):
        n = numOfPrimes(a,b)
        if (n > max_p):
            max_p = n
            max_a = a
            max_b = b

print max_p, max_a, max_b, max_a*max_b

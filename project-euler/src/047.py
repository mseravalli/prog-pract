#!/usr/bin/python
import math

def is_prime(n):
  if n == 2 or n == 3:
    return True

  if n == 1 or n % 2 == 0:
    return False

  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:
      return False

  return True

lim = 200000
tot = 4

primes = set([n for n in range(1, lim) if is_prime(n)])

def factors(n):    
    return set(reduce(list.__add__, 
                    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

count = 0
divisors = set([])
for i in (range(10, lim)):
  divisors.clear()
  divisors = factors(i)

  if len(set.intersection(primes, divisors)) == tot:
    count += 1
  else:
    count = 0

  if count == tot:
    print i - tot + 1 
    break

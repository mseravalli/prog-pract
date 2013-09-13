#!/usr/bin/python
import math

lim = 6000
crossLim = math.ceil(math.sqrt(lim))
primes = [True]*(lim+1)

primes[0] = False
primes[1] = False

for i in range(2, int(crossLim)):
  if (primes[i]):
    for j in range(i*i, lim+1, i):
      primes[j] = False

for i in range(5, lim, 2):
  if (not primes[i]):
    found = False
    j = 1
    while i - (2 * (j**2)) > 0:
      if primes[i - (2 * (j**2))]:
        found = True
        break
      j +=1
    if not found :
      print i
      break

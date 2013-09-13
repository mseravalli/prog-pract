#!/usr/bin/python
import math
import itertools as it
import re

lim = 20000
crossLim = math.ceil(math.sqrt(lim))
primes = [True]*(lim+1)

primes[0] = False
primes[1] = False

for i in range(2, int(crossLim)):
  if (primes[i]):
    for j in range(i*i, lim+1, i):
      primes[j] = False

for i in range(1001, lim/2, 2):
  if primes[i] and primes[i + 3330] and primes[i + 6660]: 
    if set(str(i)) == set(str(i + 3330)) and set(str(i)) == set(str(i + 6660)):
      print i, i + 3330, i + 6660

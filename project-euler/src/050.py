#!/usr/bin/python
import math

#crivello di eratostene
liv = 1000000
thresLiv = int(math.sqrt(liv) + 1)

natPrime = [True]*liv

natPrime[0] = False
natPrime[1] = False

for i in range(2, thresLiv):
    if (natPrime[i]):
        for j in range(i*2, liv, i):
            natPrime[j] = False

primes = []
for i in xrange(len(natPrime)):
    if (natPrime[i] and i < liv / 2):
        primes.append(i)

addends = 0
res = 0
for i in xrange(len(primes)):
    j = 0
    s = 0
    while (s < liv and i + j < len(primes)):
        s += primes[i + j]
        if (s < liv and natPrime[s]):
            if (addends < j):
                addends = j + 1
                res = s
        j += 1


print(res, addends)

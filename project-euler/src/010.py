#!/usr/bin/python
import math

lim = 2000000

crossLim = math.ceil(math.sqrt(lim))

primeList = []

for i in range(0, lim+1):
    primeList.append(True)

primeList[0] = False
primeList[1] = False

for i in range(2, int(crossLim)):
    if (primeList[i]):
        for j in range(i*i, lim+1, i):
            primeList[j] = False

s = 0
for i in range(2, lim+1):
    if (primeList[i]):
        s += i

print (s)

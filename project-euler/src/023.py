#!/usr/bin/python
import math

def divisors(num):
    d = [1]
    for i in range(2, int(math.sqrt(num) + 1)):
        if (num % i == 0):
            d.append(i)
            if (int(num/i) != i):
                d.append(int(num/i))
    return d

lim = 28124
abundants = []

for i in range(10,lim):
    if (sum(divisors(i)) > i):
        abundants.append(i)

isSum = [False]*lim
isAbundant = [False]*lim
for a in abundants:
    isAbundant[a] = True

for i in range(abundants[0],lim):
    for a in abundants:
        if (i - a > 0):
            if(isAbundant[i-a]):
                isSum[i] = True
                break

s = 0

for i in range(0, lim):
    if(not isSum[i]):
        s += i

print s


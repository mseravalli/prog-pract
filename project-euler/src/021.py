#!/usr/bin/python
import math

def divisors(num):
    d = [1]
    for i in range(2, int(math.sqrt(num) + 1)):
        if (num % i == 0):
            d.append(i)
            d.append(int(num/i))
    return d

lim = 10001
isAmicable = [0]*lim

for i in range(2, lim):
    if (isAmicable[i]==0):
        s1 = sum(divisors(i))
        s2 = sum(divisors(s1))
        if (i == s2 and i != s1):
            isAmicable[i] = s1
            isAmicable[s1] = i

print sum(isAmicable)


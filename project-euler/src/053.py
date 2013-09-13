#!/usr/bin/python
import math
lim = 100
count = 0
for i in range(1, lim+1):
  for j in range(i+1):
    c = math.factorial(i)/(math.factorial(j)*math.factorial(i-j))
    if c > 1000000:
      count += 1

print count

#!/usr/bin/python
import math

n = 1
s = 1
    
for n in xrange(2, 10):
  exp = 1
  l = 0
  while l <= exp and exp <= 50:
    p = int(math.pow(n, exp))
    l = len(str(p))
    if l == exp:
      s += 1
    exp += 1

print s


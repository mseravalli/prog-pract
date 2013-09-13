#!/usr/bin/python
import numpy as np

def fact(n):
  res = 1
  for i in range(1, n+1):
    res *= i

  return res

count = 0

for i in range(3, 50000):
  s = 0
  for n in list(str(i)):
    s += fact(int(n))

  if s == i:
    count += i
    print s

print count

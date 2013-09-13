#!/bin/python
def rev(n): return int(str(n)[::-1])

def is_ly(n):
  for i in range(0,50):
    n = n+rev(n)
    if str(n)==str(rev(n)): return 0
  return 1

print sum(is_ly(n) for n in range(10000))

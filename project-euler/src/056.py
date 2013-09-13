#!/bin/python

def dig_sum(n):
  return sum(int(i) for i in str(n))

lim = 100
print max([dig_sum(a**b) for a in range(lim) for b in range(lim)])

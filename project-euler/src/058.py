#!/bin/python
import math

# generate primes
def is_prime(n):
  if n % 2 == 0: return False
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0: return False
  return True

def p_in_l(l):
  n = 2*l + 1
  count = 0
  for i in range(1, 4):
    if is_prime(n*n - i*n + i): count += 1
  return count
 
found = False
l = 1
p = 0
n = 1
while (not found):
  p += p_in_l(l)
  n += 4
  if float(p)/float(n) < 0.1:
    print 2*l + 1, p, n
    found = True
  l += 1

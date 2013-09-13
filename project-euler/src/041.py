#!/usr/bin/python
import math

def is_pan(s):
  l = len(s)
  digits = [0]*(l + 1)
  for d in list(s):
    if int(d) >= l + 1: return False
    digits[int(d)] += 1
  is_p = digits[0] == 0
  for i in range(1, l + 1):
     is_p &= digits[i] == 1 
  return is_p

def is_prime(n):
  if n == 2 or n == 3:
    return True
  if n == 1 or n % 2 == 0:
    return False
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:
      return False
  return True

lim = 9999999
m = 0
for i in xrange(lim, 0, -2):
  if is_pan(str(i)):
    if is_prime(i):
      print i
      break

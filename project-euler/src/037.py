#!/usr/bin/python
import math

def truncate(n):
  l = set([n])
  n_str = str(n)
  len_n_str = len(n_str)
  for i in range(1, len_n_str):
    l.add(int(n_str[i:]))
    l.add(int(n_str[:-i]))
    
  return l

def isPrime(n):
  if n == 2 or n == 3:
    return True

  if n == 1 or n % 2 == 0:
    return False

  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:
      return False

  return True

s = 0
for i in range(9, 1000000, 2):
  is_trunc_p = True
  for n in truncate(i):
    is_trunc_p &= isPrime(n)

  if is_trunc_p:
    print i
    s += i

print s

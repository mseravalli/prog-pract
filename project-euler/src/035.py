#!/usr/bin/python
import math

def rotate(n):
  l = []
  n_str = str(n)
  len_n_str = len(n_str)
  for i in range(0, len_n_str):
    s = ''
    for j in range(i, i + len_n_str):
      s += n_str[j % len_n_str]

    l.append(int(s))
    
  return l

def isPrime(n):
  if n == 2 or n == 3:
    return True

  if n % 2 == 0:
    return False

  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:
      return False

  return True

# 2 already taken into account
s = 1
for i in range(3, 1000000, 2):
  is_circle_p = True
  for n in rotate(i):
    is_circle_p &= isPrime(n)

  if is_circle_p:
    s += 1

print s

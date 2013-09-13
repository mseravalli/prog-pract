#!/usr/bin/python
import math

lim = 100 + 1
crossLim = math.ceil(math.sqrt(lim))
primes = [True]*(lim+1)

primes[0] = False
primes[1] = False

for i in range(2, int(crossLim)):
  if (primes[i]):
    for j in range(i*i, lim+1, i):
      primes[j] = False

primes_l = []
for i in range(2, lim):
  if primes[i]:
    primes_l.append(i)

def ways(i, j):
  res = 0
  for k in range(j+1):
    if i == primes_l[k]:
      res += 1
    elif i > primes_l[k]:
      res += ways(i-primes_l[k], k)
    else:
      break
  return res

for i in range(4, lim):
  for j in range(len(primes_l)):
    if primes_l[j] > i:
      break
  if ways(i, j) > 5000:
    print i
    break


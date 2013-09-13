#!/usr/bin/python
import itertools as it
import math
import time

def is_prime(n):
  if n <= 1: return False
  if n == 2: return True
  if n % 2 == 0: return False
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0: return False
  return True

lim = 10000
primes = [str(i) for i in range(3,lim,2)  if is_prime(i)]

start = time.time()

pair_primes = {}
for pair in it.combinations(primes, 2):
  are_p = True
  n_0 = int(pair[0]+pair[1])
  n_1 = int(pair[1]+pair[0])
  if not (is_prime(n_0) and is_prime(n_1)):
    are_p = False
  if are_p:
    p_0 = int(pair[0])
    p_1 = int(pair[1])
    try:
      pair_primes[min(p_0, p_1)].add(max(p_0, p_1))
    except:
      pair_primes[min(p_0, p_1)] = set([max(p_0, p_1)])

end = time.time()
print end - start

start = time.time()

def find_group(p, group, lev, lim):
  if lev == lim:
    return p
  for n in group:
    try:
      res = find_group(n, group & pair_primes[n], lev+1, lim)
    except:
      res = find_group(n, set(), lev+1, lim)
    if res > 0:
      return res + p
  return 0

for key in pair_primes.keys():
  res = find_group(key, pair_primes[key], 1, 5)
  if res > 0: print key, res

end = time.time()
print end - start

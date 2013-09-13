#!/usr/bin/python
# pretty crappy solution but it works
# TODO: new implementation, create and apply masks
import re

def get_mask(a, b):
  diff_els = len (set(str(a)) - set(str(b)))
  if diff_els == 0 or diff_els == 1:
    m = str(abs(a-b))
    if len(set(m) - set('0')) == 1:
      inv_a = str(a)[::-1]
      inv_b = str(b)[::-1]
      inv_m = str(m)[::-1]

      a_dig = ''
      b_dig = ''
      for i in range(len(inv_m)):
        if inv_m[i] != '0':
          a_dig += a_dig + inv_a[i]
          b_dig += b_dig + inv_b[i]

      if len(set(a_dig)) == 1 and len(set(b_dig)) == 1:
        return re.sub('[2-9]', '1', m)

  return ''

# generate primes
lim = 1000000
isPrime = [True]*lim
isPrime[0] = False
isPrime[1] = False

for i in range(lim):
  if not isPrime[i]:
    continue
  for j in range(i*2, lim, i):
    isPrime[j] = False

primes = []
for i in range(lim):
  if isPrime[i]:
    primes.append(i)

# group by length
p_by_len = {}
for p in primes:
  try:
    p_by_len[len(str(p))].append(p)
  except:
    p_by_len[len(str(p))] = [p]
    
# group by ending
for l in p_by_len.keys():
  p_by_end = {}
  for p in p_by_len[l]:
    try:
      p_by_end[str(p)[-1]].append(p)
    except:
      p_by_end[str(p)[-1]] = [p]
    
  for e in p_by_end.keys():
    n = len(p_by_end[e])
    p = p_by_end[e]
    for i in range(n):
      masks = {}
      for j in range(i+1,n):
        m = get_mask(p[i], p[j])
        if len(m) > 0:
          try:
            masks[m] += 1
          except:
            masks[m] = 1
      for m in masks.keys():
        if masks[m] >= 7:
          print masks
          print p[i], m
          exit(0)


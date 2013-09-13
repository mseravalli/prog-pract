#!/usr/bin/python

def isPand(digits):
  if digits[0] != 0:
    return False
  res = True
  for i in range(1, 10):
    res &= digits[i] == 1

  return res

for i in xrange(100000):
  digits = [0]*10
  for j in range(1, 10):
    r = str(i * j)
    for d in list(r):
      digits[int(d)] += 1

    if isPand(digits):
      print i
      break

    


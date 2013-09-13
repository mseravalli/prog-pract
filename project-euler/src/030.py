#!/usr/bin/python
import numpy as np

lim = 100000000
exp = 5
count = 0

for n in range(2, lim):
  s = 0
  for c in list(str(n)):
    s += int(c) ** exp

  if (s == n):
    print n
    count += n

print count

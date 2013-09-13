#!/usr/bin/python
import numpy as np

max_a = 100
max_b = 100

res_set = set([])

for a in range(2, max_a + 1):
  for b in range(2, max_b + 1):
    res_set.add(a**b)

print len(res_set)

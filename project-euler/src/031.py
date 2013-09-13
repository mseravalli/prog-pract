#!/usr/bin/python
import numpy as np

coins = [200, 100, 50, 20, 10, 5, 2, 1]

def ways(amount, last):
  res = 0
  for c in coins:
    if (c > last):
      continue
    if (amount - c == 0):
      res += 1
    if (amount - c > 0):
      res += ways(amount - c, c)

  return res

print ways(200,coins[0])

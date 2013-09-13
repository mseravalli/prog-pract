#!/usr/bin/python
import numpy as np

n = 100
coins = []
for i in range(1, n+1):
  coins.append(i)

table = np.zeros((n+1, len(coins)))

for i in range(2, n+1):
  for j in range(len(coins)):
    c = coins[j]
    if c >= i:
      break
    s = 0
    for k in range(j, len(coins)):
      if i-c >= c: 
        s += table[i-c][k]
    if i-c in coins and i-c >= c:
      s += 1
    table[i][j] = s 

tot = 0
for i in range(len(coins)):
  tot += table[n][i]

print tot

#!/usr/bin/python

def num_of_sol(perim):
  tot = 0
  for a in range(1, perim / 2):
    for b in range(1, perim / 2 + 1):
      if (perim-a-b)*(perim-a-b) - a*a + b*b == 0:
        tot += 1
        break

  return tot

m = 0
p = 0
for i in range(1, 1000):
  temp = num_of_sol(i)
  if temp > m:
    m = temp
    p = i

print p, m    

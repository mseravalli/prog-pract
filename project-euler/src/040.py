#!/usr/bin/python
s = '.'

for i in range(1, 1000001):
  s += str(i)

tot = 1
mult = 1
for i in range(0, 7):
  tot *= int(s[mult])
  mult *= 10

print tot

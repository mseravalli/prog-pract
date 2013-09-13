#!/usr/bin/python

s = 1.0

for den in range(10, 100):
  for num in range(10, den):
    if (den % 10 == 0): continue
    if(float(num) / den == float(int(num/10)) / (den % 10) and (num%10) == int(den/10)):
      s *= float(int(num/10)) / (den % 10)

print s

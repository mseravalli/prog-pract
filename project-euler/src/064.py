#!/usr/bin/python
import math

lim = 10000
count = 0
for i in xrange(2, lim + 1):
  D = i
  a_0 = math.floor(math.sqrt(D))

  P = 0.0
  Q = 1.0
  a = a_0
  conv = []

  while not (2*a_0 in conv):
    P = a*Q - P
    Q = (D-(P*P))/Q
    if (Q == 0):
      break
    a = math.floor((a_0 + P) / Q)
    conv.append(a)

  if len(conv) % 2 == 1:
    count += 1
print count

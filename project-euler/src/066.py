#!/usr/bin/python
import math

def get_conv(D):
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

  conv.insert(0,a_0)
  return conv

def pq_from_conv(a):
  p_1 = a[0]
  q_1 = 1
  p = a[0]*a[1] + 1
  q = a[1]
  r = len(a)-2
  lim = r
  if (r % 2 == 0):
    lim = 2*r + 1
  for i in xrange(2, lim + 1):
    n = 1 + ((i-1) % (r+1))
    tmp = p
    p = a[n]*p + p_1
    p_1 = tmp
    tmp = q
    q = a[n]*q + q_1
    q_1 = tmp

  return [p,q]

max_x = 0
max_D = 0
for i in xrange(2, 1000):
  conv = get_conv(i)
  if (len(conv) > 1):
    p,q = pq_from_conv(conv)
    if (p > max_x):
      max_x = p
      max_D = i

print max_D

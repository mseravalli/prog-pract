#!/bin/python

def alien_num(a_n, src, trg):
  base_src = len(src)
  base_trg = len(trg)
  
  digits_src = [ d for d in src ]
  digits_trg = [ d for d in trg ]

  num = 0
  base = 1

  for i in reversed(range(len(a_n))):
    for j in range(base_src):
      if (digits_src[j]== a_n[i]):
        num += j * base
    base *= base_src

  num_trg = ''
  while num > 0:
    num_trg = digits_trg[num%base_trg] + num_trg 
    num /= base_trg

  return num_trg

n = int(raw_input())

for i in range(n):
  a_n, src, trg = str.split(raw_input())
  res = str(alien_num(a_n, src, trg))
  print 'Case #%d: %s' % (i+1, res)

#!/usr/bin/python
import itertools
digits = '234567890'
for i in range(1, 10):
  for c in itertools.combinations(digits, i):
    for p in itertools.permutations(c):
      n = '1' + ''.join(p)
      n_set = set(n)
      same_digits = True
      for j in range(2, 7):
        mult_set = set( str(int(n)*j) )
        if len( n_set - mult_set ) != 0:
          same_digits = False
      if same_digits:
        print n
        exit(0)

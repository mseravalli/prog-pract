#!/usr/bin/python

pans = [i for i in map(str, range(100, 1000)) if len(i) == len(set(i))]
for x in [2, 3, 5, 7, 11, 13, 17]:
  pans = [p + i for i in map(str, range(10)) for p in pans if i not in p and int(p[-2:] + i) % x == 0]
print sum(map(int, pans))

# import itertools as it
# import re
#
# perm = it.permutations('0123456789')
#
# primes = [2,3,5,7,11,13,17]
#
# s = 0
# for p in list(perm):
#   p_str = re.sub(r"[(),' ]", "", str(p))
#   if p_str[0] == 0 or int(p_str[3]) % 2 != 0 : continue
#   is_divis = True
#   for i in range(0, len(primes)):
#     is_divis &= int(p_str[i+1:i+4]) % primes[i] == 0
#
#   if is_divis:
#     s += int(p_str)
#     print p_str
#
#
# print s


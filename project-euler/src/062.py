#!/usr/bin/python
import collections

lim = 100000
cubes = {}
for i in xrange(lim):
  c = i*i*i
  try:
    cubes[len(str(c))].append(c)
  except:
    cubes[len(str(c))] = [c]

def is_permutation(a, b):
  d = collections.defaultdict(int)
  for x in str(a):
    d[x] += 1
  for x in str(b):
    d[x] -= 1
  return not any(d.itervalues())

for n in cubes.keys():
  for i in xrange(len(cubes[n])):
    c_small = cubes[n][i]
    count = 1
    for j in xrange(i + 1, len(cubes[n])):
      c_large = cubes[n][j]
      if is_permutation(c_small, c_large):
        count += 1
    if count == 5:
      print c_small
      exit(0)   

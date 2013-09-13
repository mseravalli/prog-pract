#!/usr/bin/python
# pent = set([])
#
# for n in range(1, 10000):
#   pent.add(n*(3*n-1)/2)
#
# d = float('inf')
# for i in pent:
#   for j in pent:
#     if i != j and i-j in pent and i+j in pent:
#       if abs(i - j) < d:
#         d = abs(i - j)
#
# print d

p = [n*(3*n-1)/2 for n in xrange(1, 10000)]
ps = set(p)

sums = []
for j in xrange(1, len(p)):
     for k in xrange(1, j):
             if p[j] + p[k] in ps and p[j] - p[k] in ps:
                        sums.append(p[j]-p[k])

print sums

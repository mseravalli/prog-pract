#!/bin/python
f = file('079.txt')
dig = {}

for l in f:
  for i in range(len(l)):
    d_i = l[i]
    if d_i == '\n': continue
    for j in range(i+1,len(l)):
      d_j = l[j]
      if d_j == '\n': continue
      try:
        dig[int(d_i)].add(d_j)
      except:
        dig[int(d_i)] = set([d_j])
f.close()

# compares sets in dig by len
# assumptions(which is valid for this case)
# different digits, different length
# digits occur only once
def cmp(a, b):
  return len(dig[b]) - len(dig[a])

res_but_last = list(dig)
res_but_last.sort(cmp)
last = [int(d) for d in list(dig[res_but_last[-1]])]
print res_but_last + last




#!/usr/bin/python
def p3n (n): return n*(n+1)/2
def p4n (n): return n*n
def p5n (n): return n*(3*n - 1)/2
def p6n (n): return n*(2*n - 1)
def p7n (n): return n*(5*n - 3)/2
def p8n (n): return n*(3*n - 2)

fig_nums = [[] for _ in range(6)]

for i in xrange(1000):
  if len(str(p3n(i))) == 4: fig_nums[0].append(p3n(i))
  if len(str(p4n(i))) == 4: fig_nums[1].append(p4n(i))
  if len(str(p5n(i))) == 4: fig_nums[2].append(p5n(i))
  if len(str(p6n(i))) == 4: fig_nums[3].append(p6n(i))
  if len(str(p7n(i))) == 4: fig_nums[4].append(p7n(i))
  if len(str(p8n(i))) == 4: fig_nums[5].append(p8n(i))

def cycle(first, last, checked):
  curr = max(checked)
  for i in xrange(len(checked)):
    if curr < 6 and checked[i] == 0:
      checked[i] = curr + 1
      for n in fig_nums[i]:
        if str(last)[2:] == str(n)[:2]:
          res = cycle(first, n, checked)
          if res != 0:
            return n + res
      checked[i] = 0
    elif curr == 6 and checked[i] == 1:
      if str(last)[2:] == str(first)[:2]:
        return first
  return 0
       
print fig_nums
checked = [0]* 6
checked[0] = 1
for n in fig_nums[0]:
  res = cycle(n, n, checked) 
  if res != 0:
    print res
    exit(0)



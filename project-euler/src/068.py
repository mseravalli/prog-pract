#!/bin/python

def is_valid(magic, lim):
  l = len(magic)
  res = True
  for i in xrange(1, l, 2):
    a = magic[i % l]
    b = magic[(i - 1) % l]
    c = magic[(i + 1) % l]
    s = a + b + c
    if a > 0 and b > 0 and c > 0:
      res = res and (s == lim)
    else:
      res = res and (s <= lim)
  return res

def max_num(a, b):
  m = ''
  lim = 16
  if (len(a) > lim):
    m = b
  elif (len(b) > lim):
    m = a
  else:
    m = max(a, b)
  return m

def to_str(magic):
  l = len(magic)
  m = l
  m_idx = -1
  for i in xrange(1, l, 2):
    if (magic[i] < m):
      m = magic[i]
      m_idx = i 

  s = ''
  for i in xrange(l / 2):
    s += str(magic[ m_idx % l])
    s += str(magic[(m_idx - 1) % l])
    s += str(magic[(m_idx + 1) % l])
    m_idx += 2
  return s 


def attempt(magic, is_avail, x, lim):
  if (max(is_avail) == 0 and x == len(is_avail)):
    return to_str(magic)
     
  res = ''

  for i in xrange(len(is_avail)):
    if (is_avail[i]):
      is_avail[i] = False
      magic[x] = i + 1
  
      if (is_valid(magic, lim)):
        res = max_num(res, attempt(magic, is_avail, x+1, lim))


      magic[x] = 0
      is_avail[i] = True

  return res

size = 10
magic = [0]*size
is_avail= [True]*size
ans = ''

for lim in xrange(1 + 2 + size, 1 + (size-1) + size + 1):
  ans = max(ans, attempt(magic, is_avail, 0, lim))
print ans

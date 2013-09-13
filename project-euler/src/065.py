#!/usr/bin/python

class Frac:
  num = 1
  den = 1
  
  def __init__(self, n, d):
    self.num = n
    self.den = d
  
  def add(self, n):
    self.num += n * self.den
  
  def inv(self):
    tmp = self.num
    self.num = self.den
    self.den = tmp
  
  def is_num_longer(self):
    return len(str(self.num)) > len(str(self.den))

  def __str__(self):
    return str(self.num) + '/' + str(self.den)    

def set_c(n):
  c = 1
  if (n + 1) % 3 == 0:
    c = (n + 1) * 2 / 3
  return c

lim = 100-1

f = Frac(1, set_c(lim))
for i in reversed(xrange(1, lim)):
  f.add(set_c(i))
  f.inv()
    
f.add(2)

print sum([int(d) for d in str(f.num)])

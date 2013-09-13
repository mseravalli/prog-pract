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

lim = 1000
count = 0

for i in xrange(lim):
  f = Frac(1, 2)
  for j in xrange(i):
    f.add(2)
    f.inv()
    
  f.add(1)
  if f.is_num_longer():
    count += 1

print count

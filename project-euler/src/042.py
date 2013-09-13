#!/usr/bin/python

fo = open("042.txt", "r")

triang = set([])
for i in range(1, 100):
  triang.add( (i*(i+1)/2) )

count = 0
for l in fo.readline().split(','):
  l = l.replace('"', '').lower()
  s = 0
  for c in list(l):
    s += ord(c) - 96
  if s in triang:
    count += 1

print count

fo.close()

#!/usr/bin/python
import numpy as np

fo = open("022.txt", "r") 
lines = fo.readlines()
fo.close()

names = []

for l in lines:
    for w in l.split(","):
        names.append(w.replace('"', ''))

names.sort()

s = 0
for i in xrange(len(names)): 
    s += (i+1) * sum(ord(c) - 64 for c in list(names[i]))

print s
    

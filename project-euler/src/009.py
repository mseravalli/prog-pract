#!/usr/bin/python
import math

solFound = False

for a in range(1, 500):
    for b in range(a+1, 500):
        c = math.sqrt(a**2 + b**2)
        if (a + b + c == 1000):
            print (a, b, c, a*b*c)
            solFound = True
            break

if (not solFound):
    print ("solution not found")

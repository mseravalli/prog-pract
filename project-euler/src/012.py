#!/usr/bin/python
import math

divisor = 1
triang = 0
natural = 1

while (divisor < 500):
    triang += natural
    natural += 1
    divisor = 1 
    for i in range (1, int(math.sqrt(triang/2 + 1))):
        if (triang % i == 0):
            divisor += 2
print (triang)

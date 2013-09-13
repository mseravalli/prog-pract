#!/usr/bin/python
import numpy as np

fo = open("067.txt", "r") 
lines = fo.readlines()
fo.close()

dim = int(len(lines))
triangle = np.zeros((dim, dim))
path = np.zeros((dim, dim))

i = 0
for l in lines:
    j = 0
    for num in str(l).split():
        triangle[i][j] = int(num)
        j += 1
    i += 1

for i in reversed(range(0, dim - 1)):
    for j in range(0, i+1):
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

print int(triangle[0][0])

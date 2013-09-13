#!/usr/bin/python
import numpy as np

fo = open("011.txt", "r") 
n = 20
grid = np.zeros((n,n))
for i in xrange(n):
    for j in xrange(n):
        grid[i][j] = int(fo.read(3))

fo.close()

res = 0
length = 4

#horizontal
for i in range(0, n):
    for j in range(0, n-length):
        tmp = 1
        for k in range(0, length):
            tmp *= grid[i][j+k]
            if (tmp > res):
                res = tmp

#vertical
for i in range(0, n-length):
    for j in range(0, n):
        tmp = 1
        for k in range(0, length):
            tmp *= grid[i+k][j]
            if (tmp > res):
                res = tmp

#diagonal 1
for i in range(0, n-length):
    for j in range(0, n-length):
        tmp = 1
        for k in range(0, length):
            tmp *= grid[i+k][j+k]
            if (tmp > res):
                res = tmp

#diagonal 2
for i in range(length-1, n):
    for j in range(0, n-length):
        tmp = 1
        for k in range(0, length):
            tmp *= grid[i-k][j+k]
            if (tmp > res):
                res = tmp

print (res)

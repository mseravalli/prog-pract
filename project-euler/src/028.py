#!/usr/bin/python
import numpy as np

dim = 1001
grid = np.zeros((dim,dim))

x = dim / 2
y = dim / 2
count = 1

grid[x][y] = count
count += 1

incr = 1

isHDone = False
isVDone = False

while(not isHDone or not isVDone):
    if(not isVDone):
        for j in range(0, incr):
            y +=1
            if (y<0 or y>=dim):
                y -= 1
                isHDone = True
                break
            else:
                grid[x][y] = count
                count += 1
    if(not isHDone):
        for i in range(0, incr):
            x +=1
            if (x<0 or x>=dim):
                x -=1
                isVDone = True
                break
            else:
                grid[x][y] = count
                count += 1

    if(isHDone or isVDone):
        break
    incr += 1

    if(not isVDone):
        for j in range(0, incr):
            y -=1
            if (y<0 or y>=dim):
                y += 1
                isHDone = True
                break
            else:
                grid[x][y] = count
                count += 1
    if(not isHDone):
        for i in range(0, incr):
            x -=1
            if (x<0 or x>=dim):
                x +=1
                isVDone = True
                break
            else:
                grid[x][y] = count
                count += 1

    incr += 1

s = 0
for i in range(0,dim):
    s+= grid[i][i]
    s+= grid[dim-i-1][i]

print s - grid[dim/2][dim/2]

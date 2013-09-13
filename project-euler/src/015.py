#!/usr/bin/python
import numpy as np

dim = 20 + 1
grid = np.zeros((dim, dim))

for k in range(dim - 2, -1, -1):
    grid[k][dim-1] = 1
    grid[dim-1][k] = 1

for i in range(dim - 2, -1, -1):
    for j in range(dim - 2, -1, -1):
        grid[i][j] = grid[i+1][j] + grid[i][j+1]

print(grid[0][0])

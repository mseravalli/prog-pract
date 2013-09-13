#!/bin/python

N = 1
S = 2
W = 4
E = 8

turn_r = {N:E, E:S, S:W, W:N}
turn_l = {N:W, W:S, S:E, E:N}
opp    = {N:S, S:N, E:W, W:E}

def walk(path, dir_start):
  d = dir_start
  max_path = {N:0, E:0, S:0, W:0}
  rel_path = {N:0, E:0, S:0, W:0}
  for i in range(len(path)):
    if path[i] == 'W':
      if i > 0 and i < len(path) - 1:
        rel_path[d] += 1
        rel_path[opp[d]] -= 1
        if rel_path[d] > max_path[d]:
          max_path[d] = rel_path[d]
    elif path[i] == 'L':
      d = turn_l[d]
    elif path[i] == 'R':
      d = turn_r[d]
  return max_path, rel_path, d

def populate_maze(m, path, x_start, y_start, d_start):
  x = x_start
  y = y_start
  d = d_start
  for i in range(len(path)):
    if path[i] == 'W':
      if i > 0:
        m[x][y] = m[x][y] | d
      if d == N: x -= 1
      if d == S: x += 1
      if d == W: y -= 1
      if d == E: y += 1
    elif path[i] == 'L':
      d = turn_l[d]
      m[x][y] = m[x][y] & (~d)
    elif path[i] == 'R':
      d = turn_r[d]
      m[x][y] = m[x][y] & (~d)

  return x, y

def maze(frw, bkw):
  max_frw, rel_frw, d_frw_end = walk(frw, S)
  max_bkw, rel_bkw, d_bkd_end = walk(bkw, opp[d_frw_end])
  
  y_dist = rel_frw[E]
  left    = 0
  right   = 0
  y_start = 0
  if y_dist > 0: # end right wrt start
    y_dist  = abs(y_dist)
    left    = max(max_frw[W], max_bkw[W] - y_dist)
    right   = max(max_frw[E] - y_dist, max_bkw[E]) 
    y_start = left 
  elif y_dist < 0: # end left wrt start
    y_dist  = abs(y_dist)
    left    = max(max_frw[W] - y_dist, max_bkw[W])
    right   = max(max_frw[E], max_bkw[E] - y_dist)
    y_start = left + y_dist 
  else:
    left    = max(max_frw[W], max_bkw[W])
    right   = max(max_frw[E], max_bkw[E])
    y_start = left


  x = max(max_frw[N] + max_frw[S] + 1, max_bkw[N] + max_bkw[S] + 1)
  y = left + y_dist + 1 + right 
  m = [[0 for _ in range(y)] for _ in range(x)]

  x_start = -1
  d_start = S
  x_start, y_start = populate_maze(m, frw, x_start, y_start, d_start)
  populate_maze(m, bkw, x_start, y_start, opp[d_frw_end])

  return m

n = int(raw_input())

for i in range(n):
  entr, exit = str.split(raw_input())
  res = (maze(entr, exit))
  print 'Case #%d:' % (i+1)
  for r in res:
    s = ''
    for c in r:
      s = s + hex(c)[2:]
    print s



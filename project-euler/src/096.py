#!/bin/python
import numpy as np

class Item(object):
  start = []
  loop = []
  def __init__(self, s, l):
    self.start = s
    self.loop = l

   
row = Item( [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0]], 
            [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8]])
col = Item( [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8]],
            [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0]]) 
box = Item( [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]],
            [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]) 

def get_missing(s, loop, g):
  missing = set([1,2,3,4,5,6,7,8,9])
  for l in loop:
    c = [s[0]+l[0], s[1]+l[1]]
    if g[c[0], c[1]] != 0:
      if g[c[0], c[1]] in missing:
        missing.remove(int(g[c[0], c[1]]))
      else:
        raise NameError('Duplicate element')
  return missing

def possible_cells(n, s, loop, g):
  cells = [] 
  for l in loop:
    c = [s[0]+l[0], s[1]+l[1]]
    if g[c[0], c[1]] != 0:
      continue
    m_row = get_missing([c[0], 0], row.loop, g)
    m_col = get_missing([0, c[1]], col.loop, g)
    s_box = [c[0] - (c[0]%3), c[1] - (c[1]%3)]
    m_box = get_missing(s_box, box.loop, g)
    if (n in m_row) and (n in m_col) and (n in m_box):
      cells.append(c)
  return cells

def fill_missing(item, g):
  for s in item.start:
    m = get_missing(s, item.loop, g)
    for n in m:
      cells = possible_cells(n, s, item.loop, g)
      if len(cells) == 1:
        c = cells[0]
        g[c[0], c[1]] = n

def blank_cells(g):
  blank = 0
  for i in xrange(9):
    for j in xrange(9):
      if g[i][j] == 0:
        blank += 1
  return blank

def is_valid(item, g):
  for s in item.start:
    els = set()
    for l in item.loop:
      c = [s[0]+l[0], s[1]+l[1]] 
      if g[c[0], c[1]] != 0:
        if g[c[0], c[1]] in els:
          return False
        els.add(g[c[0], c[1]])
  return True

def get_guess(item, g):
  cells = [[0,0]]*10
  num = -1
  m_min = 10
  for s in item.start:
    m = get_missing(s, item.loop, g)
    for n in m:
      c = possible_cells(n, s, item.loop, g)
      if len(c) < len(cells):
        cells = c
        num = n
        m_min = len(m)
      elif len(c) == len(cells) and len(m) < m_min:
        cells = c
        num = n
        m_min = len(m)
  guess = {}
  guess[num] = cells
  return guess

def cpy(f, t):
  for i in xrange(9):
    for j in xrange(9):
      t[i][j] = f[i][j]

def is_guess_right(n, c, g_old):
  g = np.zeros((dim,dim))
  cpy(g_old, g)
  g[c[0], c[1]] = n
  is_done = False
  is_right = False
  try:
    is_done = solve(g)
  except:
    is_right = False
  if is_done and is_valid(row, g) and is_valid(col, g) and is_valid(box, g):
    is_right = True

  if is_right:
    cpy(g, g_old)

  return is_right

def solve(g):
  blank = blank_cells(g) 
  while (blank > 0):
    fill_missing(row, g)
    fill_missing(col, g)
    fill_missing(box, g)
    blank_updt = blank_cells(g) 
    if (blank_updt < blank):
      blank = blank_updt
    else:
      guess = get_guess(box, g)
      for n in guess.keys():
        if len(guess[n]) == 0: # non valid result
          return False
        for c in guess[n]:
          if is_guess_right(n, c, g):
            return True
        return False
  return True

f = open('096.txt')
lines = f.readlines()
f.close()

dim = 9
i = 0
count = 0

while i < len(lines):
  
  if(lines[i].startswith('Grid')):
    print lines[i]
    i += 1
    continue
  else:
    grid = np.zeros((dim,dim))
    for j in xrange(dim):
      for k in xrange(dim):
        grid[j][k] = int(lines[i][k])
      i += 1

  solve(grid)
  print 'solved'
  count += int( str(int(grid[0][0])) +
                str(int(grid[0][1])) + 
                str(int(grid[0][2])) )  

print count

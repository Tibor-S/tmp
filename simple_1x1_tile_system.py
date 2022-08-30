from math import floor, log2
from random import random
from typing import TypedDict


wave: list[list[list[str]]] = []
img1 = [ # 1          2          3          4          5          6          7          8          9         10         11         12         13         14         15         16
  ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000'], # 1
  ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000'], # 2
  ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#FF0000', '#FF0000', '#FF0000', '#000000', '#000000', '#000000'], # 3
  ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#000000', '#000000'], # 4
  ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#FF0000', '#FF0000', '#00FF00', '#00FF00', '#00FF00', '#FF0000', '#FF0000', '#000000'], # 5
  ['#000000', '#000000', '#000000', '#FF0000', '#FF0000', '#FF0000', '#000000', '#000000', '#000000', '#00FF00', '#00FF00', '#000000', '#00FF00', '#00FF00', '#000000', '#000000'], # 6
  ['#000000', '#000000', '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#000000', '#000000', '#00FF00', '#00FF00', '#000000', '#00FF00', '#00FF00', '#000000', '#000000'], # 7
  ['#000000', '#FF0000', '#FF0000', '#00FF00', '#00FF00', '#00FF00', '#FF0000', '#FF0000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000'], # 8
  ['#000000', '#000000', '#00FF00', '#00FF00', '#000000', '#00FF00', '#00FF00', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000'], # 9
  ['#000000', '#000000', '#00FF00', '#00FF00', '#000000', '#00FF00', '#00FF00', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000'], # 10
  ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#FF0000', '#FF0000', '#FF0000', '#000000', '#000000', '#000000', '#000000', '#000000'], # 11
  ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#000000', '#000000', '#000000', '#000000'], # 12
  ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#FF0000', '#FF0000', '#00FF00', '#00FF00', '#00FF00', '#FF0000', '#FF0000', '#000000', '#000000', '#000000'], # 13
  ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#00FF00', '#00FF00', '#000000', '#00FF00', '#00FF00', '#000000', '#000000', '#000000', '#000000'], # 14
  ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#00FF00', '#00FF00', '#000000', '#00FF00', '#00FF00', '#000000', '#000000', '#000000', '#000000'], # 15
  ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000'], # 16
]
img2 = [
  ['#FF0000', '#FF0000', '#FF0000', '#FF0000'],
  ['#FF0000', '#000000', '#00FF00', '#FF0000'],
  ['#FF0000', '#00FF00', '#000000', '#FF0000'],
  ['#FF0000', '#FF0000', '#FF0000', '#FF0000']
]
img3 = [
  ['#FF0000', '#FF0000', '#00FF00', '#000000', '#000000', '#000000', '#000000', '#000000'],
  ['#FF0000', '#00FF00', '#000000', '#000000', '#00FF00', '#00FF00', '#000000', '#000000'],
  ['#00FF00', '#000000', '#000000', '#00FF00', '#FF0000', '#FF0000', '#00FF00', '#000000'],
  ['#000000', '#000000', '#00FF00', '#FF0000', '#FF0000', '#FF0000', '#00FF00', '#000000'],
  ['#000000', '#000000', '#00FF00', '#FF0000', '#FF0000', '#FF0000', '#00FF00', '#000000'],
  ['#000000', '#000000', '#00FF00', '#FF0000', '#FF0000', '#00FF00', '#000000', '#000000'],
  ['#000000', '#000000', '#000000', '#00FF00', '#00FF00', '#000000', '#000000', '#000000'],
  ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000']
]
img4 = [
  ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000'],
  ['#000000', '#00FF00', '#00FF00', '#00FF00', '#00FF00', '#00FF00', '#00FF00', '#000000'],
  ['#000000', '#00FF00', '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#00FF00', '#000000'],
  ['#000000', '#00FF00', '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#00FF00', '#000000'],
  ['#000000', '#00FF00', '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#00FF00', '#000000'],
  ['#000000', '#00FF00', '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#00FF00', '#000000'],
  ['#000000', '#00FF00', '#00FF00', '#00FF00', '#00FF00', '#00FF00', '#00FF00', '#000000'],
  ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000']
]
src = img1
out = []
class tileType(TypedDict):
  cnt: int
  valid: bool
  dir: list[list[str]]
tileSet: dict[str, tileType] = {}
width = 16
height = 16

def setOut():
  out.clear()
  
  for y in range(height):
    out.append([])
    for x in range(width):
      out[-1].append('')
      
def setTiles():
  tileSet.clear()
  
  for y in range(len(src)):
    for x in range(len(src[0])):
      clr = src[y][x]
      directions = [[],[],[],[]]
      cnt = 1
      tile = tileSet.get(clr, None)
      if tile != None:
        directions = tile.get('dir')
        cnt = tile.get('cnt') + 1
      
      coords = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
      for d in range(4):
        cx, cy = coords[d]
        if 0 <= cx and 0 <= cy and cx < len(src) and cy < len(src[0]):
          cClr = src[cy][cx]
          if directions[d].count(cClr) == 0:
            directions[d].append(cClr)
      
      tileSet.__setitem__(clr, {
        'dir': directions,
        'cnt': cnt,
        'valid': True
      })

def setWave():
  wave.clear()
  
  for y in range(height):
    wave.append([])
    for x in range(width):
      wave[-1].append(list(tileSet.keys()))

def entropy(x, y):
  clrs = wave[y][x]
  cnts = [tileSet.get(clr).get('cnt') for clr in clrs]
  tot = sum(cnts)
  return sum([-(c/tot)*log2(c/tot) for c in cnts])
  
def lstEntropy():
  lx = -1
  ly = -1
  le = 0
  ents = [(x, y, entropy(x, y)) for y in range(height) for x in range(width)]
  for x, y, e in ents:
    if e != 0 and (le == 0 or e < le):
      lx = x
      ly = y
      le = e
      
  return lx, ly, le
  
def collapse(x, y):
  clrs = wave[y][x]
  cnts = [tileSet.get(clr).get('cnt') for clr in clrs]
  tot = sum(cnts)
  rn = floor(random() * tot) + 1
  i = -1
  while rn > 0:
    i += 1
    rn -= cnts[i]
  
  wave[y][x] = [clrs[i]]

def propogate(x, y):
  clrSet = wave[y][x]
  rules = [[],[],[],[]]
  for clr in clrSet:
    tile = tileSet.get(clr)
    tRules = tile.get('dir')
    for i in range(4):
      for tRule in tRules[i]:
        if rules[i].count(tRule) == 0:
          rules[i].append(tRule)
  
    changed = [False, False, False, False]
    coords = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
    for d in range(4):
      cx, cy = coords[d]
      if 0 <= cx and 0 <= cy and cx < width and cy < height:
        tClrSet = wave[cy][cx]
        remove = []
        for tClr in tClrSet:
          if rules[d].count(tClr) == 0:
            remove.append(tClr)
        for rClr in remove:
          tClrSet.remove(rClr)
        # if remove:
        #   propogate(cx, cy)
        
def toOut():
  out.clear()
  
  for y in range(height):
    out.append([])
    for x in range(width):
      clrSet = wave[y][x]
      rs, gs, bs = ([int(clr[i:i+2], 16) for clr in clrSet] for i in range(1, 7, 2))
      rc, gc, bc = (sum(rs)//len(rs), sum(gs)//len(gs), sum(bs)//len(bs))
      aClr = '#%s%s%s' % (hex(rc)[2:].rjust(2,'0').upper(), hex(gc)[2:].rjust(2,'0').upper(), hex(bc)[2:].rjust(2,'0').upper())
      
      out[-1].append(aClr)
      
def printMap(map):
  for y in range(len(map)):
    for x in range(len(map[y])):
      match map[y][x]:
        case '#000000':
          print('\033[100m • \033[0m', end='')
        case '#FF0000':
          print('\033[41m • \033[0m', end='')
        case '#00FF00':
          print('\033[43m • \033[0m', end='')
        case _:
          print(' • ', end='')
    print('')

def run():
  try:
    setOut()
    setTiles()
    setWave()
    while lstEntropy()[2] != 0:
      x, y, e = lstEntropy()
      print(x, y, e)
      collapse(x,y)
      propogate(x,y)
      toOut()
      printMap(out)
      # [print(x, y, wave[y][x]) for y in range(height) for x in range(width)]
    print('src:')
    printMap(src)
    print('output:')
    printMap(out)
  except:
    run()
  
run()
import array
from math import floor, log2
from random import random


wave = []
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
tileSet = {}
width = 8
height = 8
N = 3

def setOut():
  out.clear()
  
  for y in range(height * N):
    out.append([])
    for x in range(width * N):
      out[-1].append('')
      
def setTiles():
  tileSet.clear()
  ptrnMap = []
  sw = len(src)
  sh = len(src[0])
  
  # Get patterns
  for y in range(sh):
    ptrnMap.append([])
    for x in range(sw):
      ptrn = []
      for oy in range(N):
        ptrn.append([])
        for ox in range(N):
          cx = (x + ox) % sw
          cy = (y + oy) % sh
          ptrn[-1].append(src[cy][cx])
        ptrnMap[-1].append(ptrn)
  
  # Fill tileSet with rules for adjacent tiles
  for y in range(len(ptrnMap)):
    for x in range(len(ptrnMap[0])):
      ptrn = ptrnMap[y][x]
      directions = [[],[],[],[]]
      cnt = 1
      tile = tileSet.get(str(ptrn), None)
      if tile != None:
        directions = tile.get('dir')
        cnt = tile.get('cnt') + 1
      
      coords = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
      for d in range(4):
        cx, cy = coords[d]
        if 0 <= cx and 0 <= cy and cx < len(ptrnMap[0]) and cy < len(ptrnMap):
          cPtrn = str(ptrnMap[cy][cx])
          if directions[d].count(cPtrn) == 0:
            directions[d].append(cPtrn)
      
      tileSet.__setitem__(str(ptrn), {
        'ptrn': ptrn,
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
  sPtrns = wave[y][x]
  cnts = [tileSet.get(sPtrn).get('cnt') for sPtrn in sPtrns]
  tot = sum(cnts)
  rn = floor(random() * tot) + 1
  i = -1
  while rn > 0:
    i += 1
    rn -= cnts[i]
  
  wave[y][x] = [sPtrns[i]]

def propogate(x, y):
  sPtrnSet = wave[y][x]
  rules = [[],[],[],[]]
  for sPtrn in sPtrnSet:
    tile = tileSet.get(sPtrn)
    tRules = tile.get('dir')
    for i in range(4):
      for tRule in tRules[i]:
        if rules[i].count(tRule) == 0:
          rules[i].append(tRule)
  
    coords = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
    for d in range(4):
      cx, cy = coords[d]
      if 0 <= cx and 0 <= cy and cx < width and cy < height:
        tsPtrnSet = wave[cy][cx]
        remove = []
        for tsPtrn in tsPtrnSet:
          if rules[d].count(tsPtrn) == 0:
            remove.append(tsPtrn)
        for rsPtrn in remove:
          tsPtrnSet.remove(rsPtrn)
        
def toOut():
  out.clear()
  setOut()
  
  for y in range(0, height * N, N):
    for x in range(0, width * N, N):
      # print('WAVE COORDS:', x//N, y//N)
      sPtrnSet = wave[y//N][x//N]
      # print('SPTRNSET:', sPtrnSet)
      outPtrn = [[[] for _ in range(N)] for _ in range(N)]
      for sPtrn in sPtrnSet:
        ptrn = tileSet.get(sPtrn).get('ptrn')
        for oy in range(N):
          for ox in range(N):
            outPtrn[oy][ox].append(ptrn[oy][ox])
            # print('CLR AT %d, %d IN PTRN:' % (ox, oy),ptrn[oy][ox])
      # print(outPtrn)
      for oy in range(N):
        for ox in range(N):
          cx = x + ox
          cy = y + oy
          clrSet = outPtrn[oy][ox]
          rs, gs, bs = ([int(clr[i:i+2], 16) for clr in clrSet] for i in range(1, 7, 2))
          rc, gc, bc = (sum(rs)//len(rs), sum(gs)//len(gs), sum(bs)//len(bs))
          aClr = '#%s%s%s' % (hex(rc)[2:].rjust(2,'0').upper(), hex(gc)[2:].rjust(2,'0').upper(), hex(bc)[2:].rjust(2,'0').upper())
          out[cy][cx] = aClr
      
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

def run(failed):
  try:
    setOut()
    setTiles()
    # print('RULES FOR PTRN:', tileSet.get("[['#00FF00', '#FF0000'], ['#00FF00', '#FF0000']]").get('dir'))
    setWave()
    while lstEntropy()[2] != 0:
      x, y, e = lstEntropy()
      # print('LST ENTROPY:', x, y, e)
      collapse(x,y)
      propogate(x,y)
      # print('WAVE AT 1, 0:', wave[0][1])
      toOut()
      printMap(out)
      # [print(x, y, wave[y][x]) for y in range(height) for x in range(width)]
    print('FAILED:', failed)
    print('src:')
    printMap(src)
    print('output:')
    printMap(out)
  except :
    toOut()
    print('output:')
    printMap(out)
    if failed % 1 == 0:
      print('FAILED:', failed)
      return
    run(failed + 1)

run(0)
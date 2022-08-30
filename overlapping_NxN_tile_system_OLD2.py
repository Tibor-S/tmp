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
width = 16
height = 16
N = 3

def setOut():
  out.clear()
  
  for y in range(height):
    out.append([])
    for x in range(width):
      out[-1].append('')
      
def setTiles():
  tileSet.clear()
  sw = len(src[0])
  sh = len(src)
  
  for y in range(sh):
    for x in range(sw):
      ptrn = []
      for oy in range(N):
        ptrn.append([])
        for ox in range(N):
          cx = (x + ox) % sw
          cy = (y + oy) % sh
          ptrn[-1].append(src[cy][cx])
      
      tile = tileSet.get(str(ptrn), None)
      if tile == None:
        tileSet.__setitem__(str(ptrn), {
          'clr': ptrn[N//2][N//2],
          'ptrn': ptrn,
          'rel': [[[] for _ in range(2*N-1)] for _ in range(2*N-1)],
          'cnt': 1,
          'valid': True
        })
      else:
        tile.__setitem__('cnt', tile.get('cnt') + 1)

def setRelations():
  keyMap = []
  rs = 2*N-1
  for _ in range(rs):
    keyMap.append([])
    for _ in range(rs):
      keyMap[-1].append(list(tileSet.keys()))
  
  x, y = N-1, N-1
  for key in keyMap[y][x]:
    tile = tileSet.get(key)
    ptrn = tile.get('ptrn')
    rel = tile.get('rel')
    for y2 in range(rs):
      for x2 in range(rs):
        for key2 in keyMap[y2][x2]:
          tile2 = tileSet.get(key2)
          ptrn2 = tile2.get('ptrn')
          valid = True
          for cx, cy in sharedCells(x, y, x2, y2):
            px, py = toPtrnCoord(cx, cy, x, y)
            px2, py2 = toPtrnCoord(cx, cy, x2, y2)
            if ptrn[py][px] != ptrn2[py2][px2]:
              valid = False
          if valid and len(sharedCells(x, y, x2, y2)) > 0:
            if rel[x2 ][y2].count(key2) == 0:
              rel[x2][y2].append(key2)
              # print('KEY %s ADDED KEY %s TO REL POSITION:' % (key, key2), x2, y2)
  
  # print(len(keyMap))
  a = str(tileSet.get(list(tileSet.keys())[1]).get('rel')[4][4]).replace(']]", ', ']]\n')
  print(list(tileSet.keys())[1])
  print(a)
  # [print([len(c) for c in i]) for i in tileSet.get(list(tileSet.keys())[1]).get('rel')]
    
    
def setWave():
  wave.clear()
  
  for y in range(height):
    wave.append([])
    for x in range(width):
      wave[-1].append(list(tileSet.keys()))

def entropy(x, y):
  sPtrns = wave[y][x]
  cnts = [tileSet.get(sPtrn).get('cnt') for sPtrn in sPtrns]
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
  tile = tileSet.get(sPtrnSet[0])
  relations = tile.get('rel')
  coords = relatedCells(x, y)
  print(coords)
  for cx, cy in coords:
    rx, ry = cx - x + N//2+1, cy - y + N//2+1
    remove = []
    for tsPtrn in wave[cy][cx]:
      if relations[ry][rx].count(tsPtrn) == 0:
        remove.append(tsPtrn)
    for rsPtrn in remove:
      wave[cy][cx].remove(rsPtrn)  
        
def toOut():
  out.clear()
  
  for y in range(height):
    out.append([])
    for x in range(width):
      if wave[y][x]:
        sPtrnSet = wave[y][x]
        clrSet = [tileSet.get(sPtrn).get('clr') for sPtrn in sPtrnSet]
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

def surrCells(x, y):
  coords = []
  for cy in range(y - N//2, y + N//2 + 1):
    for cx in range(x - N//2, x + N//2 + 1):
      if 0 <= cx and cx < width and 0 <= cy and cy < height:
        coords.append((cx, cy))

  return(coords)
  
def relatedCells(x, y):
  coords = []
  for cy in range(y - N + 1, y + N):
    for cx in range(x - N + 1, x + N):
      if 0 <= cx and cx < width and 0 <= cy and cy < height:
        coords.append((cx, cy))

  return(coords)

def sharedCells(x, y, x2, y2):
  L = N//2
  coords = [(cx, cy) for cx, cy in surrCells(x, y) if abs(cx - x2) <= L and abs(cy - y2) <= L]
  return(coords)

def toPtrnCoord(x, y, px, py): # x, y is coord on map and px, py is the coord for the middle cell in the ptrn
  return (x - px + N//2, y - py + N//2)
  
def run(failed):
  try:
    setOut()
    setTiles()
    setRelations()
    setWave()
    while lstEntropy()[2] != 0:
      x, y, e = lstEntropy()
      print(x, y, e)
      collapse(x,y)
      propogate(x,y)
      toOut()
      # printMap(out)
      # [print(x, y, wave[y][x]) for y in range(height) for x in range(width)]
    print('Failed:', failed)
    print('src:')
    printMap(src)
    print('output:')
    printMap(out)
  except:
    # toOut()
    printMap(out)
    # if failed % 10 == 0:
    #   print('FAILED:', failed)
    # run(failed + 1)

setTiles()
setRelations()
setWave()
for i in range(50):
  x, y, e = lstEntropy()
  collapse(x,y)
  propogate(x,y)
toOut()
printMap(out)
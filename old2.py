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
src = img1
out = []
ptrnSet = []
w = 16
h = 16
ps = 3

def setOut():
  out.clear()
  
  for y in range(h):
    out.append([])
    for x in range(w):
      out[-1].append('')

def setPtrns():
  for y in range(len(src) - ps + 1):
    for x in range(len(src[y]) - ps + 1):
      ptrn = []
      for oy in range(ps):
        ptrn.append([])
        for ox in range(ps):
          ptrn[-1].append(src[y + oy][x + ox])
      ptrnSet.append({
        'valid': True,
        'ptrn': ptrn
      })
      
def setWave():
  wave.clear()
  
  for y in range(h):
    wave.append([])
    for x in range(w):
      wave[-1].append([])
      for ptrnObj in ptrnSet:
        wave[-1][-1].append(ptrnObj.copy())
      
def relCoords(x, y):
  o = (ps-1)//2
  return [(nx, ny)for ny in range (y - o, y + o + 1) for nx in range (x - o, x + o + 1) ]  

def validatePtrns():
  for y in range(h):
    for x in range(w):
      # print('x:', x, 'y:', y)
      coords = relCoords(x, y)
      for ptrnObj in wave[y][x]:
        # print('VAL:', x, y, 'NEW PTRN')
        if ptrnObj.get('valid'):
          for cx, cy in coords:
            # print('cx:', cx, 'cy:', cy)
            if cx >= 0 and cy >= 0 and cx < w and cy < h:
              px = cx + (ps-1)//2 - x
              py = cy + (ps-1)//2 - y
              # print('px:', px, 'py:', py)
              if out[cy][cx] != '':
                if ptrnObj.get('ptrn')[py][px] != out[cy][cx]:
                  # print(ptrnObj.get('ptrn')[py][px], out[cy][cx])
                  ptrnObj.__setitem__('valid', False)

def entropy(x, y):
  ptrns = []
  cnt = []
  total = 0
  for ptrnObj in wave[y][x]:
    total += 1
    ptrn = ptrnObj.get('ptrn')
    sPtrn = str(ptrn)
    try:
      pi = ptrns.index(sPtrn)
    except ValueError:
      pi = -1
    if pi == -1:
      ptrns.append(sPtrn)
      cnt.append(1)
    else:
      cnt[pi] += 1
  # print(sum(cnt), total, log2(total))
  return sum([-(c/total)*log2(c/total) for c in cnt]) # simplification of sum(-(1/total)*log_2(1/total), 1 -> total) a.k.a entropy
  
def collapse(x, y):
  allPtrns = wave[y][x].copy()
  valid = [ptrnObj.get('ptrn') for ptrnObj in allPtrns if ptrnObj.get('valid')]
  ptrn = valid[floor(random() * len(valid))]
  coords = relCoords(x, y)
  
  for cx, cy in coords:
    if cx >= 0 and cy >= 0 and cx < w and cy < h:
      px = cx + (ps-1)//2 - x
      py = cy + (ps-1)//2 - y
      # print(x, y, cx, cy, px, py)
      if out[cy][cx] == '':
        out[cy][cx] = ptrn[py][px]

def collapseLst():
  lx = -1
  ly = -1
  le = 0
  
  for y in range(h):
    for x in range(w):
      ent = entropy(x, y)
      # if ent != 0 and (le == 0 or ent < le):
      if out[y][x] == '' and (le == 0 or ent < le):
        le = ent
        lx = x
        ly = y
        
  if (lx != -1 and ly != -1):
    # print('WAVE:', wave[y][x])
    print('COLLAPSE: CELL AT %d, %d WITH %s ENTROPY' % (lx, ly, str(round(le, 2))))
    collapse(lx, ly)
  else:
    print('ERROR: DECIDED TO COLLAPSE %d, %d WITH %s ENTROPY' % (lx, ly, str(round(le, 2))))

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

setOut()
setPtrns()
setWave()
print(entropy(0,0))
while sum([entropy(x,y) for y in range(h) for x in range(w)]) != 0:
  validatePtrns()
  collapseLst()
  printMap(out)
# print(wave)
# print(relCoords(0,0))

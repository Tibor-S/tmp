from math import floor, log2
from random import random


wave = []
collapsed = []
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
ptrnSet = {}
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
  ptrnMap = []
  W = len(src[0]) - ps + 1
  H = len(src) - ps + 1
  
  for y in range(H):
    ptrnMap.append([])
    for x in range(W):
      ptrn = []
      for oy in range(ps):
        ptrn.append([])
        for ox in range(ps):
          ptrn[-1].append(src[y + oy][x + ox])
      ptrnMap[-1].append(ptrn)
  
  for y in range(H): 
    for x in range(W):
      ptrn = ptrnMap[y][x]
      directions = [[],[],[],[]]
      coords = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
      ptrnObj = {
        'ptrn': ptrn.copy(),
        'dir': directions,
        'valid': True,
        'cnt': 1
      }
      cnt = 1
      if ptrnSet.get(str(ptrn), None) != None:
        ptrnObj = ptrnSet.get(str(ptrn))
        directions = ptrnObj.get('dir')
        cnt = ptrnObj.get('cnt') + 1
      
      for d in range(4):
        cx, cy = coords[d]
        if cx >= 0 and cy >= 0 and cx < W and cy < H:
          if directions[d].count(str(ptrnMap[cy][cx])) == 0:
            directions[d].append(str(ptrnMap[cy][cx]))
        
      ptrnObj.__setitem__('dir', directions)
      ptrnObj.__setitem__('cnt', cnt)
      ptrnSet.__setitem__(str(ptrn), ptrnObj)
      
def setWave():
  wave.clear()
  collapsed.clear()
  
  for y in range(h):
    wave.append([])
    collapsed.append([])
    for x in range(w):
      wave[-1].append({})
      collapsed[-1].append(False)
      for (key, ptrnObj) in ptrnSet.items():
        wave[-1][-1].__setitem__(key, ptrnObj.copy())
      
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
  # ptrns = []
  # cnt = []
  # total = 0
  # for ptrnObj in wave[y][x]:
  #   total += 1
  #   ptrn = ptrnObj.get('ptrn')
  #   sPtrn = str(ptrn)
  #   try:
  #     pi = ptrns.index(sPtrn)
  #   except ValueError:
  #     pi = -1
  #   if pi == -1:
  #     ptrns.append(sPtrn)
  #     cnt.append(1)
  #   else:
  #     cnt[pi] += 1
  # print(sum(cnt), total, log2(total))
  # return sum([-(c/total)*log2(c/total) for c in cnt]) # simplification of sum(-(1/total)*log_2(1/total), 1 -> total) a.k.a entropy
  total = sum([ptrnObj.get('cnt') for ptrnObj in wave[y][x].values() if ptrnObj.get('valid')])
  return sum([-(ptrnObj.get('cnt')/total)*log2(ptrnObj.get('cnt')/total) for ptrnObj in wave[y][x].values() if ptrnObj.get('valid')])
  
def collapse(x, y):
  collapsed[y][x] = True
  print('COLLAPSE: CELL AT %d, %d WITH %s ENTROPY' % (x, y, str(round(entropy(x,y), 2))))
  print(sum([b for row in collapsed for b in row]), '/', sum([1 for row in collapsed for _ in row]))
  allPtrnObjs = wave[y][x].copy()
  valid = [ptrnObj for ptrnObj in allPtrnObjs.values() if ptrnObj.get('valid')]
  total = sum([ptrnObj.get('cnt') for ptrnObj in valid])
  rn = floor(random() * total + 1)
  ptrnObj = {}
  for obj in valid:
    rn -= obj.get('cnt')
    if rn <= 0:
      ptrnObj = obj.copy()
      break
  # ptrn = valid[]
  coords = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
  for d in range(4):
    cx, cy = coords[d]
    if cx >= 0 and cy >= 0 and cx < w and cy < h:
      targetPtrnSet = wave[cy][cx]
      for (targetKey, targetPtrnObj) in targetPtrnSet.items():
        if ptrnObj.get('dir')[d].count(targetKey) == 0:
          targetPtrnObj.__setitem__('valid', False)
  print('COLLAPSED CELL TO KEY:', str(ptrnObj.get('ptrn')))
  
  for (cx, cy) in coords:
    if cx >= 0 and cy >= 0 and cx < w and cy < h:
      if entropy(cx, cy) == 0 and collapsed[cy][cx] == False:
        collapse(cx, cy)
  
        
def collapseLst():
  lx = 0
  ly = 0
  le = entropy(0, 0)
  
  for y in range(h):
    for x in range(w):
      ent = entropy(x, y)
      # if ent != 0 and (le == 0 or ent < le):
      if (not collapsed[y][x]) and ent <= le:
        le = ent
        lx = x
        ly = y
        
  if (lx != -1 and ly != -1):
    # print('WAVE:', wave[y][x])
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

def isFinished():
  return sum([b for row in collapsed for b in row]) == w * h

setOut()
setPtrns()
setWave()
# print(wave[0][0].get("[['#000000', '#000000', '#000000'], ['#000000', '#000000', '#000000'], ['#000000', '#000000', '#000000']]").get('cnt'))
# print(wave[0][1].get("[['#000000', '#000000', '#000000'], ['#000000', '#000000', '#000000'], ['#000000', '#000000', '#000000']]").get('valid'))
# print(entropy(0,0))
while not isFinished():
  collapseLst()
# print('WAVE 0 1:', [key for (key, obj) in wave[0][1].items() if obj.get('valid')])
# print('WAVE 1 0:', [key for (key, obj) in wave[1][0].items() if obj.get('valid')])
# print(ptrnSet.get("[['#000000', '#000000', '#FF0000'], ['#000000', '#000000', '#000000'], ['#000000', '#000000', '#000000']]").get('dir')[1])
# print(entropy(1,0))
# print(entropy(0,0))
# while sum([entropy(x,y) for y in range(h) for x in range(w)]) != 0:
#   validatePtrns()
#   collapseLst()
#   printMap(out)
# print(wave)
# print(relCoords(0,0))

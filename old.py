
import math
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

def resetOut():
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
      ptrnSet.append(ptrn)

def setWave():
  wave.clear()
  
  for y in range(len(out)):
    wave.append([])
    for x in range(len(out[y])):
      wave[-1].append([])
  
  
  for y in range(len(out)):
    for x in range(len(out[y])):
      if True: # (x % ((ps + 1)/2) == 0 and y % ((ps + 1)/2) == 0):
        for ptrn in ptrnSet:
          valid = True
          
          for oy in range(ps):
            for ox in range(ps):
              cx = x + ox
              cy = y + oy
              if (cx < w and cy < h):
                clr = out[cy][cx]
                if clr != '' and clr !=ptrn[oy][ox]:
                  valid = False
          
          if valid:  
            for oy in range(ps):
              for ox in range(ps):
                cx = x + ox
                cy = y + oy
                if (cx < w and cy < h):
                  wave[cy][cx].append(ptrn[oy][ox]) 

def entArray():
  entArr = []
  
  for y in range(len(wave)):
    entArr.append([])
    for x in range(len(wave[y])):
      entArr[-1].append(entropy(x, y))
      
  return entArr

def entropy(x, y):
  clrCnt = {}
  total = 0
  for clr in wave[y][x]:
    total += 1
    cnt = clrCnt.setdefault(clr, 0)
    clrCnt[clr] = cnt + 1
  
  ent = 0
  for cnt in clrCnt.values():
    ent -= (cnt/total) * math.log2(cnt / total)
    
  return ent

def collapseCell(x, y):
  total = len(wave[y][x])
  ri = math.floor(total * random())
  out[y][x] = wave[y][x][ri]
  
  # clrCnt = {}
  # total = 0
  # for clr in wave[y][x]:
  #   total += 1
  #   cnt = clrCnt.setdefault(clr, 0)
  #   clrCnt[clr] = cnt + 1

  # com = 0
  # cClr = ''
  # for (clr, cnt) in clrCnt.items():
  #   if cnt >= com:
  #     cClr = clr
  # print(cClr)
  # out[y][x] = cClr

  
def collapseLstEnt():
  entArr = entArray()
  lx = -1
  ly = -1
  le = 0
  
  for y in range(len(entArr)):
    for x in range(len(entArr)):
      ent = entArr[y][x]
      # if ent != 0 and (le == 0 or ent < le):
      if out[y][x] == '' and (le == 0 or ent < le):
        le = ent
        lx = x
        ly = y
        
  if (lx != -1 and ly != -1):
    print('COLLAPSE: CELL AT %d, %d WITH %s ENTROPY' % (lx, ly, str(round(le, 2))))
    collapseCell(lx, ly)
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

def finOut():
  if sum([j for sub in entArray() for j in sub]) == 0:
    for y in range(len(wave)):
      for x in range(len(wave[y])):
        if (out[y][x] == ''):
          out[y][x] = wave[y][x][0]
    

resetOut()
setPtrns()
setWave()
# print(wave)
while sum([j for sub in entArray() for j in sub]) != 0:
  collapseLstEnt()
  printMap(out)
  print('Next')
  setWave()
# print(entropy(0, 0))
# print(entArray())
# print(wave)
finOut()
printMap(out)

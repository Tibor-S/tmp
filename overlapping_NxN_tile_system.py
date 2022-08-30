
from math import floor, log2
from random import random
from time import sleep


ptrnT = list[list[str]]

img1 = [  # 1          2          3          4          5          6          7          8          9         10         11         12         13         14         15         16
    ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
        '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000'],  # 1
    ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
        '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000'],  # 2
    ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
     '#000000', '#000000', '#FF0000', '#FF0000', '#FF0000', '#000000', '#000000', '#000000'],  # 3
    ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
     '#000000', '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#000000', '#000000'],  # 4
    ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
     '#FF0000', '#FF0000', '#00FF00', '#00FF00', '#00FF00', '#FF0000', '#FF0000', '#000000'],  # 5
    ['#000000', '#000000', '#000000', '#FF0000', '#FF0000', '#FF0000', '#000000', '#000000',
     '#000000', '#00FF00', '#00FF00', '#000000', '#00FF00', '#00FF00', '#000000', '#000000'],  # 6
    ['#000000', '#000000', '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#000000',
     '#000000', '#00FF00', '#00FF00', '#000000', '#00FF00', '#00FF00', '#000000', '#000000'],  # 7
    ['#000000', '#FF0000', '#FF0000', '#00FF00', '#00FF00', '#00FF00', '#FF0000', '#FF0000',
     '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000'],  # 8
    ['#000000', '#000000', '#00FF00', '#00FF00', '#000000', '#00FF00', '#00FF00', '#000000',
     '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000'],  # 9
    ['#000000', '#000000', '#00FF00', '#00FF00', '#000000', '#00FF00', '#00FF00', '#000000',
     '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000'],  # 10
    ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
     '#FF0000', '#FF0000', '#FF0000', '#000000', '#000000', '#000000', '#000000', '#000000'],  # 11
    ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#FF0000',
     '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#000000', '#000000', '#000000', '#000000'],  # 12
    ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#FF0000', '#FF0000',
     '#00FF00', '#00FF00', '#00FF00', '#FF0000', '#FF0000', '#000000', '#000000', '#000000'],  # 13
    ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#00FF00',
     '#00FF00', '#000000', '#00FF00', '#00FF00', '#000000', '#000000', '#000000', '#000000'],  # 14
    ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#00FF00',
     '#00FF00', '#000000', '#00FF00', '#00FF00', '#000000', '#000000', '#000000', '#000000'],  # 15
    ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
     '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000'],  # 16
]
img2 = [
    ['#FF0000', '#FF0000', '#FF0000', '#FF0000'],
    ['#FF0000', '#000000', '#00FF00', '#FF0000'],
    ['#FF0000', '#00FF00', '#000000', '#FF0000'],
    ['#FF0000', '#FF0000', '#FF0000', '#FF0000']
]
img3 = [
    ['#FF0000', '#FF0000', '#00FF00', '#000000',
        '#000000', '#000000', '#000000', '#000000'],
    ['#FF0000', '#00FF00', '#000000', '#000000',
     '#00FF00', '#00FF00', '#000000', '#000000'],
    ['#00FF00', '#000000', '#000000', '#00FF00',
     '#FF0000', '#FF0000', '#00FF00', '#000000'],
    ['#000000', '#000000', '#00FF00', '#FF0000',
     '#FF0000', '#FF0000', '#00FF00', '#000000'],
    ['#000000', '#000000', '#00FF00', '#FF0000',
     '#FF0000', '#FF0000', '#00FF00', '#000000'],
    ['#000000', '#000000', '#00FF00', '#FF0000',
     '#FF0000', '#00FF00', '#000000', '#000000'],
    ['#000000', '#000000', '#000000', '#00FF00',
     '#00FF00', '#000000', '#000000', '#000000'],
    ['#000000', '#000000', '#000000', '#000000',
     '#000000', '#000000', '#000000', '#000000']
]
img4 = [
    ['#000000', '#000000', '#000000', '#000000',
        '#000000', '#000000', '#000000', '#000000'],
    ['#000000', '#00FF00', '#00FF00', '#00FF00',
     '#00FF00', '#00FF00', '#00FF00', '#000000'],
    ['#000000', '#00FF00', '#FF0000', '#FF0000',
     '#FF0000', '#FF0000', '#00FF00', '#000000'],
    ['#000000', '#00FF00', '#FF0000', '#FF0000',
     '#FF0000', '#FF0000', '#00FF00', '#000000'],
    ['#000000', '#00FF00', '#FF0000', '#FF0000',
     '#FF0000', '#FF0000', '#00FF00', '#000000'],
    ['#000000', '#00FF00', '#FF0000', '#FF0000',
     '#FF0000', '#FF0000', '#00FF00', '#000000'],
    ['#000000', '#00FF00', '#00FF00', '#00FF00',
     '#00FF00', '#00FF00', '#00FF00', '#000000'],
    ['#000000', '#000000', '#000000', '#000000',
     '#000000', '#000000', '#000000', '#000000']
]
width = 16
height = 16
wave: list[list[list[str]]] = []
collapsed: list[list[bool]] = []
collapseNxt: list[tuple[int, int]] = [(0, 0)]
out: list[list[str]] = []
ptrnMap: list[list[list[str]]] = []
ptrns: dict[str, ptrnT] = {}
count: dict[str, int] = {}
relations: dict[str, list[list[str]]] = {}
N = 3
src = img1


def avgClr(clrs: list[str]):
    try:
        rs, gs, bs = ([int(clr[i:i+2], 16) for clr in clrs]
                      for i in range(1, 7, 2))
        rc, gc, bc = (sum(rs)//len(rs), sum(gs)//len(gs), sum(bs)//len(bs))
        return '#%s%s%s' % (hex(rc)[2:].rjust(2, '0').upper(), hex(gc)[2:].rjust(2, '0').upper(), hex(bc)[2:].rjust(2, '0').upper())
    except:
        return '#0123456'


def sharedCells(x, y, x2, y2):
    return [(cx, cy) for cy in range(y, y + N) for cx in range(x, x + N) if cx >= x2 and cy >= y2 and cx < x2 + N and cy < y2 + N]


def toPtrnCoord(x, y, dx, dy):
    return dx - x, dy - y


def rInList(cnts: list[int]):
    tot = sum(cnts)
    rn = floor(random() * tot) + 1
    ri = -1
    while rn > 0:
        ri += 1
        rn -= cnts[ri]
    return ri


def entropy(x, y):
    cnts = [count.get(key) for key in wave[y][x]]
    tot = sum(cnts)
    return sum([-(c/tot)*log2(c/tot) for c in cnts])


def lstEntropy():
    lx, ly, le = -1, -1, 0
    allEnts = [(x, y, entropy(x, y))
               for y in range(height) for x in range(width)]
    for x, y, ent in allEnts:
        if ent != 0 and (le == 0 or ent < le):
            lx, ly, le = x, y, ent

    return lx, ly, le


def setWave():
    wave.clear()
    collapsed.clear()
    collapseNxt.clear()
    collapseNxt.append((0, 0))
    [wave.append([[key for key in ptrns.keys()] for _ in range(width)])
     for _ in range(height)]
    [collapsed.append([False for _ in range(width)]) for _ in range(height)]


def setOut():
    out.clear()
    [out.append([avgClr([ptrns.get(key)[0][0] for key in cell])
                for cell in row]) for row in wave]


def setPtrns():
    ptrns.clear()
    ptrnMap.clear()
    # Get all ptrns
    sh = len(src)
    sw = len(src[0])
    for y in range(sh):
        for x in range(sw):
            ptrn: ptrnT = []
            for oy in range(N):
                ptrn.append([])
                for ox in range(N):
                    ptrn[-1].append(src[(y + oy) % sh][(x + ox) % sw])
            key = str(ptrn)
            exists = ptrns.get(key, None) != None
            if exists:
                count.__setitem__(key, count.get(key) + 1)
            else:
                ptrns.__setitem__(key, ptrn)
                count.__setitem__(key, 1)

    # Check which ptrns overlap
    for key, ptrn in ptrns.items():
        relList = [[], [], [], []]
        coordComb = [((0, 1), (0, 0)), ((0, 0), (1, 0)),
                     ((0, 0), (0, 1)), ((1, 0), (0, 0))]
        for key2, ptrn2 in ptrns.items():
            for d in range(4):
                valid = True
                x1, y1 = coordComb[d][0]
                x2, y2 = coordComb[d][1]
                coords = sharedCells(x1, y1, x2, y2)
                for cx, cy in coords:
                    px1, py1 = toPtrnCoord(x1, y1, cx, cy)
                    px2, py2 = toPtrnCoord(x2, y2, cx, cy)
                    if ptrn[py1][px1] != ptrn2[py2][px2]:
                        valid = False
                if valid:
                    relList[d].append(key2)
        relations.__setitem__(key, relList)

    # Apply ptrns to ptrnMap
    for y in range(height):
        ptrnMap.append([])
        for x in range(width):
            ptrnMap[-1].append([])
            for key in ptrns.keys():
                ptrnMap[-1][-1].append(key)


def collapse(x, y):
    if not collapsed[y][x]:
        collapsed[y][x] = True
        ri = rInList([count[key] for key in wave[y][x]])
        wave[y][x] = [wave[y][x][ri]]
        for cx, cy in [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]:
            if cx >= 0 and cy >= 0 and cx < width and cy < height:
                if not collapsed[cy][cx] and collapseNxt.count((cx, cy)) == 0:
                    collapseNxt.append((cx, cy))
        propogate(x, y)


def propogate(x, y):
    key = wave[y][x][0]
    relList = relations.get(key)
    coords = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]

    for d in range(4):
        cx, cy = coords[d]
        if cx >= 0 and cy >= 0 and cx < width and cy < height:
            remove = []
            for key2 in wave[cy][cx]:
                if relList[d].count(key2) == 0:
                    remove.append(key2)
            for key2 in remove:
                wave[cy][cx].remove(key2)


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


def run(att):
    att += 1
    setPtrns()
    setWave()
    try:
        while collapseNxt:
            cx, cy = collapseNxt.pop(0)
            # print('COLLAPSING',cx, ',', cy)
            if len(wave[cy][cx]) == 0:
                raise 'Contradiction'
            collapse(cx, cy)
            # print(len(out))
        print('ATTEMPT:', att)
        setOut()
        printMap(out)
    except IndexError:
        print('wtf')
    except:
        if att % 10 == 0:
            print('ATTEMPT:', att)
            setOut()
            printMap(out)
        run(att)


run(0)

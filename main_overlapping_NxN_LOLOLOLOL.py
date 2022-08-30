from copy import deepcopy
from math import floor, log2
from random import random
import string
from turtle import width

RULES = dict[tuple[int, int]: int]
# ex: rule[(1, 1)] = 3, where 3 could refer to the color red
IMAGE1 = [  # 1          2          3          4          5          6          7          8          9         10         11         12         13         14         15         16
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
IMAGE2 = [
    ['#FF0000', '#FF0000', '#FF0000', '#FF0000'],
    ['#FF0000', '#000000', '#00FF00', '#FF0000'],
    ['#FF0000', '#00FF00', '#000000', '#FF0000'],
    ['#FF0000', '#FF0000', '#FF0000', '#FF0000']
]
IMAGE3 = [
    ['#FF0000', '#000000']
]
SOURCE = IMAGE1


class PatternClass:

    def __init__(self, clr: int, rules: RULES):
        self.clr = clr
        self.count = 1
        self.rules = rules
        self.setID()
        self.valid = True

    def increment(self):
        self.count += 1

    def setID(self):
        tID = str(self.clr)
        for (x, y), val in self.rules.items():
            tID += '|%d,%d->%d' % (x, y, val)
        self.id = tID

    def equalsAndExec(self, pattern: 'PatternClass'):
        if self.equals(pattern):
            self.count += 1
            return True
        return False

    def equals(self, pattern: 'PatternClass'):
        return self.id == pattern.id

    def eliminate(self):
        self.valid = False

    def isValid(self, dx, dy, clr):
        return self.rules[(dx, dy)] == clr


class PatternCollection:
    def __init__(self, N):
        self.patterns: list[PatternClass] = []
        self.palette: dict[int, str] = {}
        self.N = N

    def addPattern(self, newPattern: PatternClass):
        for pattern in self.patterns:
            if pattern.equalsAndExec(newPattern):
                return
        self.patterns.append(newPattern)

    def color(self, inp: list[list[str]], x: int, y: int):
        clrStr = inp[y][x]
        clr = -1
        registered = False
        for clr2, clrStr2 in self.palette.items():
            if clrStr2 == clrStr:
                clr = clr2
                registered = True
                break

        if not registered:
            clr = len(self.palette) + 1
            self.palette.__setitem__(clr, clrStr)

        return clr

    def scanMap(self, inp: list[list[str]]):
        width = len(inp[0])
        height = len(inp)

        for y in range(height):
            for x in range(width):
                # Get patterns color and register it in the palette if it isn't already
                clr = self.color(inp, x, y)

                # Get pattern rules // corner and edge cells have wildcards
                rules: RULES = {}
                sCoords = MapClass(
                    width, height, self.N).surrounding(x, y, periodic=True)
                dCoords = MapClass(
                    width, height, self.N).surrounding(x, y, allowInvalid=True)
                for i in range(len(sCoords)):
                    sx, sy = sCoords[i]
                    dx, dy = dCoords[i]
                    rules.__setitem__((dx-x, dy-y), self.color(inp, sx, sy))

                # Initialize and register pattern
                pattern = PatternClass(clr, rules)
                self.addPattern(pattern)


class TileClass:

    def __init__(self, x: int, y: int, patterns: list[PatternClass] = []):
        self.x = x
        self.y = y
        self.patterns = deepcopy(patterns)

    def eliminateInvalid(self, dx: int, dy: int, clr: int):
        for pattern in self.patterns:
            if not pattern.isValid(dx, dy, clr):
                pattern.eliminate()

    def entropy(self):
        counts = [pattern.count for pattern in self.patterns if pattern.valid]
        tot = sum(counts)
        return float(-sum([(c/tot)*log2(c/tot) for c in counts]))

    def collapse(self):
        ids = [pattern.id for pattern in self.patterns if pattern.valid]
        counts = [pattern.count for pattern in self.patterns if pattern.valid]
        n = floor(sum(counts) * random())
        i = -1
        while n > 0:
            i += 1
            n -= counts[i]
        vID = ids[i]

        for pattern in self.patterns:
            if pattern.id != vID:
                pattern.eliminate()

    def diff(self, mapX: int, mapY: int):
        return mapX - self.x, mapY - self.y

    def validPatterns(self):
        return [pattern for pattern in self.patterns if pattern.valid]

    def onlyPattern(self):
        n = self.nValid()
        if n == 1:
            return self.validPatterns()[0]
        else:
            #     print("Tile is not collapsed with %d patterns" % n)
            return

    def nValid(self):
        s = 0
        for pattern in self.patterns:
            if pattern.valid:
                s += 1
        return s

    def color(self):
        n = self.nValid()
        if n == 1:
            return self.validPatterns()[0].clr
        else:
            # print("Tile is not collapsed with %d patterns" % n)
            return -1

    def validColors(self):
        n = self.nValid()
        if n > 0:
            return [vp.clr for vp in self.validPatterns()]
        else:
            # print("Tile is not collapsed with %d patterns" % n)
            return -1

    def validRuleColors(self, dx, dy):
        n = self.nValid()
        if n > 0:
            return [vp.rules[(dx, dy)] for vp in self.validPatterns()]
        else:
            # print("Tile is not collapsed with %d patterns" % n)
            return -1


class MapClass:

    def __init__(self, width: int, height: int, N: int, patterns: list[PatternClass] = [], palette: dict[int, str] = {0: ''}):
        self.result = 0  # 0: n/a 1: Success -1: Contradiction
        self.width = width
        self.height = height
        self.N = N
        self.pallete: dict[int: string] = palette
        self.wave: list[list[TileClass]] = [
            [TileClass(x, y, patterns) for x in range(width)] for y in range(height)
        ]
        self.propagated: list[list[bool]] = [
            [False for _ in range(width)] for _ in range(height)
        ]
        self.output: list[list[int]] = [
            [-1 for _ in range(width)] for _ in range(height)
        ]

    def collapseMostCertain(self):
        def ent(elem):
            return elem[2]
        eMap = self.entropyMap()
        flatEMap = [
            eMap[y][x] for x in range(self.width) for y in range(self.height)
            if ent(eMap[y][x]) != 0
        ]
        flatEMap.sort(key=ent)

        x, y, ent = flatEMap[0]
        print('ALLOWED CLRS')
        print([p.clr for p in self.tile(x, y).patterns])
        print('COLLAPSING CELL AT %d, %d:' % (x, y))
        self.tile(x, y).collapse()

    def tile(self, x: int, y: int):
        return self.wave[y][x]

    def surrounding(self, x: int, y: int, allowInvalid=False, periodic=False):
        yRange = range(y - self.N//2, y + self.N//2 + 1)
        xRange = range(x - self.N//2, x + self.N//2 + 1)
        if not periodic and not allowInvalid:
            return [
                (sx, sy)
                for sy in yRange
                for sx in xRange
                if
                (sx != x or
                 sy != y) and
                sx >= 0 and
                sy >= 0 and
                self.width > sx and
                self.height > sy
            ]
        elif not periodic:
            return [
                (sx, sy)
                for sy in yRange
                for sx in xRange
                if
                (sx != x or
                 sy != y)
            ]
        else:
            return [
                (sx % self.width, sy % self.height)
                for sy in yRange
                for sx in xRange
                if
                (sx != x or
                 sy != y)
            ]

    def shared(self, x1: int, y1: int, x2: int, y2: int):
        sCoords1 = self.surrounding(x1, y1)
        sCoords2 = self.surrounding(x2, y2)

        shCoords = [(shx, shy)for shx, shy in sCoords1
                    if sCoords2.count((shx, shy)) != 0]
        return shCoords

    def entropyMap(self):
        return [[(x, y, self.tile(x, y).entropy()) for x in range(self.width)] for y in range(self.height)]

    def isContradiction(self, x, y):
        contradiction = True
        for pattern in self.tile(x, y).patterns:
            if pattern.valid:
                contradiction = False
                break
        return contradiction

    def propagate(self):
        # only checking zero entropies // and only checking if pattern.clr matches rule
        def run(flatEMap: list[tuple[int, int, float]]):
            print('PROPAGATING')
            finished = True
            for x, y, ent in flatEMap:
                # Check if finihed
                if ent > 0:
                    finished = False
                    # continue
                # Check if element has lost all of its patterns
                if self.isContradiction(x, y):
                    return -1

                # Eliminate surrounding tiles unfitting patterns
                sCoordinates = self.surrounding(x, y)
                tile1 = self.tile(x, y)
                # pattern1 = tile1.onlyPattern()
                for sx, sy in sCoordinates:
                    tile2 = self.tile(sx, sy)
                    shCoords = map.shared(x, y, sx, sy)
                    for pattern2 in tile2.patterns:
                        dx1, dy1 = tile1.diff(sx, sy)
                        color1 = tile1.validRuleColors(dx1, dy1)
                        dx2, dy2 = tile2.diff(x, y)
                        color2 = pattern2.rules[(dx2, dy2)]
                        # Check if middle color of trgtPattern apllies to rule
                        if color1.count(pattern2.clr) == 0:
                            pattern2.eliminate()
                            continue

                        # Check if middle color of oPattern apllies to rule
                        if tile1.validColors().count(color2) == 0:
                            pattern2.eliminate()
                            continue

                        # Check if both patterns respective rules match
                        for shx, shy in shCoords:
                            dx1, dy1 = tile1.diff(shx, shy)
                            color1 = tile1.validRuleColors(dx1, dy1)
                            dx2, dy2 = tile2.diff(shx, shy)
                            color2 = pattern2.rules[(dx2, dy2)]

                            if color1.count(color2) == 0:
                                pattern2.eliminate()
                                break
                if tile1.nValid() <= 1:
                    self.propagated[y][x] = True
            if finished:
                return 1
            return 0
        eMap = self.entropyMap()
        flatEMap = [
            eMap[y][x] for x in range(self.width) for y in range(self.height) if not self.propagated[y][x]
        ]
        while len(flatEMap) > 0 and flatEMap[0][2] == 0:
            self.result = run(flatEMap)
            if self.result != 0:
                return
            eMap = self.entropyMap()
            flatEMap = [
                eMap[y][x] for x in range(self.width) for y in range(self.height) if not self.propagated[y][x]
            ]
            if len(flatEMap) == 0:
                self.result = 1
                return
        print('FLAT:', flatEMap)
        print(flatEMap and flatEMap[0][2] == 0)

    def toOut(self):
        for y in range(self.height):
            for x in range(self.width):
                self.output[y][x] = self.tile(x, y).color()

    def render(self):
        for row in self.output:
            for clr in row:
                print(clr, end='|')
            print('')


[print('---------------------------------------------------------------------')
 for _ in range(10)]
collection = PatternCollection(5)
collection.scanMap(SOURCE)
map = MapClass(8, 8, 5, collection.patterns, collection.palette)
while True:
    map.toOut()
    map.render()
    map.collapseMostCertain()
    map.propagate()
    print(map.propagated)
    print(map.result)
    if map.result != 0:
        break
print("Result is %d :)" % map.result)
map.toOut()
map.render()
print(collection.palette)

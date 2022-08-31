
from math import floor, log2
from random import random
from turtle import width
from typing import TypeVar

T = TypeVar('T')
PattternDict = dict[int, 'Pattern']
# Every pattern is associated with an unique integer a.k.a id
PatternCells = dict[tuple[int, int], int]
# 0, 0 is center while -1, -1 or -2, -2 etc is top left
Relations = tuple[list[int], list[int], list[int], list[int]]
# Tuple goes from top to right, bottom and left, integer refers to pattern id
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
    ['#FF0000', '#000000', '#FF0000', '#000000'],
    ['#FF0000', '#000000', '#FF0000', '#000000'],
]
SOURCE = IMAGE2


def contains(l: list[T], val: T):
    for elem in l:
        if elem == val:
            return True
    return False


class Pattern:
    def __init__(self, N: int):
        self.id = -1
        self.N = N
        self.rule: PatternCells = {}
        self.relations: Relations = ([], [], [], [])

    def render(self):
        minx = - (self.N // 2)
        maxx = + self.N // 2
        miny = - (self.N // 2)
        maxy = + self.N // 2
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                print('\033[%dm • \033[0m' % (40 + self.rule[(x, y)]), end='')
            print('')

        return self

    def fromImg(self, x: int, y: int, source: list[list[int]], periodic=True):
        minx = x - self.N // 2
        maxx = x + self.N // 2
        miny = y - self.N // 2
        maxy = y + self.N // 2
        width = len(source[0])
        height = len(source)

        for cy in range(miny, maxy + 1):
            for cx in range(minx, maxx + 1):
                if periodic or (x >= 0 and y >= 0 and x < width and y < height):
                    self.rule[(cx - x, cy - y)] = source[cy %
                                                         height][cx % width]

        return self

    def similar(self, pattern2: 'Pattern'):
        minx = - (self.N // 2)
        maxx = + self.N // 2
        miny = - (self.N // 2)
        maxy = + self.N // 2
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                if self.rule[(x, y)] != pattern2.rule[(x, y)]:
                    return False
        return True

    def setID(self, id):
        self.id = id
        return self

    def relation(self, pattern2: 'Pattern'):
        directionPos = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        cell1 = Cell(0, 0, self.N)
        for d in range(4):
            x2, y2 = directionPos[d]
            cell2 = Cell(x2, y2, self.N)
            shCoords = cell1.shared(cell2)
            related = True
            for shx, shy in shCoords:
                rCoord1 = cell1.relative(shx, shy)
                rCoord2 = cell2.relative(shx, shy)
                if self.rule[rCoord1] != pattern2.rule[rCoord2]:
                    related = False
            if related:
                self.relations[d].append(pattern2.id)

        return self


class Cell:
    patternIDs: list[int]  # valid pattern ids
    pWeights: dict[int, int]

    def __init__(self, x: int, y: int, N: int):
        self.x = x
        self.y = y
        self.N = N
        self.pWeights = {}
        self.patternIDs = []
        self.propogated = False

    def populate(self, patterns: dict[int, Pattern], pWeights: dict[int, int]):
        self.patternIDs = list(patterns.keys())
        self.patterns = patterns
        self.pWeights = pWeights

        return self

    def collapse(self):
        probs = [self.pWeights[pID] for pID in self.patternIDs]
        tot = sum(probs)
        n = floor(tot * random())
        i = -1
        while n > 0:
            i += 1
            n -= probs[i]
        pID = self.patternIDs[i]
        for rpID in self.patternIDs.copy():
            if rpID != pID:
                self.removeID(rpID)

        # print(self.patterns[pID].relations)

        return self

    def entropy(self):
        probs = [self.pWeights[pID] for pID in self.patternIDs]
        tot = sum(probs)
        return sum([-(p/tot)*log2(p/tot) for p in probs])

    def propogate(self, cells: dict[tuple[int, int]: 'Cell']):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        for dx, dy in directions:
            cx, cy = self.x + dx, self.y + dy
            cell2 = cells.get((cx, cy), Cell(-1, -1, -1))
            self.updRelations(cell2)
        self.propogated = True
        return self

    def updRelations(self, cell2: 'Cell'):
        rx, ry = self.relative(cell2.x, cell2.y)
        d = -1
        match (rx, ry):
            case (0, -1):
                d = 0
            case (1, 0):
                d = 1
            case (0, 1):
                d = 2
            case (-1, 0):
                d = 3

        remove = []
        for patternID2 in cell2.patternIDs:
            valid = False
            for patternID1 in self.patternIDs:
                pattern1 = self.patterns[patternID1]
                for patternRelID1 in pattern1.relations[d]:
                    if patternRelID1 == patternID2:
                        valid = True
                        break
                if valid:
                    break
            if not valid:
                remove.append(patternID2)
        for patternID2 in remove:
            cell2.removeID(patternID2)
        return self

    def removeID(self, id: int):
        self.patternIDs.remove(id)
        return self

    def surround(self):
        minx = self.x - self.N // 2
        maxx = self.x + self.N // 2
        miny = self.y - self.N // 2
        maxy = self.y + self.N // 2
        return [(sx, sy) for sy in range(miny, maxy + 1) for sx in range(minx, maxx + 1)]

    def shared(self, cell2: 'Cell'):
        sCoords1 = self.surround()
        sCoords2 = cell2.surround()

        return [sCoord for sCoord in sCoords1 if contains(sCoords2, sCoord)]

    def relative(self, x: int, y: int):
        return x - self.x, y - self.y

    def isDummy(self):
        return self.x == -1 and self.y == -1 and self.N == -1

    def isCorrupt(self):
        return len(self.patternIDs) == 0


class Map:
    class Contradiction(Exception):
        def __init__(self, attempt: int, message: str = "Contradiction occured"):
            self.attempt = attempt
            self.message = message
            super().__init__(self.message)

        def __str__(self):
            return 'Attempt %d -- %s' % (self.attempt, self.message)

    palette: dict[int, str]
    source: list[list[int]]
    patterns: PattternDict
    pWeights: dict[int, int]
    cells: dict[tuple[int, int], Cell]

    def __init__(self, N, width=-1, height=-1):
        self.N = N
        self.width = width
        self.height = height
        self.cells = {}

    def scanImg(self, source: list[list[str]]):
        self.palette: dict[int, str] = {}
        self.source: list[list[int]] = []

        for row in source:
            self.source.append([])
            for cell in row:
                clrKey = -1
                nKeys = 0
                for key, strClr in self.palette.items():
                    nKeys += 1
                    if strClr == cell:
                        clrKey = key

                if clrKey != -1:
                    self.source[-1].append(clrKey)
                else:
                    clrKey = nKeys + 1
                    self.palette[clrKey] = cell
                    self.source[-1].append(clrKey)

        return self

    def extractPatterns(self):
        self.patterns = {}
        self.pWeights = {}
        width = len(self.source[0])
        height = len(self.source)

        # Get all patterns
        for y in range(height):
            for x in range(width):
                pattern = Pattern(3).fromImg(x, y, self.source)
                pKey = -1
                nKeys = 0
                for key, recPattern in self.patterns.items():
                    nKeys += 1
                    if pattern.similar(recPattern):
                        pKey = key

                if pKey == -1:
                    pKey = nKeys + 1
                    pattern.setID(pKey)
                    self.patterns[pKey] = pattern
                self.pWeights[pKey] = self.pWeights.get(pKey, 0) + 1

        # Relate Patterns
        for pattern1 in self.patterns.values():
            for pattern2 in self.patterns.values():
                pattern1.relation(pattern2)

        return self

    def populate(self):
        self.cells = {}
        for y in range(self.height):
            for x in range(self.width):
                self.cells[(x, y)] = Cell(x, y, self.N)
        for cell in self.cells.values():
            cell.populate(self.patterns, self.pWeights)
        return self

    def lowestEntropy(self):
        le = -1
        lc = Cell(-1, -1, -1)

        for cell in self.cells.values():
            ent = cell.entropy()
            # print(le, lc.x, lc.y, '|||', ent, cell.x, cell.y, '|||',
            #   not cell.propogated and (le == -1 or ent < le))
            if not cell.propogated and (le == -1 or ent < le):
                le = ent
                lc = cell

        return lc

    def renderSrc(self):

        for row in self.source:
            for cell in row:
                print('\033[%dm • \033[0m' % (40 + cell), end='')
            print('')

    def renderClr(self):
        cellMap = [[-1for __x__ in range(self.width)]
                   for __y__ in range(self.height)]
        for cell in self.cells.values():
            if len(cell.patternIDs) == 1:
                cellMap[cell.y][cell.x] = cell.patternIDs[0]

        for row in cellMap:
            for cell in row:
                print('\033[%dm • \033[0m' %
                      (40 + self.patterns[cell].rule[(0, 0)]), end='')
            print('')

    def renderIDs(self):
        cellMap = [['¤¤U¤¤' for __x__ in range(self.width)]
                   for __y__ in range(self.height)]
        for cell in self.cells.values():
            if len(cell.patternIDs) == 1:
                cellMap[cell.y][cell.x] = cell.patternIDs[0]
            else:
                cellMap[cell.y][cell.x] = 'l' + str(len(cell.patternIDs))

        for row in cellMap:
            for cell in row:
                print(str(cell).ljust(3, ' ').rjust(5, ' '), end='')
            print('')

        return self

    def reset(self):
        self.populate()
        return self

    def solve(self):
        solved = False
        attempt = 1
        while not solved:
            try:
                cell = self.lowestEntropy()
                while not cell.isDummy():
                    if cell.isCorrupt():
                        raise self.Contradiction(attempt)
                    cell.collapse().propogate(self.cells)
                    cell = self.lowestEntropy()
                solved = True
            except self.Contradiction:
                print('Contradiction -- Attempt:', attempt)
                self.reset()
                attempt += 1

        return self


map = Map(3, 32, 32).scanImg(SOURCE).extractPatterns().populate().solve()
map.renderSrc()
map.renderIDs()
map.renderClr()
print('done')

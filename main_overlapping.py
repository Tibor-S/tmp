
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
SOURCE = IMAGE1


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

    def populate(self, patterns: dict[int, Pattern], pWeights: dict[int, int]):
        self.patternIDs = list(patterns.keys())
        self.patterns = patterns
        self.pWeights = pWeights

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
            print(patternID2)
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
        print('remove')
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


class Map:
    palette: dict[int, str]
    source: list[list[int]]
    patterns: PattternDict
    pWeights: dict[int, int]

    def __init__(self, N):
        self.N = N

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

                if pKey != -1:
                    self.pWeights[pKey] = self.pWeights.get(pKey, 0) + 1
                else:
                    pKey = nKeys + 1
                    pattern.setID(pKey)
                    self.patterns[pKey] = pattern

        # Relate Patterns
        for pattern1 in self.patterns.values():
            for pattern2 in self.patterns.values():
                pattern1.relation(pattern2)

        return self


# for y in range(len(SOURCE)):
#     for x in range(len(SOURCE[0])):
#         Pattern(3).fromImg(x, y, Map(3, SOURCE).source).render()
map = Map(3).scanImg(SOURCE).extractPatterns()

cell1 = Cell(0, 0, 3).populate(map.patterns, map.pWeights)
cell2 = Cell(1, 0, 3).populate(map.patterns, map.pWeights)

cell1.patternIDs = [1]
cell1.updRelations(cell2)
print(cell1.patterns[1].relations)
print(cell2.patternIDs)

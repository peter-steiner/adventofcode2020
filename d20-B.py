#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/20
"""

# Imports
import sys
import os
import re
import math
import time

# Global variables
task="d20"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data


class Tile:
    def __init__(self, tileId, camarr):
        self.id = tileId
        self.camarr = camarr[:]
        self.borders = [""]*4
        self.rotateClock()
        self.rotateAntiClock()

    def flip(self):
        self.camarr = self.camarr[::-1]
        self.rotateClock()
        self.rotateAntiClock()

    def rotateClock(self):
        self.borders[1] = "".join(self.camarr[0])
        self.borders[3] = "".join(self.camarr[-1])
        self.camarr = list(zip(*self.camarr[::-1]))
        self.borders[0] = "".join(self.camarr[0])
        self.borders[2] = "".join(self.camarr[-1])

    def rotateAntiClock(self):
        self.borders[3] = "".join(self.camarr[0][::-1])
        self.borders[1] = "".join(self.camarr[-1][::-1])
        self.camarr = list(zip(*self.camarr))[::-1]
        self.borders[0] = "".join(self.camarr[0])
        self.borders[2] = "".join(self.camarr[-1])

    def p(self):
        tmp = ""
        for r in self.camarr:
            tmp += "".join(r) + "\n"
        print("Id: {} \n{}".format(self.id, tmp))

def popTile(tiles, t):
    tilesTmp = []
    for i in range(len(tiles)):
        if tiles[i].id != t.id:
            tilesTmp.append(tiles[i])
    return tilesTmp

def printMatrix(matrix, side):
    rows = [""]*side 
    for i in range(side):
        for k in range(side):
            #print(i, k)
            if matrix[i][k] == None:
                rows[i] += "xxxx" + " : "                
            else:
                rows[i] += str(matrix[i][k].id) + " : "
    print("----------------")
    for r in rows:
        print("M", r)
    
mutations = []
maxid = 0
tileLength = 0


def strippAndLookForMonsters(tilesMutated, mut, side):
    global maxId
    global tileLength

    tilesStrippedMutated = [None]*(maxId+1)
    tiles = []
    for t in tilesMutated:
        if t != None:
            tiles.append(t)
    tm = []
    #print(tiles)
    tileMut = None
    for tile in tiles:
        arrMut = tile.camarr[1:tileLength-1]
        for i in range(len(arrMut)):
            arrMut[i] = arrMut[i][1:tileLength-1]
        tileMut = Tile(tile.id, arrMut)
        tilesStrippedMutated[tile.id] = tileMut
        tm.append(tileMut)

    tileMutLength = len(tm[-1].camarr[0])
    tmp = []
    for m in mut:
        #print(m)
        tmp.append(tilesStrippedMutated[m])

    #Build big ass array
    mutAsArr = []
    max = 0
    refString = ""
    # Tiles GROUP row
    for n in range(side):
        nPrim = math.floor(n/3)
        # Tile row
        for y in range(len(tm[0].camarr)):
            # Tiles col
            rowArr = []
            rowStr = ""
            for x in range(side):
                #print(side*n + x, y)
                rowArr += tmp[side*n +x].camarr[y]
                rowStr += "".join(tmp[side*n + x].camarr[y])
            mutAsArr.append(rowArr)
            refString += rowStr + "\n"

    if mut[0] == 1951 and mut[8] == 1171:
        print("1337\n", refString)

    #Rotate and flip
    for i in range(1, 9):
        sum = 0
        # TEST CONTENT FOR SEAMONSTERS
        for k in range(0, side*tileMutLength-3):    
            tmpStr = ""
            for n in range(3):
                tmpStr += "".join(mutAsArr[k+n])
            #print("-------")
            sum += findSeaMonster(tmpStr, tileMutLength*side, mut[0])
            # Test for seamonster
        if i == 4:
            # FLIP
            mutAsArr = mutAsArr[::-1]
        else:
            # ROTATE
            mutAsArr = list(zip(*mutAsArr[::-1]))
        if sum > max:
            max = sum
            countHashes = refString.count("#")
            print("Found monsters", max, mut, countHashes, countHashes-max*15)

    return

def buildImage(matrix, tiles, tilesMutated, x, y, side, depth, path, borders):
    global mutations

    if depth > side*side:
        mutations.append([n for n in path[:-1].split(":")])
#        print("Prosess", mutations[-1][0], mutations[-1])
        strippAndLookForMonsters(tilesMutated, [int(n) for n in path[:-1].split(":")], side)
        return

    if x > 0 and x%side == 0:
        y += 1
        x = 0

    upperStr = ""
    leftStr = ""
    if y > 0:
        upperStr = matrix[y-1][x].borders[2]
    if x > 0:
        leftStr = matrix[y][x-1].borders[1]

    #1 corner
    for t in tiles:
        if not str(t.id) in path:
            for i in range(1, 9):
                #tTMP = Tile(t.id, t.camarr)
                tilesMutated[t.id] = t
                if x == 0 and y == 0:
                    matrix[y][x] = t

                    tilesTmp = popTile(tiles, t)
                    bordStr = borders + "|" + "NONE" + ":" + t.borders[1] + "*" + t.borders[1]
                    buildImage(matrix, tilesTmp, tilesMutated, x+1, y, side, depth+1, path + str(t.id) + ":", bordStr)                   
                    matrix[y][x] = None
                if x == 0 and y > 0:
                    # TEST surrounding LEFT & UP
                    if upperStr == t.borders[0]:
                        #Match
                        matrix[y][x] = t
                        tilesTmp = popTile(tiles, t)
                        bordStr = borders + "|" + upperStr + ":" + t.borders[0]
                        buildImage(matrix, tilesTmp, tilesMutated, x+1, y, side, depth+1, path + str(t.id) + ":", bordStr)
                        matrix[y][x] = None
                if x > 0 and y > 0:
                    # TEST surrounding LEFT & UP
                    if leftStr == t.borders[3] and upperStr == t.borders[0]:
                        #Match
                        matrix[y][x] = t
                        tilesTmp = popTile(tiles, t)
                        bordStr = borders + "|" + leftStr + ":" + t.borders[3] + "&" + upperStr + ":" + t.borders[0]
                        buildImage(matrix, tilesTmp, tilesMutated, x+1, y, side, depth+1, path + str(t.id) + ":", bordStr)
                        matrix[y][x] = None
                if y == 0 and x > 0:
                    #test left  only
                    if leftStr == t.borders[3]:
                        #Match
                        matrix[y][x] = t
                        tilesTmp = popTile(tiles, t)
                        bordStr = borders + "|" + leftStr + ":" + t.borders[3]
                        buildImage(matrix, tilesTmp, tilesMutated, x+1, y, side, depth+1, path + str(t.id) + ":", bordStr)
                        matrix[y][x] = None
                if i == 4:
                    t.flip()
                else:
                    t.rotateClock()

"""
.####...#####..#...###..
"""

"""
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
"""
.#.#...#.###...#.##.O#..#.O.##.OO#.#.OO.##.OOO##..#O.#O#.O##O..O.#O##.##
"""


def findSeaMonster(tmpStr, rowLength, id):
    found = 0
    sea = list(tmpStr)
    ref1 = rowLength - 18
    ref2 = rowLength - 18
    lastSpot = 0
    points = [ref1, 5, 1, 5, 1, 5, 1, 1]
    #print()
    for n in range(0, len(sea)-63):
        # Phase
        hits = 0
        lastSpot = 0
        if sea[n+17] == "#":
            lastSpot = n+17 
            hits += 1
        for p in points:
            if (lastSpot + p) < len(sea) and sea[lastSpot + p] == "#":
                lastSpot = lastSpot+p
                hits += 1
        lastSpot += ref2
        for i in range(6):
            if lastSpot + i*3 < len(sea) and sea[lastSpot + i*3] == "#":
                hits += 1
        if hits == 15:
            print("Found at ", n, id)
            found += 1
    return found

def a():
    rows = [n for n in readInput().split('\n')]
    tiles = []

    global mutations
    global maxId
    global tileLength

    maxId = 0
    tileId = 0
    for i in range(len(rows)):
        row = rows[i]
        if "Tile" in row:
            tileId = int(row.split("Tile ")[1].split(":")[0])
            if tileId > maxId:
                maxId = tileId
            tileMatr = []
            for n in range(i+1, i+11):
                tileRow = []
                tileRow[:0] = rows[n]
                tileMatr.append(tileRow)
            tile = Tile(tileId, tileMatr)
            tiles.append(tile)
    tileLength = len(tiles[-1].camarr[0])
    side = int(math.sqrt(len(tiles)))
    image = []
    for a in range(side):
        image.append([None]*side)

    tilesMutated = [None]*(maxId+1)
    printMatrix(image, side)
    #print(side, tiles)
    buildImage(image, tiles, tilesMutated, 0, 0, side, 1, "", "")

    ###############################################
    #mutations = ['1951', '2311', '3079', '2729', '1427', '2473', '2971', '1489', '1171']
def b():
    print("ABCD")
    tiles = []
    tmpId = 1
    side = 3
    tmp = [ ["1", "2", "3", "4"], ["5", "6", "7", "8"], ["9", "10", "11", "12"], ["13", "14", "15", "16"]]
    tiles.append(Tile(tmpId, tmp))

    tileMut = None
    for tile in tiles:
        arrMut = tile.camarr[1:side]
        for i in range(len(arrMut)):
            arrMut[i] = arrMut[i][1:side]
        print(tile.id, arrMut)
        tileMut = Tile(tile.id, arrMut)
    
    tileMut.p()

    print("Test rotation")
    tiles[0].p()
    print("1")
    tiles[0].rotateAntiClock()
    tiles[0].p()
    print(tiles[0].borders)
    print("2")
    tiles[0].rotateAntiClock()
    tiles[0].p()
    print("3")
    tiles[0].rotateAntiClock()
    tiles[0].p()
    print("4")
    tiles[0].rotateAntiClock()
    tiles[0].p()

    print("###############################")
    tiles[0].p()
    print("1")
    tiles[0].rotateClock()
    tiles[0].p()
    print(tiles[0].borders)
    print("2")
    tiles[0].rotateClock()
    tiles[0].p()
    print(tiles[0].borders)
    print("3")
    tiles[0].rotateClock()
    tiles[0].p()
    print(tiles[0].borders)
    print("4")
    tiles[0].rotateClock()
    tiles[0].p()
    print(tiles[0].borders)
    res = 0
    print("B): ", res)

def c():

    s = ".#.#...#.###...#.##.O#..#.O.##.OO#.#.OO.##.OOO##..#O.#O#.O##O..O.#O##.##"
    s = "#.###...#.##...#.##O###..O##.#OO.###OO##..OOO##...O#.O..O..O.#O##O##.###"
    print(len(s), "-----\n")
    for i in range(len(s)):
        if s[i] == "O":
            print(i)
    s = ".#.#...#.###...#.##.##..#.#.##.###.#.##.##.#####..##.###.####..#.####.##"
    s = "#.###...#.##...#.######..###.###.#######..#####...##.#..#..#.#######.###"
    print(findSeaMonster(s, 24, 1))

# Main body
if __name__ == '__main__':
    start = time.time()

    a()
    end = time.time()
    exectime = end - start
    print("Executed A in: {}".format(exectime))

#    b()
    """
    end = time.time()
    exectime = end - start
    print("Executed B in: {}".format(exectime))
    """
    
    end = time.time()
    exectime = end - start
    print("Executed in: {}".format(exectime))
    sys.exit(1)

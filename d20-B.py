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
task="d20-t"
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

def buildImage(matrix, tiles, x, y, side, depth, path, borders):
    global mutations

    if depth > side*side:
        lu = matrix[0][0].id
        lb = matrix[side-1][0].id
        ru = matrix[0][side-1].id
        rb = matrix[side-1][side-1].id
#        print("END", path)
#        print("END Corners: ", lu, lb, ru, rb, lu*lb*rb*ru) 
#        print("END", borders)
#        printMatrix(matrix, side)
        mutations.append([n for n in path[:-1].split(":")])
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
                if x == 0 and y == 0:
                    matrix[y][x] = t
                    tilesTmp = popTile(tiles, t)
                    bordStr = borders + "|" + "NONE" + ":" + t.borders[1] + "*" + t.borders[1]
                    buildImage(matrix, tilesTmp, x+1, y, side, depth+1, path + str(t.id) + ":", bordStr)                   
                    matrix[y][x] = None
                if x == 0 and y > 0:
                    # TEST surrounding LEFT & UP
                    if upperStr == t.borders[0]:
                        #Match
                        matrix[y][x] = t
                        tilesTmp = popTile(tiles, t)
                        bordStr = borders + "|" + upperStr + ":" + t.borders[0]
                        buildImage(matrix, tilesTmp, x+1, y, side, depth+1, path + str(t.id) + ":", bordStr)
                        matrix[y][x] = None
                if x > 0 and y > 0:
                    # TEST surrounding LEFT & UP
                    if leftStr == t.borders[3] and upperStr == t.borders[0]:
                        #Match
                        matrix[y][x] = t
                        tilesTmp = popTile(tiles, t)
                        bordStr = borders + "|" + leftStr + ":" + t.borders[3] + "&" + upperStr + ":" + t.borders[0]
                        buildImage(matrix, tilesTmp, x+1, y, side, depth+1, path + str(t.id) + ":", bordStr)
                        matrix[y][x] = None
                if y == 0 and x > 0:
                    #test left  only
                    if leftStr == t.borders[3]:
                        #Match
                        matrix[y][x] = t
                        tilesTmp = popTile(tiles, t)
                        bordStr = borders + "|" + leftStr + ":" + t.borders[3]
                        buildImage(matrix, tilesTmp, x+1, y, side, depth+1, path + str(t.id) + ":", bordStr)
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
    #print("MEH", range(0, len(sea)-57))
    ref1 = rowLength - 18
    ref2 = rowLength - 18
    lastSpot = 0
    points = [ref1, 5, 1, 5, 1, 5, 1, 1]
    for n in range(0, len(sea)-63):
        # Phase
        #print("!", n)
        hits = 0
        lastSpot = 0
        if sea[n+17] == "#":
            lastSpot = n+17 
            hits += 1
        for p in points:
            if sea[lastSpot + p] == "#":
                lastSpot = lastSpot+p
                hits += 1
        lastSpot += ref2
        for i in range(6):
            #print(lastSpot + i*3)
            if sea[lastSpot + i*3] == "#":
                hits += 1
        if hits == 15:
            print("Found at ", n, id)
            found += 1
    return found

def a():
    rows = [n for n in readInput().split('\n')]
    tiles = []
    global mutations
    tileId = 0
    maxId = 0
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

    side = int(math.sqrt(len(tiles)))
    image = []
    for a in range(side):
        image.append([None]*side)


    printMatrix(image, side)
    buildImage(image, tiles, 0, 0, side, 1, "", "")

    for mut in mutations:
        print(mut)

    tiles[0].p()
    tileLength = len(tiles[-1].camarr[0])

    print(tileLength)
    tilesMutated = [None]*(maxId+1)
    tm = []
    tileMut = None
    for tile in tiles:
        arrMut = tile.camarr[1:tileLength-1]
        for i in range(len(arrMut)):
            arrMut[i] = arrMut[i][1:tileLength-1]
        tileMut = Tile(tile.id, arrMut)
        tilesMutated[tile.id] = tileMut
        tm.append(tileMut)

    tileLength = len(tm[-1].camarr[0])
    tilesMutated[2311].p()
    """
    print(len(tm[0].camarr))
    print(tm[0].camarr)
    print(len(tm[0].camarr[0]))
    """
    max = 0
    #mutations = ['1951', '2311', '3079', '2729', '1427', '2473', '2971', '1489', '1171']
    for mut in mutations:
        tmp = []
        for m in mut:
            #print(m)
            tmp.append(tilesMutated[int(m)])

        #Build big ass array
        mutAsArr = []
        bajs = ""
        for k in range(0, int(len(mut)/side)):    
            for n in range(tileLength):
                mutAsArr.append(tmp[k].camarr[n] + tmp[k+1].camarr[n]+ tmp[k+2].camarr[n])
                bajs += "".join(tmp[k].camarr[n] + tmp[k+1].camarr[n]+ tmp[k+2].camarr[n]) + "\n"
        if mut[0] == "1951":
            print("b")
            print(bajs)
        #if mut[0] == "1951":
            #print(mutAsArr, len(mutAsArr))
        #Rotate and flip
        for i in range(1, 9):
            #print("-------------------\n", mut[0])
            sum = 0
            # TEST CONTENT FOR SEAMONSTERS
            for k in range(0, side*tileLength-3):    
                tmpStr = ""
                for n in range(3):
                    tmpStr += "".join(mutAsArr[k+n])
                #print("-------")
                if tmpStr == ".#.#...#.###...#.##.##..#.#.##.###.#.##.##.#####..##.###.####..#.####.##":
                    print("AW111", mut[0])
                if tmpStr == "#.###...#.##...#.######..###.###.#######..#####...##.#..#..#.#######.###":
                    print("AW222", mut[0])
                #print(tmpStr)
                sum += findSeaMonster(tmpStr, tileLength*side, mut[0])
                # Test for seamonster
            if i == 4:
                # FLIP
                mutAsArr = mutAsArr[::-1]
            else:
                # ROTATE
                mutAsArr = list(zip(*mutAsArr[::-1]))
            if sum > max:
                max = sum
                print("Found monsters", max, mut)

def b():
#    rows = [int(n) for n in readInput().split('\n')]
#   res = 0
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
...####.#.####.##.###...

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



"""

for k in range(0, side*tileLength-3):    
                tmpStr = ""
                for n in range(3):
                    # Row n + (n + 1) + (n +2)
                    y = math.floor((k+n)/tileLength)
                    for s in range(side):
                        #Col 1,2,3
                        sp = 3 * y
                        #print(k, sp+s, (k+n%8))
                        tmpStr += "".join(tmp[sp + s].camarr[(k+n)%8])
                #print("-------")
                #print(tmpStr)
                sum += findSeaMonster(tmpStr, tileLength*side)
                # Test for seamonster
"""
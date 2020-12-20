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
        self.matched = False
        self.rotateClock
        self.rotateAntiClock

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

def buildImage(matrix, tiles, x, y, side, depth, path):

    if depth > side*side:
        lu = matrix[0][0].id
        lb = matrix[side-1][0].id
        ru = matrix[0][side-1].id
        rb = matrix[side-1][side-1].id
        print("END", path)
        print("END Corners: ", lu, lb, ru, rb, lu*lb*rb*ru) 
        printMatrix(matrix, side)
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
                    buildImage(matrix, tilesTmp, x+1, y, side, depth+1, path + str(t.id) + ":")                   
                    matrix[y][x] = None
                if x == 0 and y > 0:
                    # TEST surrounding LEFT & UP
                    if upperStr == t.borders[0]:
                        #Match
                        matrix[y][x] = t
                        tilesTmp = popTile(tiles, t)
                        buildImage(matrix, tilesTmp, x+1, y, side, depth+1, path + str(t.id) + ":")
                        matrix[y][x] = None
                if x > 0 and y > 0:
                    # TEST surrounding LEFT & UP
                    if leftStr == t.borders[3] and upperStr == t.borders[0]:
                        #Match
                        matrix[y][x] = t
                        tilesTmp = popTile(tiles, t)
                        buildImage(matrix, tilesTmp, x+1, y, side, depth+1, path + str(t.id) + ":")
                        matrix[y][x] = None
                if y == 0 and x > 0:
                    #test left  only
                    if leftStr == t.borders[3]:
                        #Match
                        matrix[y][x] = t
                        tilesTmp = popTile(tiles, t)
                        buildImage(matrix, tilesTmp, x+1, y, side, depth+1, path + str(t.id) + ":")
                        matrix[y][x] = None
                if i == 4:
                    t.flip()
                else:
                    t.rotateClock()

def a():
    rows = [n for n in readInput().split('\n')]
    tiles = []

    tileId = 0
    for i in range(len(rows)):
        row = rows[i]
        if "Tile" in row:
            tileId = int(row.split("Tile ")[1].split(":")[0])
            tileMatr = []
            for n in range(i+1, i+11):
                tileRow = []
                tileRow[:0] = rows[n]
                tileMatr.append(tileRow)
            tile = Tile(tileId, tileMatr)
            tiles.append(tile)

    sides = int(math.sqrt(len(tiles)))
    image = []
    for a in range(sides):
        image.append([None]*sides)

    printMatrix(image, sides)
    buildImage(image, tiles, 0, 0, sides, 1, "")


def b():
#    rows = [int(n) for n in readInput().split('\n')]
#   res = 0
    tiles = []
    tmpId = 1
    tmp = [ ["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"] ]
    tiles.append(Tile(tmpId, tmp))

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

# Main body
if __name__ == '__main__':
    start = time.time()

    a()
    end = time.time()
    exectime = end - start
    print("Executed A in: {}".format(exectime))

    #b()
    """
    end = time.time()
    exectime = end - start
    print("Executed B in: {}".format(exectime))
    """
    
    end = time.time()
    exectime = end - start
    print("Executed in: {}".format(exectime))
    sys.exit(1)

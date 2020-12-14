#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/14
"""

# Imports
import sys
import os
import re
import math

# Global variables
task="d14"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

mask = list(range(36))

class Mem():
    def __init__(self, id):
        self.id = id
        self.mem = format(0, '036b')
    def mask(self, mask):
        tmpMem = list(self.mem)
        for m in range(len(mask)):
            if mask[m] != "X":
                tmpMem[m] = mask[m]
        self.mem = "".join(tmpMem)

    def getIntValue(self):
        return int(self.mem, 2)

    def addInt(self, val):
#        self.mem = format(int(self.mem, 2) + val, '036b')
        self.mem = format(val, '036b')
    
    def p(self):
        print(self.mem, self.getIntValue())

def a():
    rows = [n for n in readInput().split('\n')]

    global mask
    maxMem = 0
    #Init bank
    for r in rows:
        if "mem" in (r):
            mem, val = r.split(" = ")
            mem = re.findall('\d+', mem)[0]
            mem = int(mem)
            if mem > maxMem: 
                maxMem = mem

    bank = [-1] * (maxMem+1)
    print(len(mask), maxMem)
    for r in rows:
        if "mask" in (r):
            mask = list(r.split(" = ")[1])
            print(r)
        else: 
            mem, val = r.split(" = ")
            mem = re.findall('\d+', mem)[0]
            val = int(val)
            mem = int(mem)

            if bank[mem] != -1:
                m = bank[mem]
                m.addInt(val)
                m.mask(mask)
            else: 
                print("Create for ", mem)
                m = Mem(mem)
                m.addInt(val)
                m.mask(mask)
                bank[mem] = m
            bank[mem].p()

    print("--------------------")

    sum = 0
    for b in range(len(bank)):
        if bank[b] != -1:
            #bank[b].p()
            sum += bank[b].getIntValue()

    print("A): ", sum)


def b():
    rows = [int(n) for n in readInput().split('\n')]
    res = 0

    print("B): ", res)

# Main body
if __name__ == '__main__':
    a()
#    b()
    sys.exit(1)

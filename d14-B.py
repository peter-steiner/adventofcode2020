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
import time

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
    def __init__(self, id, val):
        self.id = id
        self.val = val
        self.mem = format(0, '036b')
    def mask(self, mask):
        tmpMem = list(self.mem)
        for m in range(len(mask)):
            maskVal = mask[m]            
            if maskVal == "X" or maskVal == "1":
                tmpMem[m] = mask[m]            
        self.mem = "".join(tmpMem)

    def getIntValue(self):
        return int(self.mem, 2)

    def setInt(self, val):
        self.mem = format(val, '036b')
    
    def p(self):
        print(self.mem)

def getMemBanks(mem, val, memBanks):

    if mem.count("X") == 0:
        memBanks.append("".join(mem))
        return
    floatIndex = mem.index("X")
    memCpy = list(mem)
    memCpy[floatIndex] = val
    memCpy = "".join(memCpy)
    getMemBanks(memCpy, "0", memBanks)
    getMemBanks(memCpy, "1", memBanks)

def b():
    rows = [n for n in readInput().split('\n')]
    global mask
    bank = []
    for r in rows:
        if "mask" in (r):
            mask = list(r.split(" = ")[1])
        else: 
            mem, val = r.split(" = ")
            mem = re.findall('\d+', mem)[0]
            # val = mem
            val = int(val)
            mem = int(mem)
            # Calculate adresses
            floating = Mem(mem, 0)
            floating.setInt(mem)
            floating.mask(mask)

            memBanks = []
            getMemBanks(floating.mem, "0", memBanks)
            getMemBanks(floating.mem, "1", memBanks)
            memBanks = list(set(memBanks))

            # Set values
            for mb in memBanks:
                memId = int(mb, 2)
                bank.append(Mem(memId, val))

    print("--------------------")

    sum = 0
    done = []
    for b in reversed(bank):
        #print(b.id, b.val)
        if b.id not in done:
            sum += b.val
            done.append(b.id)

    print("B): ", sum)



# Main body
if __name__ == '__main__':
    start = time.time()
    b()

    end = time.time()
    exectime = end - start
    print("Executed in: {}".format(exectime))
    sys.exit(1)

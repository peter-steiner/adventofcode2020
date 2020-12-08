#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/8
"""

# Imports
import sys
import os
import re
import math

# Global variables
task="d8"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def exec(program, pos, amplVal):
    op, acc = program[pos].split(" ")
    if "nop" == op:
        return [pos+1, amplVal]
    if "acc" == op:
        amplVal += int(acc)
        return [pos+1, amplVal]
    if "jmp" == op:
        pos += int(acc)
        return [pos, amplVal]

    return [pos, amplVal]

def a():
    program = [n for n in readInput().split('\n')]
    max = 400
    res = 0
    amplVal = 0
    it = 0
    pos = 0
    paths = []
    
    while it < max:
        prePos = pos
        preAmplVal = amplVal
        #print("Move: ", preAmplVal, preAmplVal) 
        pos, amplVal = exec(program, pos, amplVal)
        key = program[prePos] + " " + program[pos]
        #print("Move: ", key, preAmplVal, amplVal) 
        if "jmp" in key and key in paths:
            print("Found loop: ", key, preAmplVal, it) 
            res = preAmplVal
            break
        paths.append(key)
        it +=1

    print("A): ", res, it)

# Main body
if __name__ == '__main__':
    a()
    sys.exit(1)

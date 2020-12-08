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

def b():
    program = [n for n in readInput().split('\n')]
    res = 0
    
    state = False
    for i in range(len(program)):
        instr = program[i]
        orgInstr = instr
        if "jmp" in instr:
            program[i] = instr.replace("jmp","nop")
        it = 0
        amplVal = 0
        pos = 0
        paths = []
        if state:
            break
        while it < len(program):
            if pos > len(program)-2:
                pos, amplVal = exec(program, pos, amplVal)
#                print("Finished: ", program[i], amplVal)
                res = amplVal
                state = True
                break

            prePos = pos
            preAmplVal = amplVal
            #print("Move: ", preAmplVal, preAmplVal) 
            pos, amplVal = exec(program, pos, amplVal)
            key = program[prePos] + " " + program[pos]
            #print("Move: ", key, preAmplVal, amplVal) 
            if "jmp" in key and key in paths:
                res = preAmplVal
                break
            paths.append(key)
            it +=1
        program[i] = orgInstr

    print("B): ", res)

# Main body
if __name__ == '__main__':
    b()
    sys.exit(1)

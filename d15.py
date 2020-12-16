#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/15
"""

# Imports
import sys
import os
import re
import math
import time

# Global variables
task="d15"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    rows = [n for n in readInput().split('\n')]
    numb = rows[0].split(",")

    numbers = ["X"]*2021
    for n in range(len(numb)):
        numbers[n] = int(numb[n])

    turn = 0
    while turn < 2020:
        if numbers[turn] == "X":
            spoken = numbers[turn-1]
            if numbers.count(spoken) > 1: 
                indices = sorted([i for i, x in enumerate(numbers) if x == spoken], reverse=True)
                last, prev = indices[0:2]
                speak = last - prev
                numbers[turn] = speak
                #break
            else:
                numbers[turn] = 0
        turn += 1

    print("A): ", numbers[2019])

def b():
    rows = [n for n in readInput().split('\n')]
    numb = rows[0].split(",")
    
    #numb = "0,3,6".split(",")
    print(numb)
    iterationSize = 30000000
    numbers = ["X"]*iterationSize
    for n in range(len(numb)):
        numbers[n] = int(numb[n])

    start = time.time()
    turn = 0    
    indices = dict()
    while turn < iterationSize:
        speak = str(numbers[turn])
        if turn%10000 == 0:
            end = time.time()
            exectime = end - start
            print("Progress Turn {} {}% {} total runtime".format(turn, round(turn/iterationSize*100, 1), exectime))
        if numbers[turn] == "X":
            spoken = numbers[turn-1]
            if str(spoken) in indices and len(indices[str(spoken)]) > 1: 
                ind = indices[str(spoken)]
                #print(indices)
                prev, last = ind[-2:]
                speak = last - prev
                numbers[turn] = speak
                #break
            else:
                numbers[turn] = 0
                speak = 0
        if str(speak) in indices:
            indices[str(speak)].append(turn)
        else:
            indices[str(speak)] = [turn]
        turn += 1

    print("B): ", numbers[iterationSize-1])

# Main body
if __name__ == '__main__':
    start = time.time()

    a()
    end = time.time()
    exectime = end - start
    print("Executed A in: {}".format(exectime))
    
    b()
    end = time.time()
    exectime = end - start
    print("Executed B in: {}".format(exectime))
    
    end = time.time()
    exectime = end - start
    print("Executed in: {}".format(exectime))
    sys.exit(1)

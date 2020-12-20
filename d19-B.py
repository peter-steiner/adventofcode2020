#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/19
"""

# Imports
import sys
import os
import re
import math
import time

# Global variables
task="d19-tB"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

possibleStr = []
combos = []
ifa = 0
ifb = 0

infiteloop = 0

def findStr(rules, index):
    val = rules[index]
    l = len(val)
    global infiteloop

    if l == 1:
        val = val[0]
        if val == "a" or val == "b":
            #print("End" + ":"  +val)
            return [val]
        # 2 index
        if " " in val:
            #print(":", val)
            v1 = val.split(" ")

            as1 = findStr(rules, int(v1[0])) 
            as2 = findStr(rules, int(v1[1]))
            versions1 = []
            for a in as1:
                for b in as2:
                    versions1.append(a + b)
            #print(":1", versions1)
            return versions1
        # 1 index
        else:
            #print(":2", val)
            ret = findStr(rules, int(val))
            #print(ret)
            return ret

    # Or split
    if l == 2:
        a, b = val
        # [ ind1, ind2 ]
        v1 = a.split(" ")
        v2 = b.split(" ")

       #print("v1, v2", v1, v2)
        versions1 = []
        if len(v1) == 2:
            as1 = findStr(rules, int(v1[0])) 
            as2 = findStr(rules, int(v1[1]))
            for a in as1:
                for b in as2:
                    versions1.append(a + b)
        else:
            versions1 = findStr(rules, int(v1[0]))
#            print("1", versions1, v1)

        if len(v2) >= 2:
            
            if len(v2) == 2:
                as21 = findStr(rules, int(v2[0])) 
                as22= findStr(rules, int(v2[1]))
            
                versions2 = []
                for a in as21:
                    for b in as22:
                        versions2.append(a + b)
            else:
                if infiteloop > 1:
                    return [""]
                as21 = findStr(rules, int(v2[0])) 
                as22= findStr(rules, int(v2[1]))
                as23= findStr(rules, int(v2[2]))
            
                versions2 = []
                for a in as21:
                    for b in as22:
                        for c in as23:
                            versions2.append(a + b + c)
                infiteloop += 1
        else:
            versions2 = findStr(rules, int(v2[0]))
#            print("2", versions2, v2)

        return versions1 + versions2


def parseRule(rulesStr):

    if " | " in rulesStr:
        a, b = rulesStr.split(" | ")        
        return [a, b]

    return [rulesStr]

def a():
    rows = [n for n in readInput().split('\n')]
    rules = ["x"]*1000
    values = []

    global combos
    determined = ["x"]*1000

    for n in rows:
        #print(n)
        if ": " in n:
            index, rule = n.split(": ")
            if '"' in rule:
                rule = rule.replace('"', "", 2)
                if rule == "a":
                    determined[int(index)] = "a"
                else:
                    determined[int(index)] = "b"
            if "" != n:
                rules[int(index)] = parseRule(rule)
        else:
            if not "" == n:
                values.append(n)

    print(len(values))

    """
    for r in rules:
        if r != "x":
            print(r)    
    """
    maxValLength = 0
    for v in values:
        if len(v) > maxValLength:
            maxValLength = len(v)


    mutEight = findStr(rules, 8)
    mutEleven = findStr(rules, 11)
    la = len(mutEight)
    lb = len(mutEleven)

    print("calc Mut eight")
    mutEightPrim = [] + mutEight

    print(len(mutEightPrim))
    for a in mutEight: 
        for b in mutEight:
            ab = a + b
            if len(ab) <= maxValLength:
                mutEightPrim.append(ab)

    print(len(mutEightPrim))
    mut42 = findStr(rules, 11)
    mut31 = findStr(rules, 11)

    print("calc Mut eleven")
    mutElevenPrim = [] + mutEleven
    for a in mut42:
        for b in mutEleven:
            for c in mut31:
                abc = a + b + c
                if len(abc) <= maxValLength:
                    mutElevenPrim.append(abc)

    
    sum = 0
    print("calc Mut result")
    result = []
    for a in mutEightPrim:
        for b in mutElevenPrim:
#            for c in mut31:
                ab = a + b
                if len(ab) <= maxValLength:
                    for v in values:
                        if v in ab:
                            sum += 1
                            result.append(ab)

    print("Get matching count", sum)
    
    sum = 0
    for v in values:
        if v in result:
            sum += 1
    
    print("A): ", sum)

def b():
    rows = [int(n) for n in readInput().split('\n')]
    res = 0

    print("B): ", res)

# Main body
if __name__ == '__main__':
    start = time.time()

    a()
    end = time.time()
    exectime = end - start
    print("Executed A in: {}".format(exectime))

    """
    b()
    end = time.time()
    exectime = end - start
    print("Executed B in: {}".format(exectime))
    """

    end = time.time()
    exectime = end - start
    print("Executed in: {}".format(exectime))
    sys.exit(1)

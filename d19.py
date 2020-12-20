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
task="d19"
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


def findStr(rules, index):
    val = rules[index]
    l = len(val)

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

        if len(v2) == 2:
            as21 = findStr(rules, int(v2[0])) 
            as22= findStr(rules, int(v2[1]))
            versions2 = []
            for a in as21:
                for b in as22:
                    versions2.append(a + b)
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
    la = len(findStr(rules, 8))
    lb = len(findStr(rules, 11))
    
    print(rules[0])
    inds = rules[0][0].split(" ")
    result = findStr(rules, int(inds[0]))
    for i in range(1, len(inds)):
        #print("A", findStr(rules, int(inds[i]), ""))
        resA = findStr(rules, int(inds[i]))
        resTmp = []
        for a in resA:
            for b in result:
                resTmp.append(b + a)
        result = resTmp

    print(len(result), la*lb)
    result = list(set(result))
    #print("Mutations", result)
    #print("Values", values)

    sum = 0
    for v in values:
        if v in result:
            sum += 1
            #print("------------")
            #print(v)
            ind = result.index(v)
            #print(result[ind], ind)

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

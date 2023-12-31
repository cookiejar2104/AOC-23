# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 09:56:06 2023

@author: DIBYAJYOTI
"""

import sys
from collections import defaultdict
import math
from dataclasses import dataclass

@dataclass
class PartNum:
    """Class for keeping track of an item in inventory."""
    number: int
    leftIdx: int
    rightIdx: int
    lineNum: int

    def __init__(self, n: int, l: int, r: int, ln: int):
        self.number = n
        self.leftIdx = l
        self.rightIdx = r
        self.lineNum = ln

maxx = 0
maxy = 0

def parse(): 
    file1 = open('input.in', 'r')
    Lines = file1.readlines()

    partnums = []

    global maxx, maxy
    maxx = len(Lines) - 1
    maxy = len(Lines[maxx]) - 2

    for linenum,line in enumerate(Lines):
        num = -1
        leftidx = -1
        rightidx = -1
        for idx,c in enumerate(line):
            if c.isdigit():
                if leftidx < 0:
                    leftidx = idx
                rightidx = idx
                if num < 0:
                    num = int(c)
                else:
                    num = num * 10 + int(c)
            elif num > 0:
                partnums.append(PartNum(num, leftidx, rightidx, linenum))
                num = -1
                leftidx = -1
                rightidx = -1

    return Lines, partnums

def task1():

    Lines, partnums = parse()

    sum = 0

    for p in partnums:
        found = False
        for x in range(p.lineNum-1, p.lineNum+2):
            for y in range(p.leftIdx-1, p.rightIdx+2):
                if x < 0 or x > maxx:
                    continue
                if y < 0 or y > maxy:
                    continue
                if Lines[x][y] != '.' and not Lines[x][y].isdigit():
                    found = True
                    break
        if found:
            sum += p.number

    print(sum)

def task2():
    Lines, partnums = parse()

    sum = 0

    for x in range(0, maxx+1):
        for y in range(0, maxy+1):
            if Lines[x][y] != '*':
                continue
            connectedparts = []
            for p in partnums:
                if y >= (p.leftIdx - 1) and y <= (p.rightIdx +1) and abs(p.lineNum - x) < 2:
                    connectedparts.append(p)
            if len(connectedparts) == 2:
                sum += (connectedparts[0].number * connectedparts[1].number)
 
    print(sum)

def main() -> int:
    task1()
    task2()

if __name__ == '__main__':
    sys.exit(main())


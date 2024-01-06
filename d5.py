# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:42:31 2024

@author: DIBYAJYOTI
"""

import sys
from collections import defaultdict
import math
from dataclasses import dataclass

import re

@dataclass
class Mapping:
    """Class for keeping track of an item in inventory."""
    dstStart: int
    srcStart: int
    range: int

    def __init__(self, d: int, s: int, r: int):
        self.dstStart = d
        self.srcStart = s
        self.range = r
    
    def contains(self, i: int):
        return (i >= self.srcStart) and (i <= self.srcStart + self.range)

    def map(self, i: int):
        return i - self.srcStart + self.dstStart

    def intersect(self, b: int, e: int):
        return max(b, self.srcStart) <= min(e, self.srcStart + self.range)

    def cut(self, b: int, e: int):
        return (max(b, self.srcStart) - self.srcStart + self.dstStart , min(e, self.srcStart + self.range) - self.srcStart + self.dstStart)

    def remains(self, b: int, e: int):
        retval = []
        if b < self.srcStart:
            retval.append((b, self.srcStart - 1))
        if e > (self.srcStart + self.range):
            retval.append((self.srcStart + self.range + 1, e))
        return retval


def task1(): 
    file1 = open('input.in', 'r')
    Lines = file1.readlines()

    seeds = [] 

    mappings = []

    for line in Lines:
        if not seeds:
           seeds = [int(x) for x in line.split(":")[1].strip().split(" ")]
        else:
            if len(line) < 2:
                continue
            if ":" in line: 
                mappings.append([])
            else:
                mappings[-1].append(Mapping(*[int(x) for x in line.split(" ")]))

    current = seeds.copy()
    for m in mappings:
        tmp = []
        for c in current:
            for mm in m:
                if mm.contains(c):
                    tmp.append(mm.map(c))
                    break
            else:
                tmp.append(c)
        current = tmp.copy()

    print(min(current))
 

def task2():
    file1 = open('input.in', 'r')
    Lines = file1.readlines()

    seeds = []

    mappings = []

    for line in Lines:
        if not seeds:
            nums = line.split(":")[1].strip().split(" ")
            for x in range(0, len(nums)-1, 2):
                seeds.append((int(nums[x]), int(nums[x]) + int(nums[x+1])))
        else:
            if len(line) < 2:
                continue
            if ":" in line:
                mappings.append([])
            else:
                mappings[-1].append(Mapping(*[int(x) for x in line.split(" ")]))

    current = seeds.copy()
    for m in mappings:
        tmp = []
        while len(current) > 0:
            left = []
            for c in current:
                for mm in m:
                    if mm.intersect(c[0], c[1]):
                           tmp.append(mm.cut(c[0], c[1]))
                           left = left + mm.remains(c[0], c[1])
                           break
                else:
                    tmp.append(c)
            current = left
        current = tmp.copy()

    ret = current[0][0]
    for c in current:
        ret = min(ret, c[0])
   
    print(ret)

def main() -> int:
    task1()
    task2()

if __name__ == '__main__':
    sys.exit(main())


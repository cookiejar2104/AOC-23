# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:33:34 2024

@author: DIBYAJYOTI
"""

import sys
from collections import defaultdict
import math
from dataclasses import dataclass

import re

def task1(): 
    file1 = open('input.in', 'r')
    Lines = file1.readlines()

    sum = 0

    for line in Lines:
        winning, mine = line.split(":")[1].split("|")
        winning = set([int(x) for x in re.split(r'\s{1,}', winning.strip())])
        mine = set([int(x) for x in re.split(r'\s{1,}', mine.strip())])
        if(mine & winning):
            sum += pow(2, len(winning & mine)-1)

    print(sum)


def task2():
    file1 = open('input.in', 'r')
    Lines = file1.readlines()

    cards = defaultdict(int)

    for num, line in enumerate(Lines):
        cards[num] = cards[num] + 1
        winning, mine = line.split(":")[1].split("|")
        winning = set([int(x) for x in re.split(r'\s{1,}', winning.strip())])
        mine = set([int(x) for x in re.split(r'\s{1,}', mine.strip())])
        if(mine & winning):
            won = len(winning & mine)
            for x in range(0, won):
                idx = num + x + 1
                if idx >= len(Lines):
                    continue
                cards[idx] = cards[idx] + cards[num]

    print(sum(cards.values()))

def main() -> int:
    task1()
    task2()

if __name__ == '__main__':
    sys.exit(main())


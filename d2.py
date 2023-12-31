import sys
from collections import defaultdict
import math

keys = ["red", "green", "blue"]
values = [12,13,14]
ballset = dict(zip(keys, values))

def task1():
    file1 = open('input.in', 'r')
    Lines = file1.readlines()
 
    sum = 0   

    for line in Lines:
        id = line.split(":")[0].split(" ")[1]
        possible = True
        for x in line.split(":")[1].split(";"):
            for y in x.strip().split(","):
                 qty, col = y.strip().split(" ")
                 if int(qty) > ballset[col]:
                     possible = False
        if possible:
            sum += int(id)
    print(sum)

def task2():
    file1 = open('input.in', 'r')
    Lines = file1.readlines()
 
    sum = 0

    for line in Lines:
        bs = defaultdict(int)
        id = line.split(":")[0].split(" ")[1]
        possible = True
        for x in line.split(":")[1].split(";"):
            for y in x.strip().split(","):
                 qty, col = y.strip().split(" ")
                 bs[col] = max(bs[col], int(qty))
        sum += math.prod(bs.values())


    print(sum)

def main() -> int:
    task1()
    task2()

if __name__ == '__main__':
    sys.exit(main())


import sys


def task1():
    file1 = open('input.in', 'r')
    Lines = file1.readlines()
 
    sum = 0   

    for line in Lines:
        for c in line:
            if c.isdigit():
                sum += int(c) * 10
                break
        for c in line[::-1]:
            if c.isdigit():
                sum += int(c)
                break

    print(sum)

keys = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
values = [1,2,3,4,5,6,7,8,9]
mapping = dict(zip(keys, values))

def task2():
    file1 = open('input.in', 'r')
    Lines = file1.readlines()
 
    sum = 0

    for line in Lines:
        s = line
        while s:
            found = False
            for k in keys:
                if s.startswith(k):
                    sum += mapping[k] * 10
                    found = True
                    break
            else:
                c = s[0]
                if c.isdigit():
                    sum += int(c) * 10
                    found = True

            if found:
                break
   
            s = s[1:]

        s = line
        while s:
            found = False
            for k in keys: 
                if s.endswith(k):
                    sum += mapping[k] 
                    found = True
                    break
            else:
                c = s[-1]
                if c.isdigit():
                     sum += int(c)
                     found = True
            
            if found:
                break

            s = s[:-1]
    print(sum)

def main() -> int:
    task1()
    task2()

if __name__ == '__main__':
    sys.exit(main())
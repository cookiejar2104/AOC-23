with open("input.in") as fin:
    data = fin.read()
    
ans = 0;

for line in data.strip().split():
    num1 = None
    num2 = None
    for c in line:
        if c.isdigit() and num1 == None:
            num1 = c
        if c.isdigit():
            num2 = c
        
    num = int(num1 + num2)
    ans+=num

print(ans)
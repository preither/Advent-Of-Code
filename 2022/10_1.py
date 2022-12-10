f = open('input.txt', 'r')
lines = f.readlines()


x = 1
next_add = 0

last_cylce = 220

cycle = 0
next_mark = 20

s = 0

for l in lines:
    cut = l[:-1].split(" ")

    x += next_add
    cycle += 1
    if cycle >= next_mark:
        if cycle > next_mark:
            s += (x-next_add)*next_mark
        else:
            s += x*next_mark
        if next_mark == last_cylce:
            break
        else:
            next_mark += 40

    next_add = 0
    if cut[0] == "addx":
        cycle += 1
        next_add = int(cut[1])

print(s)
    
        


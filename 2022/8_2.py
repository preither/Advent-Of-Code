with open('input.txt') as f:
    contents = f.readlines()

max = 0
xlen = len(contents[0]) -1
ylen = len(contents)
for x in range(xlen):
    for y in range(ylen):
        val = contents[y][x]
        score = 1
        cnt = 0
        for i in range(x):
            cnt += 1
            if contents[y][x-i-1] >= val:
                break
        score *= cnt
        cnt = 0
        for i in range(x+1, xlen):
            cnt += 1
            if contents[y][i] >= val:
                break
        score *= cnt
        cnt = 0
        for i in range(y):
            cnt += 1
            if contents[y-i-1][x] >= val:
                break
        score *= cnt
        cnt = 0
        for i in range(y+1, ylen):
            cnt += 1
            if contents[i][x] >= val:
                break
        score *= cnt

        if score > max:
            max = score

            




print(max)
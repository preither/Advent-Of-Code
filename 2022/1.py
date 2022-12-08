with open('input.txt') as f:
    contents = f.readlines()

max  = [0, 0, 0]
cnt = 0
for i in contents:
    max.sort()
    if i == "\n":
        if cnt > max[0]:
            max[0] = cnt
        cnt = 0
    else:
        cnt += int(i[:-1])

print(sum(max))
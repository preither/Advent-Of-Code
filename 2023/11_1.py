with open('input.txt') as f:
    c = f.readlines()

galaxies = []
expand_cnt = 0

empty_columns = []
for j in range(len(c[0])-1):
    column_empty = True
    for i in range(len(c)):
        if c[i][j] == "#":
            column_empty = False
    if column_empty:
        empty_columns.append(j)

for i in range(len(c)):
    row_empty = True
    for j in range(len(c[0])-1):
        if c[i][j] == "#":
            expand_cnt_c = 0
            for z in empty_columns:
                if j < z:
                    break
                expand_cnt_c += 1
            galaxies.append([i + expand_cnt,j+expand_cnt_c])
            row_empty = False
    if row_empty:
        expand_cnt += 1

s = 0
for i in range(len(galaxies)):
    for j in range(i+1,len(galaxies)):
        s += abs(galaxies[i][0]-galaxies[j][0]) + abs(galaxies[i][1]-galaxies[j][1])

print(s)


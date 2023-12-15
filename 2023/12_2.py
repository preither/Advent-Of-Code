def check(row):
    s = ""
    cnt = 0
    for r in row:
        if r == "#":
            cnt += 1
        else:
            if cnt > 0:
                s += "," + str(cnt)
                cnt = 0
    
    if cnt > 0:
        s += "," + str(cnt)

    return s[1:]

with open('test.txt') as f:
    c = f.readlines()

cnt = 0
fortschritt = 0
for i in c:
    fortschritt += 1
    split = i.split(" ")

    row = split[0]
    row = 5 * (row + "?")
    row = row[:-1]

    expect = split[1][:-1]
    expect = 5 * (expect + ",")
    expect = expect[:-1]

    damaged = row.count("?")

    for d in range(2**damaged):
        copy = row
        for l in range(damaged):
            bit = 1 & (d >> l)
            val = ""
            if bit == 0:
                val = "."
            else:
                val = "#"
            copy = copy.replace("?", val, 1)
        checked = check(copy)
        if checked == expect:
            cnt += 1
    print(fortschritt)
        
print(cnt)
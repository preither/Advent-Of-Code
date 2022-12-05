f = open('input.txt', 'r')
lines = f.readlines()

cnt = 0

for l in lines:
    size = len(l)
    first = l[:int(size/2)]
    second = l[int(size/2):]
    for i in first:
        if i in second:
            val = ord(i) - ord('a') + 1
            if val < 0:
                val = ord(i) - ord('A') + 1 + 26
            cnt += val
            break

print(cnt)
    
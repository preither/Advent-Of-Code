f = open('input.txt', 'r')
lines = f.readlines()

cnt = 0
possible = ""
for l in range(len(lines)):
    if l % 3 == 0:
        possible = ""
        for i in lines[l]:
            if i in lines[l+1]:
                possible += i

        for i in possible:
            if i in lines [l+2]:
                val = ord(i) - ord('a') + 1
                if val < 0:
                    val = ord(i) - ord('A') + 1 + 26
                cnt += val
                break

print(cnt)
    
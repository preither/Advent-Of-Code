with open('input.txt') as f:
    line = f.readlines()[0]

cnt = 0
chars = []

for i in line:
    chars.append(i)
    if cnt >= 13:    
        found = True
        for i in range(13):
            if chars[i] in chars[i+1:]:
                found = False
                break
        if found:
            break
        chars.pop(0)
    cnt += 1

print(cnt + 1)

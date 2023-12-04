with open('input.txt') as f:
    c = f.readlines()

win_cnt = []
for i in c:
    nums = i[:-1].split(": ")[1].split(" | ")
    winning = nums[0].split(" ")
    having = nums[1].split(" ")

    cnt = 0
    for j in having:
        if j != "" and j in winning:
            cnt += 1
    win_cnt.append(cnt)

copies = []
for i in range(len(win_cnt)):
    copies.append(1)

for i in range(len(win_cnt)):
    for j in range(i+1, i+1+win_cnt[i]):
        if j >= len(win_cnt):
            break
        copies[j] += copies[i]

cnt = sum(copies)
print(cnt)
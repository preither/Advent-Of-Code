with open('input.txt') as f:
    stones = list(map(int, f.readline()[:-1].split(" ")))

stone_cnt = {}
for s in stones:
    stone_cnt[s] = 1
cnt = 0

while cnt < 75:
    new_stones = {}
    for s in stone_cnt:
        stone_str = str(s)
        new = []
        if s == 0:
            new.append((1, stone_cnt[s]))
        elif len(stone_str) %2 == 0:
            split_point = int(len(stone_str)/2)
            new.append((int(stone_str[:split_point]), stone_cnt[s]))
            new.append((int(stone_str[split_point:]), stone_cnt[s]))
        else:
            new.append((s * 2024, stone_cnt[s]))

        for i in new:
            if i[0] in new_stones:
                new_stones[i[0]] += i[1]
            else:
                new_stones[i[0]] = i[1]

    stone_cnt = new_stones
    cnt += 1
    print(cnt)

s = 0

for i in stone_cnt:
    s += stone_cnt[i]

print(s)
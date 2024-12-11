with open('input.txt') as f:
    stones = list(map(int, f.readline()[:-1].split(" ")))

cnt = 0

while cnt < 25:
    new_stones = []
    for s in stones:
        stone_str = str(s)
        if s == 0:
            new_stones.append(1)
        elif len(stone_str) %2 == 0:
            split_point = int(len(stone_str)/2)
            new_stones.append(int(stone_str[:split_point]))
            new_stones.append(int(stone_str[split_point:]))
        else:
            new_stones.append(s * 2024)

    stones = new_stones
    cnt += 1

print (len(stones))
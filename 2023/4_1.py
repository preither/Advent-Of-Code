with open('input.txt') as f:
    c = f.readlines()

s = 0
for i in c:
    nums = i[:-1].split(": ")[1].split(" | ")
    winning = nums[0].split(" ")
    having = nums[1].split(" ")

    cnt = 0
    for j in having:
        if j != "" and j in winning:
            cnt += 1
    if cnt > 0:
        s += 2**(cnt-1)

print(s)
    
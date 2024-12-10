with open('input.txt') as f:
    contents = f.readlines()

solutions = 0
for c in contents:
    v, f = c[:-1].split(":")
    val = int(v)
    nums = list(map(int, f[1:].split(" ")))

    for i in range(2**len(nums[1:])):
        s = nums[0]
        bi = bin(i)
        while len(bi) - 2 < len(nums[1:]):
            bi = bi[:2] + "0" + bi[2:]
        cnt = 1
        for j in bi[2:]:
            if j == "0":
                s += nums[cnt]
            else:
                s *= nums[cnt]
            if s > val:
                break
            cnt += 1

        if val == s:
            solutions += val
            break


print(solutions)
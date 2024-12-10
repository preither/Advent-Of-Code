def decimal_to_base3(num):
    if num == 0:
        return '0'
    base3 = ''
    while num > 0:
        base3 = str(num % 3) + base3
        num = num // 3
    return base3

with open('input.txt') as f:
    contents = f.readlines()

solutions = 0
for c in contents:
    v, f = c[:-1].split(":")
    val = int(v)
    nums = list(map(int, f[1:].split(" ")))

    for i in range(3**len(nums[1:])):
        s = nums[0]
        bi = decimal_to_base3(i)
        while len(bi)< len(nums[1:]):
            bi = "0" + bi
        cnt = 1
        for j in bi:
            if j == "0":
                s += nums[cnt]
            elif j == "1":
                s *= nums[cnt]
            else:
                s = int(str(s) + str(nums[cnt]))
            if s > val:
                break
            cnt += 1

        if val == s:
            solutions += val
            break


print(solutions)
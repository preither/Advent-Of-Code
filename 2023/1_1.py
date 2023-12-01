import re

with open('input.txt') as f:
    c = f.readlines()

s = 0
for i in c:
    nums = re.findall("[0-9]", i)
    s += 10 * int(nums[0]) + int(nums[-1])

print(s)

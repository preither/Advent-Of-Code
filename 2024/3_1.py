import re

with open('input.txt') as f:
    contents = f.readlines()

string = ""
for c in contents:
    string += c[:-1]

x = re.findall('mul\([0-9]?[0-9]?[0-9]?,[0-9]?[0-9]?[0-9]?\)', string)

s = 0
for mul in x:
    nums= mul[4:-1].split(",")
    s += int(nums[0]) * int(nums[1])

print(s)
    
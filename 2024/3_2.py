import re

with open('input.txt') as f:
    contents = f.readlines()

string = ""
for c in contents:
    string += c[:-1]

x = re.findall('(mul\([0-9]?[0-9]?[0-9]?,[0-9]?[0-9]?[0-9]?\))|(do\(\))|(don\'t\(\))', string)

enabled = True
s = 0
for mul in x:
    if mul[0] != '' and enabled:
        nums= mul[0][4:-1].split(",")
        s += int(nums[0]) * int(nums[1])
    if mul[1] != '':
       enabled = True
    if mul[2] != '':
       enabled = False


print(s)
    
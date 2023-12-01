import re

num_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open('input.txt') as f:
    c = f.readlines()

s = 0
num_regex = "|".join(num_strings)
regex = "[0-9]|" + num_regex
for i in c:
    nums = [0,0]
    
    #find first
    nums[0] = re.findall( regex, i) [0]
    
    #find last
    for j in range(0, len(i)):
        num = re.findall( regex, i[len(i)-j-1:])
        if len(num) > 0:
            nums[1] = num[0]
            break

    num = [0,0]    

    for i in range(2):
        try:
            num[i] = num_strings.index(nums[i]) + 1
        except:
            num[i] = nums[i]
    s += 10 * int(num[0]) + int(num[1])

print(s)

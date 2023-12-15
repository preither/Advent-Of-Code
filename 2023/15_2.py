def hash(string):
    h = 0
    for i in string:
        h += ord(i)
        h *= 17
        h %= 256
    return h

with open('input.txt') as f:
    c = f.readlines()

boxes = []
for b in range(256):
    boxes.append({})

s = 0
i = c[0][:-1].split(",")

for j in i:
    if "-" in j:
        split = j.split("-")
        label = split[0]
        box = hash(label)
        try:
            boxes[box].pop(label)
        except:
            pass

    if "=" in j:
        split = j.split("=")
        label = split[0]
        box = hash(label)
        focal = int(split[1])
        boxes[box][label] = focal

for j in range(len(boxes)):
    cnt = 1
    for key in boxes[j]:
        s += (j+1) * cnt * boxes[j][key]
        cnt += 1

print(s)

     

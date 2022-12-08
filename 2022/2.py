with open('input.txt') as f:
    contents = f.readlines()

lut = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

win =  {
    "A" : "Y",
    "B" : "Z",
    "C" : "X"
}

draw  = {
    "A" : "X",
    "B" : "Y",
    "C" : "Z"
}

loose = {
    "A" : "Z",
    "B" : "X",
    "C" : "Y"
}

points = 0
for i in contents:
    if i[2] == "X":
        points +=  lut[loose[i[0]]]
    if i[2] == "Y":
        points +=  lut[draw[i[0]]] + 3
    if i[2] == "Z":
        points +=  lut[win[i[0]]] + 6
    

print(points)

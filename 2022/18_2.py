from copy import copy

class Field:
    def __init__(self):
        self.array = []
        self.cnt = 0

        for x in range(21):
            self.array.append([])
            for y in range(21):
                self.array[x].append([])
                for z in range(21):
                    self.array[x][y].append(0)
    def add_cube(self,x,y,z):
        self.array[x][y][z] = 1

    def check_cube(self,x,y,z):
        try:
            if self.array[x][y][z] != 1:
                self.cnt += 1
        except:
            pass
    def check_cube_air(self,x,y,z):
        try:
            if self.array[x][y][z] == 1:
                self.cnt -= 1
        except:
            pass
    def flip(self,x,y,z):
        if self.array[x+1][y][z] == 0 or self.array[x-1][y][z] == 0 or self.array[x][y+1][z] == 0 or self.array[x][y-1][z] == 0 or self.array[x][y][z+1] == 0 or self.array[x][y][z-1] == 0:
            self.array[x][y][z] = 0

f = open('input.txt', 'r')
lines = f.readlines()

field = Field()

for l in lines:
    cut = l[:-1].split(",")
    field.add_cube(int(cut[0]),int(cut[1]),int(cut[2]))

cnt = 0
for x in range(0,21):
    for y in range(0,21):
        for z in range(0,21):
            if field.array[x][y][z] == 1:
                field.check_cube(x-1,y,z)
                field.check_cube(x+1,y,z)
                field.check_cube(x,y-1,z)
                field.check_cube(x,y+1,z)
                field.check_cube(x,y,z-1)
                field.check_cube(x,y,z+1)
            else:
                ##check if pocket
                found = False
                for i in range(x, 21):
                    if field.array[i][y][z] != 0:
                        found = True
                        break
                if found:
                    found = False
                    for i in range(x, -1, -1):
                        if field.array[i][y][z] != 0:
                            found = True
                            break
                if found:
                    found = False
                    for i in range(y, 21):
                        if field.array[x][i][z] != 0:
                            found = True
                            break
                if found:
                    found = False
                    for i in range(y, -1, -1):
                        if field.array[x][i][z] != 0:
                            found = True
                            break
                if found:
                    found = False
                    for i in range(z, 21):
                        if field.array[x][y][i] != 0:
                            found = True
                            break
                if found:
                    found = False
                    for i in range(z, -1, -1):
                        if field.array[x][y][i] != 0:
                            found = True
                            break
                if found:
                    field.array[x][y][z] = 2

for x in range(0,21):
    for y in range(0,21):
        for z in range(0,21):
            if field.array[x][y][z] == 2:
                field.flip(x,y,z)

for x in range(0,21):
    for y in range(0,21):
        for z in range(0,21):
            if field.array[x][y][z] == 2:
                field.check_cube_air(x-1,y,z)
                field.check_cube_air(x+1,y,z)
                field.check_cube_air(x,y-1,z)
                field.check_cube_air(x,y+1,z)
                field.check_cube_air(x,y,z-1)
                field.check_cube_air(x,y,z+1)




print(field.cnt)
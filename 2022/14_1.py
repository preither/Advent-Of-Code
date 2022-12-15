from copy import copy
class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Field:
    def __init__(self):
        self.f = []
        for i in range(200):
            self.f.append([])
            for j in range(200):
                self.f[i].append(0)

        self.norm = 400
        self.lowest = 0

    def check_horizontal(self, p1, p2):
        if int(p1[0]) == int(p2[0]):
            return "vertical"
        else:
            return "horizontal"

    def add_line(self, line):
        for i in range(len(line)-1):
            if self.check_horizontal(line[i], line[i+1]) == "vertical":
                y1 = int(line[i][1])
                y2 = int(line[i+1][1])
                if y2 < y1:
                    help = y2
                    y2 = y1
                    y1 = help
                
                if self.lowest < y2:
                    self.lowest = y2

                x = int(line[i][0]) - self.norm
                for j in range(y1,y2+1):
                    self.f[j][x] = 1
            else:
                x1 = int(line[i][0]) - self.norm
                x2 = int(line[i+1][0]) - self.norm
                if x2 < x1:
                    help = x2
                    x2 = x1
                    x1 = help
                
                y = int(line[i][1])

                if self.lowest < y:
                    self.lowest = y

                for j in range(x1,x2+1):
                    self.f[y][j] = 1

    def iterate_sand(self, sand_pos):
        if sand_pos.y+1 > self.lowest:
            return True
        if self.f[sand_pos.y+1][sand_pos.x] == 0:
            self.f[sand_pos.y][sand_pos.x] = 0
            self.f[sand_pos.y+1][sand_pos.x] = 2
            sand_pos.y += 1
        elif self.f[sand_pos.y+1][sand_pos.x-1] == 0:
            self.f[sand_pos.y][sand_pos.x] = 0
            self.f[sand_pos.y+1][sand_pos.x-1] = 2
            sand_pos.y += 1
            sand_pos.x -= 1
        elif self.f[sand_pos.y+1][sand_pos.x+1] == 0:
            self.f[sand_pos.y+1][sand_pos.x+1] = 2
            self.f[sand_pos.y][sand_pos.x] = 0
            sand_pos.y += 1
            sand_pos.x += 1
        
        return False



    def insert_sand(self):
        x = 500 - self.norm
        y = 0

        sand_pos = Pos(x, y)

        last_pos = copy(sand_pos)

        while(1):
            if self.iterate_sand(sand_pos):
                return True
            else:
                if sand_pos.x == last_pos.x and sand_pos.y == last_pos.y:
                    break
            last_pos = copy(sand_pos)

        return False

            




f = open('input.txt', 'r')
lines = f.readlines()

field = Field()

for l in lines:
    cut = l[:-1].split(" -> ")
    line = []
    for c in cut:
        line.append(c.split(","))
    field.add_line(line)

cnt = 0

while(field.insert_sand() == False):
    cnt += 1

print(cnt)
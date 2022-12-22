class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Field:
    def __init__(self, array, start):
        self.array = array
        self.b = len(array[0]) -1
        self.h = len(array)
        self.pos = Vec(start, 0)
        self.direction = Vec(1, 0)

    def rotate(self, dircetion):
        if dircetion == "R":
            new_x = self.direction.y * -1
            new_y = self.direction.x
        else:
            new_x = self.direction.y
            new_y = self.direction.x * -1 
        self.direction.x = new_x
        self.direction.y = new_y

    def find_left_start(self, row):
        for i in range(self.b):
            try:
                if self.array[row][i] != " ":
                    return i
            except:
                pass

    def find_right_start(self, row):
        for i in range(self.b-1, -1, -1):
            try:
                if self.array[row][i] != " ":
                    return i
            except:
                pass

    def find_top_start(self, column):
        for i in range(self.h):
            try:
                if self.array[i][column] != " ":
                    return i
            except:
                pass

    def find_bottom_start(self, column):
        for i in range(self.h-1, -1, -1):
            try:
                if self.array[i][column] != " ":
                    return i
            except:
                pass

    def jump_edge(self):
        if self.direction.x == 1:
            return self.find_left_start(self.pos.y), self.pos.y
        elif self.direction.x == -1:
            return self.find_right_start(self.pos.y), self.pos.y
        elif self.direction.y == 1:
            return self.pos.x, self.find_top_start(self.pos.x)
        else:
            return self.pos.x, self.find_bottom_start(self.pos.x)

    def move(self, steps):
        for i in range(steps):
            new_x = self.pos.x + self.direction.x
            new_y = self.pos.y + self.direction.y

            if new_x >= self.b:
                try:
                    new_x = self.find_left_start(new_y)
                except:
                    pass
            if new_x < 0:
                try:
                    new_x = self.find_right_start(new_y)
                except:
                    pass
            if new_y >= self.h:
                try:
                    new_y = self.find_top_start(new_x)
                except:
                    pass
            if new_y < 0:
                try:
                    new_y = self.find_bottom_start(new_x)
                except:
                    pass

            #print(new_x, new_y)
            try:
                dest = self.array[new_y][new_x]
            except:
                dest = " "
            if dest == " ":
                new_x, new_y = self.jump_edge()
                dest = self.array[new_y][new_x]

            if dest == "#":
                break
            else:
                self.pos.x = new_x
                self.pos.y = new_y


f = open('test.txt', 'r')
lines = f.readlines()

array = lines[:-2]

b = len(array[0])
h = len(array)

#find start
for i in range(b):
    if array[0][i] == ".":
        start = i
        break

field = Field(array, start)

commands = lines[-1]
moves = commands[:-1].replace("R", " ").replace("L", " ").split(" ")

cnt = 1
field.move(int(moves[0]))
print(field.pos.x, field.pos.y)
for c in commands:
    if c == "R" or c == "L":
        field.rotate(c)
        field.move(int(moves[cnt]))
        cnt += 1
        print(field.pos.x, field.pos.y)
        

pw = 1000 * (field.pos.y + 1) + 4* (field.pos.x + 1)

if field.direction.y == 1:
    pw += 1
elif field.direction.x == -1:
    pw += 2
elif field.direction.y  == -1:
    pw += 3

print(pw)


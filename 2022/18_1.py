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
            self.cnt += 1-self.array[x][y][z] 
        except:
            pass


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

print(field.cnt)
class rope:
    def up(self):
        self.h_y+=1
        if self.h_y - self.t_y > 1:
            self.t_y += 1
            if self.h_x != self.t_x:
                self.t_x = self.h_x

    def down(self):
        self.h_y-=1
        if self.t_y - self.h_y > 1:
            self.t_y -= 1
            if self.h_x != self.t_x:
                self.t_x = self.h_x
    def rigth(self):
        self.h_x+=1
        if self.h_x - self.t_x > 1:
            self.t_x += 1
            if self.h_y != self.t_y:
                self.t_y = self.h_y
    def left(self):
        self.h_x-=1
        if self.t_x - self.h_x > 1:
            self.t_x -= 1
            if self.h_y != self.t_y:
                self.t_y = self.h_y

    
    h_x = 0
    h_y = 0

    t_x = 0
    t_y = 0

with open('input.txt') as f:
    contents = f.readlines()

visited = {}

r = rope()

moves = {
    "U": r.up,
    "D": r.down,
    "R": r.rigth,
    "L": r.left
}


for c in contents:
    cut = c[:-1].split(" ")

    for i in range(int(cut[1])):
        moves[cut[0]]()
        #print("h", r.h_x, r.h_y)
        #print("t", r.t_x, r.t_y)

        st = str(r.t_x) + "_" + str(r.t_y)
        visited[st] = 1


print(len(visited))



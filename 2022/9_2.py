class rope:
    def up(self):
        self.y[0]+=1
        self.tail()

    def down(self):
        self.y[0]-=1
        self.tail()

    def rigth(self):
        self.x[0]+=1
        self.tail()

    def left(self):
        self.x[0]-=1
        self.tail()

    def tail(self):
        for i in range(len(self.x) - 1):
            x_dif = self.x[i] - self.x[i+1]
            y_dif = self.y[i] - self.y[i+1]

            if abs(x_dif) + abs(y_dif) > 2:
                self.x[i+1] += x_dif / abs(x_dif)
                self.y[i+1] += y_dif / abs(y_dif)
            else:
                if abs(x_dif) > 1:
                    self.x[i+1] += x_dif /abs(x_dif)
                    if self.y[i+1] != self.y[i]:
                        self.y[i+1] = self.y[i]
                if abs(y_dif) > 1:
                    self.y[i+1] += y_dif /abs(y_dif)
                    if self.x[i+1] != self.x[i]:
                        self.x[i+1] = self.x[i]

    x = [0,0,0,0,0,0,0,0,0,0]
    y = [0,0,0,0,0,0,0,0,0,0]



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

        st = str(r.x[-1]) + "_" + str(r.y[-1])
        visited[st] = 1


print(len(visited))



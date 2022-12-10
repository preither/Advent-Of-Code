class drawer():
    def draw(self,x,cycle):
        cycle = cycle%40
        if abs(x-cycle) <= 1:
            self.row += "#"
        else:
            self.row += "."
        if (cycle+1) % 40 == 0:
            print(self.row)
            self.row = ""

    row =""

f = open('input.txt', 'r')
lines = f.readlines()

x = 1
cycle = -1

d = drawer()

for l in lines:
    cut = l[:-1].split(" ")

    cycle += 1
    d.draw(x, cycle)

    if cut[0] == "addx":
        cycle += 1
        d.draw(x, cycle)
        x += int(cut[1])       


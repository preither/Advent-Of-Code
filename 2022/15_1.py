class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Raute:
    def __init__(self, sensor, beacon):
        self.distance = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)
        self.top = Point(sensor.x, sensor.y + self.distance)
        self.bottom = Point(sensor.x, sensor.y - self.distance)
        self.right = Point(sensor.x + self.distance, sensor.y)
        self.left = Point(sensor.x - self.distance, sensor.y)
        self.sensor = sensor

class Field:
    def __init__(self):
        self.beacons = []
        self.sensors = []
        self.rauten = []
        self.max_x = 0
        self.min_x = 0

    def checkMinMax(self, new_min_max):
        if new_min_max > self.max_x:
            self.max_x = new_min_max
        if new_min_max < self.min_x:
            self.min_x = new_min_max

    def addSensor(self, s_x, s_y, b_x, b_y):
        #self.checkMinMax(s_x)
        #self.checkMinMax(b_x)
        self.sensors.append(Point(s_x, s_y))
        self.beacons.append(Point(b_x, b_y))
        self.rauten.append(Raute(self.sensors[-1], self.beacons[-1]))
        self.checkMinMax(self.rauten[-1].left.x)
        self.checkMinMax(self.rauten[-1].right.x)

    def checkLine(self, y_line):
        line = []
        for i in range(self.min_x, self.max_x+1):
            line.append(".")
        for s in self.sensors:
            if s.y == y_line:
                line[s.x + abs(self.min_x)] = "S"
        for b in self.beacons:
            if b.y == y_line:
                line[b.x + abs(self.min_x)] = "B"

        for r in self.rauten:
            if y_line >= r.bottom.y and y_line <= r.top.y:
                #print(r.sensor.x, r.sensor.y)
                dist = abs(r.sensor.y - y_line) 
                start_x = r.sensor.x - (r.distance - dist)
                end_x = r.sensor.x + (r.distance - dist)
                for i in range(start_x, end_x+1):
                    if line[i + abs(self.min_x)] == ".":
                        line[i + abs(self.min_x)] = "#"
                #print(line)

        return line.count("#")


        





f = open('input.txt', 'r')
lines = f.readlines()

field = Field()

for l in lines:
    cut = l[:-1].split("=")
    s_x = int(cut[1].split(",")[0])
    s_y = int(cut[2].split(":")[0])
    b_x = int(cut[3].split(",")[0])
    b_y = int(cut[4])

    field.addSensor(s_x, s_y, b_x, b_y)

print(field.checkLine(2000000))




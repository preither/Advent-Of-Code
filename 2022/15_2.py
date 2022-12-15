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
        self.empty_point = Point(0,0)

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

    def checkLine(self, y_line, max_x):
        ranges_start = []
        ranges_end = {}
        for r in self.rauten:
            if y_line >= r.bottom.y and y_line <= r.top.y:
                #print(r.sensor.x, r.sensor.y)
                dist = abs(r.sensor.y - y_line) 
                start_x = r.sensor.x - (r.distance - dist)
                end_x = r.sensor.x + (r.distance - dist)
                ranges_start.append(start_x)
                try:
                    test = ranges_end[start_x]
                    if end_x > test:
                        ranges_end[start_x] = end_x
                except:
                    ranges_end[start_x] = end_x

        ranges_start.sort()

        current_start = ranges_start[0]
        current_end = ranges_end[ranges_start[0]]

        for r in ranges_start:
            if r <= current_end:
                end = ranges_end[r]
                if end > current_end:
                    current_end = end
                if end > max_x:
                    break
            else:
                break

        if current_start <= 0 and current_end >= max_x:
            return False
        else:
            self.empty_point.x = current_end + 1
            self.empty_point.y = y_line
            return True


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

for l in range(0, 4000000+1):
    #print(round(l))
    if field.checkLine(l, 4000000):
        break
frequency = field.empty_point.x * 4000000 + field.empty_point.y
print (frequency)




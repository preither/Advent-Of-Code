class Num:
    def __init__(self, name, operation):
        self.name = name
        self.operation = operation
        self.observer = []
        self.val = ""
        #self.observe = []
        pass

    def add_observer(self, observer):
        self.observer.append(observer)

    def set_value(self, val):
        self.val = str(val)
        for ob in self.observer:
            ob.notify(self.name, self.val)

    def notify(self, name, val):
        self.operation = self.operation.replace(name, val)
        try:
            self.set_value(eval(self.operation))
        except:
            pass

f = open('input.txt', 'r')
lines = f.readlines()

dic = {}

for l in lines:
    cut = l[:-1].split(": ")
    dic[cut[0]] = Num(cut[0], cut[1])

for key in dic:
    obj = dic[key]
    if not obj.operation.isnumeric():
        cut = obj.operation.split(" ")

        dic[cut[0]].add_observer(obj)
        dic[cut[2]].add_observer(obj)

for key in dic:
    obj = dic[key]
    if obj.operation.isnumeric():
        obj.set_value(obj.operation)

print(dic["root"].val)

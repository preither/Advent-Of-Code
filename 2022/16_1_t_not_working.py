import networkx as nx
import itertools

f = open('test.txt', 'r')
lines = f.readlines()

flow_rates = {}
active_valves = []

G = nx.Graph()

for l in lines:
    cut = l[:-1].split(" ")
    valve = cut[1]
    rate = cut[4].split("=")[1][:-1]
    flow_rates[valve] = int(rate)

    if int(rate) > 0:
        active_valves.append(valve)

    lead = []
    for i in range(9, len(cut)):
        G.add_edge(valve, cut[i].split(",")[0])

pos = "AA"
s = 0

cnt = 1
for i in range(30):
    paths = nx.shortest_path_length(G, source = pos)
    max_points = 0
    next_valve = ""
    for a in active_valves:
        points = (30 - cnt - paths[a]) * flow_rates[a]
        if points > max_points:
            max_points = points
            next_valve = a

    print(pos + " -> " + next_valve)
    print(max_points)
    
    if next_valve != "":
        cnt += paths[next_valve] + 1
        s += max_points
        pos = next_valve
        active_valves.remove(next_valve)
    else:
        break


print(s)

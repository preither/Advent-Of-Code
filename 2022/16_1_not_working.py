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

print(len(active_valves))
comb = list(itertools.permutations(active_valves, len(active_valves)))
max_points = 0
for l in comb:
    s = 0
    pos = "AA"
    cnt = 1
    #print(l)
    for valve in l:
        path = nx.shortest_path_length(G, source = pos, target=valve)
        points = (30 - cnt - path) * flow_rates[valve]
        cnt += path + 1
        s += points
        pos = valve
    if s > max_points:
        max_points = s

print(max_points)

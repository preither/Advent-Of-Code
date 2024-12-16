from enum import Enum
import copy

def check_field(map, already_checked, position, field_to_check):
    max_height = len(map) - 1
    max_width = len(map[0]) - 2

    if field_to_check[0] < 0 or field_to_check[0] > max_height or field_to_check[1] < 0 or field_to_check[1] > max_width:
        return False
    
    if field_to_check in already_checked:
        return False 
    
    if map[field_to_check[0]][field_to_check[1]] == map[position[0]][position[1]]:
        return True
    
    return False

class Direction(Enum):
    RIGHT = 0
    LEFT = 1
    DOWN = 2
    UP = 3

class Node():
    dist = -1
    prev = []
    

with open('input.txt') as f:
    contents = f.readlines()


directions = [(0, 1),(0, -1),(1, 0),(-1, 0)]
unvisited_nodes = {}
deleted_nodes = {}
target = ()
path_nodes = []
start = ()


cnt = 0
for y in range(len(contents)):
    for x in range(len(contents[0][:-1])):
        if contents[y][x] == "." or contents[y][x] == "E":
            for d in Direction:
                unvisited_nodes[(y,x,d)] = Node()
                unvisited_nodes[(y,x,d)].prev = []
            if contents[y][x] == "E":
                target = (y, x)
        elif contents[y][x] == "S":
            unvisited_nodes[(y,x,Direction.RIGHT)] = Node()
            unvisited_nodes[(y,x,Direction.RIGHT)].dist = 0
            start = (y,x)

while len(unvisited_nodes) > 0:
    #search lowest dist
    lowest_node = ()
    lowest_val = -1
    for key in unvisited_nodes:
        if unvisited_nodes[key].dist >= 0:
            if unvisited_nodes[key].dist < lowest_val or lowest_val == -1:
                lowest_node = key
                lowest_val = unvisited_nodes[key].dist

    if lowest_val == -1:
        break

    if lowest_node[0] == target[0] and lowest_node[1] == target[1]:
        nodes_cur = unvisited_nodes[lowest_node].prev
        while len(nodes_cur) > 0:
            next_nodes = []
            for nodes_ in nodes_cur:
                for n in deleted_nodes[nodes_].prev:
                    point = (n[0], n[1])
                    if point[0] == start:
                        continue
                    elif point not in path_nodes:
                        path_nodes.append(point)
                    next_nodes.append(n)
                nodes_cur = next_nodes

        print(len(path_nodes) + 2)
        break

    for d in Direction:
        new_pos = (lowest_node[0] + directions[d.value][0], lowest_node[1] + directions[d.value][1], d)
        if new_pos in unvisited_nodes:
            edge_cost = 1
            if lowest_node[2] != d:
                edge_cost = 1001
            new_distance = unvisited_nodes[lowest_node].dist + edge_cost

            if new_distance <= unvisited_nodes[new_pos].dist or unvisited_nodes[new_pos].dist == -1:
                unvisited_nodes[new_pos].dist = new_distance
                unvisited_nodes[new_pos].prev.append(lowest_node)

    deleted_nodes[lowest_node] = Node()
    deleted_nodes[lowest_node].prev = copy.deepcopy(unvisited_nodes[lowest_node].prev)
    del unvisited_nodes[lowest_node]


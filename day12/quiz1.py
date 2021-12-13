import sys

input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]

graph = {}

for x in data:
    node1, node2 = x.split("-")
    if node1 not in graph:
        graph[node1] = [node2]
    else:
        graph[node1].append(node2)

    if node2 not in graph:
        graph[node2] = [node1]
    else:
        graph[node2].append(node1)

paths = [[]]


def dfs(graph, current_vertex, visited):
    visited.append(current_vertex)
    for vertex in graph[current_vertex]:
        if vertex not in visited or not vertex.islower():
            dfs(graph, vertex, visited.copy())
    paths.append(visited)


dfs(graph, "start", [])

count = 0
for path in paths:
    if len(path) >= 2 and path[0] == "start" and path[-1] == "end":
        count += 1

print(count)

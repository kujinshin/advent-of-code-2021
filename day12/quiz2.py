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


def valid_path(path):
    start_count = 0
    end_count = 0
    for node in path:
        if node == "start":
            start_count += 1
        if node == "end":
            end_count += 1
    return start_count == 1 and end_count == 1


paths = [[]]


def dfs(graph, current_vertex, visited, visit_twice):
    if current_vertex.islower() and current_vertex in visited:
        visit_twice = False
    visited.append(current_vertex)
    for vertex in graph[current_vertex]:
        if vertex not in visited or not vertex.islower() or visit_twice:
            dfs(graph, vertex, visited.copy(), visit_twice)
    paths.append(visited)


dfs(graph, "start", [], True)

count = 0
for path in paths:
    if len(path) >= 2 and path[0] == "start" and path[
            -1] == "end" and valid_path(path):
        count += 1

print(count)

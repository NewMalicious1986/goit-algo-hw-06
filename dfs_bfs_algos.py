import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'D')
G.add_edge('C', 'D')
G.add_edge('D', 'E')

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        for neighbor in set(graph.neighbors(node)) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            stack.append((neighbor, path + [neighbor]))
    return None

def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (node, path) = queue.popleft()
        for neighbor in set(graph.neighbors(node)) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            queue.append((neighbor, path + [neighbor]))
    return None

start, goal = 'A', 'E'
dfs_result = dfs_path(G, start, goal)
bfs_result = bfs_path(G, start, goal)

print("DFS path:", dfs_result)
print("BFS path:", bfs_result)

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()
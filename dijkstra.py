import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges_with_weights = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1),
    ('D', 'E', 3)
]

G.add_weighted_edges_from(edges_with_weights)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)
plt.title("Граф з вагами")
plt.show()

# Алгоритм Дейкстри
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    unvisited = set(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

shortest_paths = {}
for start_node in G.nodes():
    distances = dijkstra(G, start_node)
    for target_node, distance in distances.items():
        if start_node != target_node:
            shortest_paths[(start_node, target_node)] = distance

print("Shortest paths between all vertices in the graph:")
for (start, target), distance in shortest_paths.items():
    print(f"{start} -> {target}: distance {distance}")
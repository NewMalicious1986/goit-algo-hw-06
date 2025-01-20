import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'D')
G.add_edge('C', 'D')
G.add_edge('D', 'E')

num_nodes = G.number_of_nodes()  
num_edges = G.number_of_edges()  
degrees = dict(G.degree())       

print("Number of nodes:", num_nodes)
print("Number of edges:", num_edges)
print("Node degrees:")
for node, degree in degrees.items():
    print(f"  Node {node}: {degree}")

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

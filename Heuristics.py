import networkx as nx
G = nx.Graph()
G.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'F'),
    ('D', 'G'),
    ('E', 'G'),
    ('F', 'G')
])
heuristic = {
    'A': 7,
    'B': 5,
    'C': 3,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}
nx.set_node_attributes(G, heuristic, 'heuristic')
print(G.nodes(data=True))
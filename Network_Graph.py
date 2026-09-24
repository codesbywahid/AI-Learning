import networkx as nx
import matplotlib.pyplot as plt
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
pos = {
    'A': (0, 3),
    'B': (-1, 2),
    'C': (1, 2),
    'D': (-1.5, 1),
    'E': (-0.5, 1),
    'F': (1, 1) ,
    'G': (0, 0)}
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1800,
    font_size=12
    )
plt.show()
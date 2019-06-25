import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import itertools

# create a large, random graph with distinct labels
G = nx.Graph()
nodes = ["".join(x) for x in itertools.product("ABCD", repeat=3)]
for i in range(0, len(nodes)):
    for j in range(i + 1, len(nodes)):
        if random.randint(0, math.ceil(len(nodes) / 4)) == 0:
            G.add_edge(nodes[i], nodes[j], weight=random.randint(1, 10))


# draw
pos = nx.spring_layout(G)
nx.drawing.nx_pylab.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()


import matplotlib.pyplot as plt
import networkx as nx
import random


'''
We are creating a random spanning tree of the graph G, 
and randomly remove one of it's edges, breaking it into two components.
Returning the spanning tree, if we call again the function using the previous result
we continue splitting the graph into further pieces 3,4,5 etc 
'''
def create_connected_component(G):
    T = nx.minimum_spanning_tree(G)
    print('Starting number of connected components is now: {}'.format(nx.number_connected_components(T)))
    edges = list(T.edges(data=True))
    x, y, _ = random.choice(edges)
    T.remove_edge(x, y)
    print('Number of connected components is now: {}'.format(nx.number_connected_components(T)))
    return T
#
#
G = nx.complete_graph(20)
nx.draw(G)
plt.draw()
plt.show()

G2 = create_connected_component(G)
G3 = create_connected_component(G2)
plt.figure()
# Final graph 
nx.draw_networkx(G3, with_labels=False)
plt.show()

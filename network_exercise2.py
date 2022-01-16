import networkx as nx
import matplotlib.pyplot as plt
# creating a small-world graph using watt-strogatz graph function generator
plot1 = plt.figure(1)
G1 = nx.watts_strogatz_graph(n=30, k=12, p=0.5)
pos = nx.circular_layout(G1)
nx.draw_networkx(G1, pos)
plt.draw()
# creating a scale-free graph using barabasi-albert graph function generator
plot2 = plt.figure(2)
G2= nx.barabasi_albert_graph(30,2)
nx.draw(G2, with_labels=True)
plt.draw()
plt.show()

# calculating betwenenness centrality for G1 and G2
betweenness_centrality_G1 = nx.betweenness_centrality(G1)
betweenness_centrality_G2 = nx.betweenness_centrality(G2)
# print results
print(betweenness_centrality_G1)
print(betweenness_centrality_G2)
# calculating degrees for G1 and G2
degrees_G1 = {node:val for (node, val) in G1.degree()}
degrees_G2 = {node:val for (node, val) in G2.degree()}
# printing results
print(degrees_G1)
print(degrees_G2)

# creating plots to compare those values
plot1 = plt.figure(1)
#plot1.legend(['1','2'])

myList1 = degrees_G1.items()
myList1 = sorted(myList1)
x1, y1 = zip(*myList1)
plt.plot(x1, y1,'-b',label="Watts-Strogatz")

myList2 = degrees_G2.items()
myList2 = sorted(myList2)
x2, y2 = zip(*myList2)

plt.plot(x2, y2,"-r", label="Barabasi-Albert")
plt.title('Degree Comparison')
plt.legend()
plt.show()

plot2 = plt.figure(2)
myList1 = betweenness_centrality_G1.items()
myList1 = sorted(myList1)
x1, y1 = zip(*myList1)
plt.plot(x1, y1,"-b", label="Watts-Strogatz")

myList2 = betweenness_centrality_G2.items()
myList2 = sorted(myList2)
x2, y2 = zip(*myList2)

plt.plot(x2, y2,"-r", label="Barabasi-Albert")
plt.legend()
plt.title('Betweenness Centrality Comparison')
plt.show()

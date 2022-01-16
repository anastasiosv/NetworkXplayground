import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

file = './ppi_matrix.xlsx'
file2 = './ppi_names.xlsx'

# read excel file to generate labels
df_names = pd.read_excel(
    file2,
    header=None,
    index_col=None
)
# creating headers reading with the data from excel
headers = []
for elem in df_names.values.tolist():
    headers.append(elem[0])
# reading excel and assigning labels from the other file
df = pd.read_excel(
    file,
    index_col=None,
    header=None,
    names=headers
    )
# setting index to be headers
df.index=headers
# Creating the graph from pandas
# this function reads a dataframe from Pandas and creates a graph according the its values
G = nx.from_pandas_adjacency(df)
# setting name of the Graph
G.name = "Graph from PPI matrix"
# printing general info of the graph like number of nodes and number of edges
print(nx.info(G))
# drawing the graph to a plot
nx.draw(G)
plt.draw()
# showing plot
plt.show()
# setting A as the adjacency matrix just of our data
A = nx.adjacency_matrix(G)
dfA = pd.DataFrame(data=A.todense())
# printing the matrix
print(dfA)
# creating two dictionaries for degrees and centralities
rankings = dict()
centrality = dict()
# having searched on the https://www.ncbi.nlm.nih.gov/gene/ I have found and mapped the ids with the names of the genes
ppi_nam={
    351:'APP',
    207:'AKT1',
    154:'ADRB2',
    335:'APOA1',
    25:'ABL1',
    60:'ACTB',
    408:'ARRB1'
}
# searching through the names of the Graphs as these are the keys I can find the degree and centrality of its one of them
for key in df_names.values:
    # checking if the key exists in my ppi_nam dictionary (First time of execution didn't include this feature, as we couldn't know if those are the values)
    # another way to retrieve this information is through web scrapping using python but I didn't use it in our exercise

    if key[0] in ppi_nam.keys():
        rankings[ppi_nam[key[0]]]=G.degree[key[0]]
    else:
        rankings[key[0]] = G.degree[key[0]]

# calculating betweenness centrality for our graph
betweenness_centrality = nx.betweenness_centrality(G)
# using Counter and a dictionary to keep the 5 most common of them
print('=== Degree Top 5 ===')
print(dict(Counter(rankings).most_common(5)))
# the same applies to betweenness centrality
c = dict(Counter(betweenness_centrality).most_common(5))
# checking with the keys and if exists print(ppi_name) with the value
print('=== Betweenness Centrality Top 5 ===')
for key in c:
    if key in ppi_nam.keys():
        print(ppi_nam[key], c[key])
    else:
        print(key,c[key])

#degree, betweenness, top5 values


# Number of connected components for Graph G
print('Number of connected components for Graph G is: {}'.format(nx.number_connected_components(G)))


# S contains a copy of the connected components of Graph G
S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
# NumOfNodes contains a dictionary of the number of nodes of each subgraph
NumOfNodes = dict()
for c in nx.connected_components(G):
    NumOfNodes[G.subgraph(c).copy()] = G.subgraph(c).copy().number_of_nodes()
# print S and NumOfNodes so we can see the outcome
print('List with copy of connected components for Graph G: {}'.format(S))
print('Number of nodes in every connected components of Graph G is: {}'.format(NumOfNodes.values()))

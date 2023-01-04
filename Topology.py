import random
import networkx as nx
import matplotlib.pyplot as plt

# Initialize the graph
G = nx.Graph()

# Initialize the arrays
a1 = [i for i in range(1, 99)]
a2 = []
a3 = ['s', 'd']
a4 = []
a5 = []
a6 = []

# Repeat until all numbers are in a6
while a1 or a2 or a3 or a4 or a5:
    # Generate two random numbers from the current array
    if a1:
        message = 'a1'
        array = a1
    elif a2:
        message = 'a2'
        array = a2
    elif a3:
        message = 'a3'
        array = a3
    elif a4:
        message = 'a4'
        plt.show()
        array = a4
    else:
        message = 'a5'
        array = a5
    if not array:
        continue
    index1 = random.randint(0, len(array) - 1)
    index2 = random.randint(0, len(array) - 1)
    if index1 == index2:
        continue
    # Add the two numbers to the graph
    num1 = array[index1]
    num2 = array[index2]
    num1_weight = random.randint(6, 9)
    num2_weight = random.randint(6, 9)
    if G.has_edge(num1, num2):
        # Skip adding the edge if it already exists
        continue
    elif (num1 == 's' and num2 == 'd') or (num1 == 'd' and num2 == 's'):
        # Skip adding the edge if it is between s and d
        continue
    # elif (num1 == 's' or num2 == 's') and G.has_node('d') and G.has_node('s'):
    #     path_length = nx.shortest_path_length(G, 's', 'd', weight='weight', method='dijkstra')
    #     if path_length < 70:
    #         continue
    # elif (num1 == 'd' or num2 == 'd') and G.has_node('s') and G.has_node('d'):
    #     path_length = nx.shortest_path_length(G, 's', 'd', weight='weight', method='dijkstra')
    #     if path_length < 70:
    #         continue
    # to Add the nodes and edges to the graph
    G.add_node(num1, connections=5, weight=num1_weight)
    G.add_node(num2, connections=5, weight=num2_weight)
    G.add_edge(num1, num2, weight=(num1_weight + num2_weight) / 2)

    # Remove the numbers from the current array and add them to the next array

    if a1:
        a2.append(num1)
        a2.append(num2)
    elif a2:
        a3.append(num1)
        a3.append(num2)
    elif a3:
        a4.append(num1)
        a4.append(num2)
    elif a4:
        a5.append(num1)
        a5.append(num2)
    else:
        a6.append(num1)
        a6.append(num2)
    array.pop(index1)
    if index1 < index2:
        index2 -= 1
    array.pop(index2)

    # print(message, array)
    # nx.draw(G, with_labels=True)
    # plt.show()
# Initialize the counts dictionary
counts = {}

# Create a list with the node colors
node_colors = []

# Iterate over the nodes of the graph
for node in G.nodes():

    if node in ['s', 'd']:
        node_colors.append('red')
    else:
        node_colors.append('lightblue')

    # Get the degree of the node
    degree = G.degree(node)

    # Increment the count for the degree
    if degree not in counts:
        counts[degree] = 0
    counts[degree] += 1
print(counts)


# Calculate all possible paths
# paths = nx.all_simple_paths(G, 's', 'd')
# print(list(paths))
# print(paths)
Shortest = nx.shortest_path(G, 's', 'd', weight='weight', method='dijkstra')
edge_list = [(Shortest[i], Shortest[i + 1]) for i in range(len(Shortest) - 1)]
layout = nx.spring_layout(G, pos={'s': (0, 0.5), 'd': (1, 0.5)}, fixed=['s', 'd'])
path_length = nx.shortest_path_length(G, 's', 'd', weight='weight', method='dijkstra')
print("path_length: ", path_length)


nx.draw(G, with_labels=True, node_color=node_colors, edge_color='lightgreen', width=1, linewidths=1, pos=layout)
nx.draw_networkx_edges(G, pos=layout, edgelist=edge_list, edge_color='r', width=2)
nx.draw_networkx_nodes(G, pos=layout, nodelist=Shortest, node_color='r')

# also draw weights of edges on the graph
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=edge_labels, font_size=5)
plt.show()

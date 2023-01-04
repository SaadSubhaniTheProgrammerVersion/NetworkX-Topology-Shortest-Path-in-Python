import networkx as nx
import matplotlib.pyplot as plt
from random import randint

G=nx.Graph()

edges={}
color_map = []
timers=[]
time_delay=[]
hops=[]

for iterations in range(0,20):
    G.clear()

    for u in range(0,98):
        G.add_node(u,weight=randint(6,9))

    G.add_node('s',weight=randint(6,9))#source
    G.add_node('d',weight=randint(6,9))#


    for v in range(0,3):
        random=randint(0,97)
        weight1=G.nodes[v]["weight"]
        weight2=G.nodes[random]["weight"]
        average=(weight1+weight2)/2
        G.add_edge('s',random,weight=average)

    for v in range(0,3):

        random=randint(0,97)
        weight1=G.nodes[v]["weight"]
        weight2=G.nodes[random]["weight"]
        average=(weight1+weight2)/2
        G.add_edge('d',random)

    for u in range(0,98):
        for v in range(0,5):
            random=randint(0,97)
            if random!=u:
                weight1=G.nodes[u]["weight"]
                weight2=G.nodes[random]["weight"]
                average=(weight1+weight2)/2
                if(G.degree(u)<5 and G.degree(random)<5):
                    G.add_edge(u,random,weight=average)


            
    for node in G.nodes():
        if node=='s' or node=='d':
            color_map.append('red')
        else:
            color_map.append('lightblue')

    # print(G.nodes.data())

    # print(G.edges.data())
    # print("Bad nodes are: ",bad_nodes)
    Shortest=nx.shortest_path(G,'s','d',weight='weight',method='dijkstra')
    edgelist = [(Shortest[i], Shortest[i+1]) for i in range(len(Shortest)-1)]

    # print(edgelist)

    # layout = nx.spring_layout(G,pos={'s':(0,0.5),'d':(1,0.5)},fixed=['s','d'])
    # nx.draw(G,with_labels=True,node_color=color_map,edge_color='lightgreen',width=1,linewidths=1,pos=layout)
    # nx.draw_networkx_edges(G, pos=layout, edgelist=edgelist, edge_color='r', width=2)
    # nx.draw_networkx_nodes(G, pos=layout, nodelist=Shortest, node_color='r')
    # plt.show()

    time_delay.clear()
    for i in range(0,(len(edgelist)-1)):
        time_delay.append(G.edges[edgelist[i]]['weight'])

    total=0
    for values in time_delay:
        total=sum(time_delay)

    print("Time delay for iteration number",iterations, "is: ",total,"ms")
    print("Number of Hops for iteration number",iterations, "is: ", len(Shortest)-1)
    hops.append(len(Shortest)-1)
    timers.append(total)

for values in timers:
    FINAL=sum(timers)/len(timers)

for overs in hops:
    OVERHEAD=sum(hops)/len(hops)


print("\n\nThe average time delay for 20 ITERATIONS is: ",FINAL,"ms")
print("The overhead for 20 packets transmission is: ",OVERHEAD,"hops/packet")

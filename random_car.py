import networkx as nx
from Graph import nx_Graph
import random


def random_car(G="", count=0, seed=False, same_source=1, same_dest=1):

    count += 1

    # print("count: ", count)

    if seed:
        random.seed(count)

    if G == "":
        G = nx_Graph()
    nodes = list(G.nodes())

    if same_source:
        start = nodes[2]
    else:
        start = random.choice(nodes[0:5])


    # subgraph_start = nx.ego_graph(G, nodes[0], radius=500, center=True)
    # subgraph_end = nx.ego_graph(G, nodes[-1], radius=500, center=True)
    #
    # start_nodes_list = list(subgraph_start.nodes())
    # end_nodes_list = list(subgraph_end.nodes())

    end_nodes = list(nx.shortest_path(G, start))

    if same_dest:
        end = end_nodes[-1]
    else:
        end = random.choice(end_nodes[0:5])



    # end = random.choice(end_nodes[10:20])



    while end == start:
        end = random.choice(nodes)


    try:
        nx.dijkstra_path(G, start, end, weight='edge_length_file')

    except nx.NetworkXNoPath:
        print("unholy nodes found!: ")
        print("u: ", start, "  |  v: ", end)

        return random_car(G="", count=count+1, seed=True)


    # print("START | END", start, end)


    return start, end

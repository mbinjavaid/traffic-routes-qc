import networkx as nx
from Graph import nx_Graph
# import matplotlib.pyplot as plt
# from random_car import random_car

# G = nx_Graph()
#
# start, end = random_car(G)



def shortest_path_networkx(u, v, G="", starting_nodes_csv_file="", ending_nodes_csv_file="", edge_length_file="", display=False):
    if G == "":
        G = nx_Graph(starting_nodes_csv_file, ending_nodes_csv_file, edge_length_file, display)

    # print("u: ", u)
    # print("v: ", v)

    r = nx.dijkstra_path(G, u, v, weight='edge_length_file')

    # print("networkx DJ: \n", r)

    return r

# print(shortest_path_networkx(start, end, G))

import numpy as np
import csv
import matplotlib.pyplot as plt
import networkx as nx
import random


def load_osmnx_files(starting_nodes_csv_file="", ending_nodes_csv_file="", edge_length_file = "", speeds_file=""):
    """This function loads the starting_nodes and ending_nodes from OSMnx data files and returns them."""

    try:
        starting_nodes_csv = np.loadtxt(starting_nodes_csv_file)
        ending_nodes_csv = np.loadtxt(ending_nodes_csv_file)
        edge_length_csv = np.loadtxt(edge_length_file)
        speeds_csv = np.loadtxt(speeds_file)

    except (FileNotFoundError, IOError):
        print("starting_nodes or ending_nodes or length csv files not found.")
        print("Checking in default directory: osmnx...")

        try:
            starting_nodes_csv = np.loadtxt('osmnx/starting_nodes.csv')
            ending_nodes_csv = np.loadtxt('osmnx/ending_nodes.csv')
            edge_length_csv = np.loadtxt('osmnx/lengths_of_edges.csv')
            speeds_csv = np.loadtxt('osmnx/speeds.csv')

        except (FileNotFoundError, IOError):
            print("Files not found in default directory: osmnx")
            print("Try again with the starting_nodes and ending_nodes and length csv files")
            starting_nodes_csv = ""
            ending_nodes_csv = ""
            edge_length_csv = ""
            speeds_csv = ""

    return starting_nodes_csv, ending_nodes_csv, edge_length_csv, speeds_csv


def graph(starting_nodes_csv_file="", ending_nodes_csv_file="", edge_length_file = "", speeds_file="", csv_export = False):
    """This function takes the starting_nodes and ending_nodes location, loads them and returns the dictionary of graph
    in the form of nodes."""

    starting_nodes_csv, ending_nodes_csv, edge_length_csv, speeds_csv = load_osmnx_files(starting_nodes_csv_file,
                                                                             ending_nodes_csv_file, edge_length_file, speeds_file)

    starting_nodes = [0]
    ending_nodes = []

    for i in range(len(starting_nodes_csv)):

        if starting_nodes[-1] != starting_nodes_csv[i]:
            starting_nodes.append(starting_nodes_csv[i])
            ending_nodes.append([ending_nodes_csv[i]])
            continue

        ending_nodes[-1].append(ending_nodes_csv[i])

    starting_nodes.remove(0)

    ox_graph = dict(zip(starting_nodes, ending_nodes))

    if csv_export:
        with open('csv files/graph.csv', 'w') as f:
            w = csv.writer(f)
            w.writerows(ox_graph.items())
        print("graph.csv file created")

    return ox_graph


def nx_Graph(starting_nodes_csv_file="", ending_nodes_csv_file="", edge_length_file="", speeds_file="", display=False):
    """This function takes the starting_nodes and ending_nodes location, loads them and returns the graph in the
    networkx format."""

    starting_nodes_csv, ending_nodes_csv, edge_length_csv, speeds_csv = load_osmnx_files(starting_nodes_csv_file,
                                                                             ending_nodes_csv_file, edge_length_file, speeds_file)

    G = nx.DiGraph()

    # adding nodes
    G.add_nodes_from(starting_nodes_csv)

    # adding edges
    for i in range(len(starting_nodes_csv)):
        if display:
            print("Graph Data:")
            print("start: ", starting_nodes_csv[i], " end: ", ending_nodes_csv[i], " weight: ", edge_length_csv[i])
            print()
        G.add_edge(starting_nodes_csv[i], ending_nodes_csv[i], weight=edge_length_csv[i], speed=random_speed_gen(speeds_csv[i]))

    # showing graph if display is True
    if display:
        pos = nx.spring_layout(G)
        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=200)

        # edges
        nx.draw_networkx_edges(G, pos,
                               width=6)
        nx.draw_networkx_edges(G, pos,
                               width=6, alpha=0.5, edge_color='b', style='dashed')

        # labels
        nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')

        plt.axis('off')
        plt.show()

    return G

# nx_Graph(display=True)


def random_speed_gen(speed, min_speed=30, max_speed=60, seed_no = 1):

    if seed_no != 0:
        random.seed(seed_no)

    if np.isnan(speed):
        speed = 10 * random.randint(min_speed/10, max_speed/10)

    return speed
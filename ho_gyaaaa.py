# from all_paths import find_all_paths, find_all_paths_networkx
# from shortest_path_networkx import shortest_path_networkx
# import networkx as nx
import numpy as np
# from three_routes_all_cars import three_routes_all_cars
from three_routes_all_cars import r_routes_all_cars
from Graph import nx_Graph, graph
from Q import QConstructor
from QBSolv import Q_dict, QBSolve_classical_solution, selection_rules, routes_from_selection_rule, best_nodes, QBSolve_QC_solution
from nodes_segments_Dict import segments_to_nodes_dict, nodes_to_segment_dict
from Map_plotting import nodes_to_xy_dict as nxy
# from Map_plotting import Flat_Earth as fe
# from random_car import random_car
# from all_paths_dijkstra import nearby_nodes, mid_dijkstra, start_dijkstra, glue
from overlap_count import overlap_count
# from Map_plotting import Flat_Earth_2 as fe2
# from matplotlib import pyplot as plt
# import pickle
# import random
import folium
# from folium.plugins import HeatMap
# import tkinter as tk
import time
from heatmap import heatmap_list, color_from_count_list



def main(n, r, loc, same_source, same_dest, qc):
    graph_ = graph("osmnx/"+loc+"/starting_nodes.csv", "osmnx/"+loc+"/ending_nodes.csv", "osmnx/"+loc+"/lengths_of_edges.csv")
    # print("graph: ", graph_)
    G = nx_Graph("osmnx/"+loc+"/starting_nodes.csv", "osmnx/"+loc+"/ending_nodes.csv", "osmnx/"+loc+"/lengths_of_edges.csv", display=False)


    # start, end = random_car(G, seed=True)

    short = False
    for i in range(2):

        if i == 1:
            short = True
            # print("huuu")

        root_function = r_routes_all_cars(G, graph_, n=n, seed=True, seed_id=0,
                                          short=short, r=r, same_source=same_source, same_dest=same_dest)  # n is the number of cars
        # r is the number of routes (3)

        root = root_function[0]
        # random_start_list = root_function[1][0]
        # random_end_list = root_function[1][1]

        # print("random_start_list: ", random_start_list)
        # print("random_end_list: ", random_end_list)

        print("root: ", root)
        Q = QConstructor(root, r=r)
        print("length of Q:", len(Q))

        Qdict = Q_dict(Q)
        print("length of Q_dict:", len(Qdict))
        print("Q_dict:", Qdict)

        QUBO_time_start = time.clock()

        if qc == False:

            QB_classical_result = QBSolve_classical_solution(Qdict)
            print("CC Output: ", QB_classical_result)
            print("CC Output: ", QB_classical_result)

        if qc == True and short == False:
            QB_classical_result = QBSolve_QC_solution(Qdict)
            print("QC Output: ", QB_classical_result)


        if qc == True and short == True:
            QB_classical_result = QBSolve_classical_solution(Qdict)
            print("CC Output: ", QB_classical_result)

        QUBO_time_end = time.clock()


        print("QB_classical_result: ", QB_classical_result)

        # print("rrr: ", r)
        selection_rules_ = selection_rules(QB_classical_result, r)
        print("selection rules: ", selection_rules_)

        best_routes = routes_from_selection_rule(root, selection_rules_)
        print("routes from selection rule", best_routes)

        best_length = 0
        for i in best_routes:
            best_length += len(i)

        print("overall lenght of best routes solution: ", best_length)

        hist_labels, overlap_count_ = overlap_count(best_routes)
        print("overLap: ", overlap_count_)

        std = np.std(overlap_count_)
        print("Standard Deviation: ", std)

        # importing dictionaries (ns and sn) to convert routes back to nodes
        ns_dict = nodes_to_segment_dict(graph_)
        sn_dict = segments_to_nodes_dict(ns_dict)
        print("sn_dict: ", sn_dict)
        # best_nodes_ = best_nodes(best_routes, sn_dict)
        # print("best_nodes: ", best_nodes_)

        # print(nxy.nodes_to_xy_dict())

        # nxy1 = nxy("osmnx/"+loc+"/osmid.csv", "osmnx/"+loc+"/x.csv", "osmnx/"+loc+"/y.csv")
        nxy1 = nxy(loc)

        big_heatmap_list = heatmap_list(best_routes, sn_dict, nxy1)

        heatmap_list_ = big_heatmap_list[0]

        count_list_ = big_heatmap_list[1]

        map_hooray = folium.Map(location=[33.5961, 73.0538], tiles='Stamen Toner')

        for k in range(len(heatmap_list_)):
            # # adding folium markers for start and end positions of cars
            # for i in range(len(random_start_list)):
            #     start_long_lat = list(nxy1[random_start_list[i]])
            #     folium.Marker(start_long_lat, popup='<s>start</s>', tooltip="start", icon=folium.Icon(color='green')).add_to(map_hooray)
            #
            #     end_long_lat = list(nxy1[random_end_list[i]])
            #     folium.Marker(end_long_lat, popup='<e>end</e>', tooltip="end", icon=folium.Icon(color='red')).add_to(map_hooray)

            folium.PolyLine(heatmap_list_[k], weight=11, color=color_from_count_list(count_list_[k], max(count_list_)),
                            opacity=10).add_to(map_hooray)

        # Display the map
        if short == True:
            map_hooray.save("heatmap_short.html")
        else:
            map_hooray.save("heatmap_opt.html")


        elapsed = QUBO_time_end - QUBO_time_start

    return elapsed


# main(30, 4, "NUST, Islamabad", 0, 0, 1)
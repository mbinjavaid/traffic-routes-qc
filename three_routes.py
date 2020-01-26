from nodes_segments_Dict import nodes_to_segment_dict
from shortest_path_networkx import shortest_path_networkx
# from all_paths import find_all_paths_networkx
# from random_car import random_car
import numpy as np
# import networkx as nx
# from all_paths_dijkstra import find_all_paths_dj
from all_paths import k_shortest_paths
# from Graph import graph, nx_Graph


# graph = graph()
# G = nx_Graph()
#
# start, end = random_car(G, True)
#
# shortest_path = shortest_path_networkx(start, end, G)
# # print("shortest path:\n", shortest_path)
# #
# ## car_paths = find_all_paths_networkx(G, start, end)
# ## print("all car paths\n", car_paths)
#
# ns_dict = nodes_to_segment_dict(graph)
# print("graph segments\n", ns_dict)


def find_all_paths_in_segments(ns_dict, car_paths):

    """This function takes in the dictionary relating nodes to segments called graph_segments as the first parameter
    and takes all the possible paths from one node to another called all_paths as the second parameter
    and outputs all the possible paths in the form of there segments.

    Input: all paths (between two nodes) in the form of nodes
    Output: all paths (between two nodes) in the form of segments
    """

    all_paths_segments = []
    one_path_segments = []

    # loops through all the paths
    for i in range(len(car_paths)):
        # loops through one of the path
        for j in range(0, len(car_paths[i]) - 1):
            one_path_segments.append(ns_dict[(car_paths[i][j], car_paths[i][j + 1])])
        all_paths_segments.append(one_path_segments)
        one_path_segments = []

    # all_paths_segments.sort(key = len)

    return all_paths_segments


# print(find_all_paths_in_segments(ns_dict, car_paths))


def intersection_length(list1, list2):
    return len(set(list1).intersection(list2))


def union_length(list1, list2):
    return len(list(set(list1) | set(list2)))


def diff_list(list1, list2):
    return list(set(list1).symmetric_difference(set(list2)))


def jack(all_paths_segments, lists):
    """Takes all route list in segments and takes a list
    and finds a path (in segments) that is maximally dissimilar between the two."""

    jack_list = []

    for i in all_paths_segments:
        jack_list.append(intersection_length(lists, i))

    arg_min_path = all_paths_segments[np.argmin(jack_list)]

    return arg_min_path


def three_paths(graph, G, start, end):

    # shortest_path = shortest_path_networkx(start, end, G)


    # finding the value of r by using 50pc of djkistra path lenght
    # r = 0.5*nx.dijkstra_path_length(G, start, end)

    # print("r: ", r)


    # all_car_paths = find_all_paths_dj(G, start, end, r)

    # find k number of paths between start and end, beginning with the shortest path.
    all_car_paths = k_shortest_paths(G, start, end, 50)

    # print("All car paths uhhhhhhh: ", len(all_car_paths))

    shortest_path = all_car_paths[0]

    # all_car_paths = find_all_paths_networkx(G, start, end)
    ns_dict = nodes_to_segment_dict(graph)

    all_car_paths_segments = find_all_paths_in_segments(ns_dict, all_car_paths)

    list1 = find_all_paths_in_segments(ns_dict, [shortest_path])[0]
    list2 = jack(all_car_paths_segments, list1)

    union_list = list2 + list1

    list3 = jack(all_car_paths_segments, union_list)

    return list1, list2, list3



def r_paths(graph, G, start, end, r=3):

    # shortest_path = shortest_path_networkx(start, end, G)


    # finding the value of r by using 50pc of djkistra path lenght
    # r = 0.5*nx.dijkstra_path_length(G, start, end)

    # print("r: ", r)


    # all_car_paths = find_all_paths_dj(G, start, end, r)

    # find k number of paths between start and end, beginning with the shortest path.

    # if r == 3:
    #     number_of_paths = 50
    # else:
    number_of_paths = 20 * r

    all_car_paths = k_shortest_paths(G, start, end, number_of_paths)

    # print("All car paths uhhhhhhh: ", len(all_car_paths))

    shortest_path = all_car_paths[0]

    # all_car_paths = find_all_paths_networkx(G, start, end)
    ns_dict = nodes_to_segment_dict(graph)

    all_car_paths_segments = find_all_paths_in_segments(ns_dict, all_car_paths)

    big_list = []

    list1 = find_all_paths_in_segments(ns_dict, [shortest_path])[0]
    list2 = jack(all_car_paths_segments, list1)

    big_list.append(list1)
    big_list.append(list2)

    for i in range(2, r):
        # union_list = list2 + list1
        union_list = [item for sublist in big_list for item in sublist]

        list3 = jack(all_car_paths_segments, union_list)

        big_list.append(list3)

    return big_list


def three_paths_same(graph, G, start, end):
    """This is a test! :))"""
    """Testing for all car there respective shortest path"""

    ns_dict = nodes_to_segment_dict(graph)
    shortest_path = shortest_path_networkx(start, end, G)

    list1 = find_all_paths_in_segments(ns_dict, [shortest_path])[0]

    return list1, list1, list1


def r_paths_same(graph, G, start, end, r=3):
    """This is a test! :))"""
    """Testing for all car there respective shortest path"""

    ns_dict = nodes_to_segment_dict(graph)
    shortest_path = shortest_path_networkx(start, end, G)

    list1 = find_all_paths_in_segments(ns_dict, [shortest_path])[0]

    big_list = []
    for i in range(r):
        big_list.append(list1)

    return big_list



# print("uuh", three_paths(graph, G, start, end))
# print("3:  ", three_paths_same(graph, G, start, end))
# print("r:  ", r_paths_same(graph, G, start, end))

# print("3:  ", three_paths(graph, G, start, end))
# print("r:  ", r_paths(graph, G, start, end, r=5))


# def three_routes_all_cars():
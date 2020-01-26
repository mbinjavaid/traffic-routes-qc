import networkx as nx
from shortest_path_networkx import shortest_path_networkx
import itertools
from Graph import nx_Graph
from random_car import random_car

G = nx_Graph()
# # u,v = random_car(G)


def is_connected(G, u, v):
    return v in list(nx.shortest_path(G, u))


# print(is_connected(G, 304489780.0, 304485897.0))



def nearby_nodes(G, start, end, r):
    # nx.ego_graph(G, node, radius=r, center=True)
    nearby_nodes_ = nx.single_source_shortest_path_length(G, source=start, cutoff = r)

    # print("r: ", r)
    # print("nearby_nodes_", nearby_nodes_)

    a = list(nearby_nodes_)

    a.pop(0)

    # print("before a: ", a)
    #
    # # length_a = len(a)
    #
    # for i in a:
    #
    #     try:
    #         shortest_path_networkx(i, end, G)
    #         # shortest_path_networkx(start, i, G)
    #
    #     except nx.NetworkXNoPath:
    #         b = a.pop(a.index(i))
    #         print("poppinguuuunnnggmuummm: ", b)
    #
    #
    #         # print("startuuh: ", start, "mid uuh: ", i, "enduuh: ", end)
    #
    # print("after a: ", a)


    trash_mids = []
    good_mids = []

    # print("a: ", a)
    for i in a:

        cond = is_connected(G, i, end)
        # print("cond uuh: ", cond)
        #
        # if not cond:
        #     print("in cond uuhhhh: ", i)
        #     a.remove(i)
        #     trash_mids.append(i)



        if cond:
            good_mids.append(i)


    # print("Trash mids", trash_mids)

    return good_mids


def mid_dijkstra(G, nearby_nodes_, start, end):
    """mid is a nearby point to starting point, and end is the final endpoint of the car
    Returns shortest paths from every one of the nearby nodes to the end"""

    # print("nearby_nodes uuhh in mid_dj: ", nearby_nodes_)

    big_mid_list = []



    for midu in nearby_nodes_:

        # print("midu: ", midu)

        big_mid_list.append(shortest_path_networkx(midu, end, G))

        # print("big_mid_list: ", big_mid_list)

    return big_mid_list

def start_dijkstra(G, start, nearby_nodes):
    """this function calls on dijkstra to find shortest paths from the start point to every mid point"""

    big_start_list = []

    for mid in nearby_nodes:
        big_start_list.append(shortest_path_networkx(start, mid, G))

    for i in big_start_list:
        i.pop(-1)

    return big_start_list


def glue(start_list, mid_list):

    glue_list = []

    for i in range(0, len(mid_list)):
        a = start_list[i] + mid_list[i]
        glue_list.append(a)

    return list(glue_list)


def find_all_paths_dj(G, start, end, r):
    nearby_nodes_ = nearby_nodes(G, start, end, r)

    # print("nearBY nodes: ", nearby_nodes_)

    start_dijkstra_ = start_dijkstra(G, start, nearby_nodes_)
    mid_dijkstra_ = mid_dijkstra(G, nearby_nodes_, start, end)


    glue_ = glue(start_dijkstra_, mid_dijkstra_)


    # print("length unsorted glue_: ", len(glue_[0]))
    glue_.sort(key=len)
    # print("sorted glue_         : ", len(glue_[0]))


    return glue_


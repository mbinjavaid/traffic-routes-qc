import networkx as nx
# from all_paths_dijkstra import glue
from itertools import islice


# def find_all_paths(graph, start, end, path=[]):
# #     """This function takes in the graph in the form of dictionary from one node to all the nodes it's linked to,
# #         starting and ending nodes as input
# #         and outputs all the possible paths from starting node to ending node in the from of nodes"""
# #
# #     path = path + [start]
# #     if start == end:
# #         return [path]
# #     if start not in graph:
# #         return []
# #     paths = []
# #     for node in graph[start]:
# #         if not node in path:
# #             # print("GOING IN")
# #             new_paths = find_all_paths(graph, node, end, path)
# #             for newpath in new_paths:
# #                 paths.append(newpath)
# #
# #                 if len(paths) >= 30:
# #                     break
# #             if len(paths) >= 30:
# #                 break
# #
# #     paths.sort(key=len)
# #     return paths


def find_all_paths_networkx(graph, start, end):
    print("findimg all paths")

    # for path in nx.all_simple_paths(graph, start, end, cutoff = 500):
    #     print("PATH: ", path)

    # all_paths = list(nx.all_simple_paths(graph, start, end, cutoff=100))


    # for path in nx.shortest_simple_paths(graph, start, end):
    #     print("PATH: ", path)

    all_paths = list(nx.shortest_simple_paths(graph, start, end))



    # print("findimg all paths 2")
    # sorting all_paths by the length
    """RIGHT NOW IT SORTS BY NUMBER OF NODES, NEED TO CHANGE TO SORT BY ACTUAL LENGTHS"""
    # all_paths.sort(key=len)

    # print("all_paths OLD: ", all_paths)

    return all_paths


def k_shortest_paths(G, source, target, k):
    """HOLY LINE"""
    return list(islice(nx.shortest_simple_paths(G, source, target), k))


# from Graph import graph
# import pandas as pd

def nodes_to_segment_dict(graph):
    """Returns a dictionary with KEYS: nodes and VALUES: segments"""

    key = []

    # this loop generates the key
    for i in graph:
        for j in graph[i]:
            key.append((i, j))

    ns_dict = {key[i]: i for i in range(len(key))}

    return ns_dict


def segments_to_nodes_dict(nodes_to_segment_dict):
    """Returns a dictionary with KEYS: segments and VALUES: nodes
    Inverting the above dictionary."""

    sn_dict = {v: k for k, v in nodes_to_segment_dict.items()}

    return sn_dict

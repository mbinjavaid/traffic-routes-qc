import numpy as np


def nodes_to_xy_dict(loc):

    """Makes a dict relating OSMid's for nodes to there (x,y) coordinates"""

    with open("osmnx/"+loc+"/osmid.csv", "r") as f:
        nodes = np.loadtxt(f)

    with open("osmnx/"+loc+"/x.csv", "r") as f:
        x = np.loadtxt(f)

    with open("osmnx/"+loc+"/y.csv", "r") as f:
        y = np.loadtxt(f)

    xy = list(zip(y, x))

    nodes_xy_dict = dict(zip(nodes, xy))

    return nodes_xy_dict

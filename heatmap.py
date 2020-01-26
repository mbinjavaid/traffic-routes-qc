from collections import Counter
import numpy as np
# import struct
from colour import Color
# import math

def segment_count_dict(best_routes):
    """This function takes the best routes list (in segments) i.e the routes chosen by selection rules
    and counts the number of times a segment shows up in that list.
    Note that it takes all the routes for all the cars."""

    # flattening the list of best routes
    flat_best_routes = [item for sublist in best_routes for item in sublist]

    # making a dictionary with keys as segment numbers and values as the number of time that segment shows up
    segment_count = dict(Counter(flat_best_routes))


    print("segment_count: ", segment_count)
    return segment_count


# best_routes = [[5, 10, 12, 13], [5, 11, 12], [5, 10, 12]]
#
# segment_count_dict_ = segment_count_dict(best_routes)
# print("segment_count: ", segment_count_dict_)


def GPS_sim_single(start_2d, end_2d, step, count):
    """This function takes in a starting point and ending point in terms of longitude and latitude and the number of
    time that segment appears in routes (count) for which the start and end pairs are given.
    It fills in the points as if a car moves straight between the two points, with count as the last element of every
    pair of xy."""

    start_x = start_2d[0]   # x coord of starting node
    start_y = start_2d[1]   # y coord of starting node

    end_x = end_2d[0]   # x coord of ending node
    end_y = end_2d[1]   # y coord of ending node


    if start_x > end_x:
        GPS_x = np.arange(start_x, end_x, -step)
    else:
        GPS_x = np.arange(start_x, end_x, step)


    GPS_y = np.linspace(start_y, end_y, len(GPS_x))

    count_list = [count] * len(GPS_x)

    # GPS_xy = list(zip(GPS_x, GPS_y, count_list))
    GPS_xy = list(zip(GPS_x, GPS_y))

    return GPS_xy


# GPS1 = GPS_sim_single((20,0), (0,10), 0.0005, 5)
# print("GPS_sim_single: ", GPS1)


def xy_coord_count_dict(segment_count_dict, sn_dict, n_xy_dict):
    """This function takes in:
    segment_count_dict that relates segments of graph with the number od times they appears (their count)
    sn_dict that relates segments of a graph to two nodes (starting and ending nodes)
    n_xy_dict that relates one node with its x and y coordinates (in tuple form)

    and it returns a dictionary with keys as a pair of xy_tuples [(start_x, start_y), (end_x, end_y)] with the count of
    the segment to which the pair of tuples relates."""


    segment_list = list(segment_count_dict.keys())
    count_list = list(segment_count_dict.values())

    xy_coord_pair_list = []

    for segment in segment_list:
        node_pair = sn_dict[segment]

        start_node = node_pair[0]
        end_node = node_pair[1]

        xy_coord_pair_start = n_xy_dict[start_node]
        xy_coord_pair_end = n_xy_dict[end_node]

        xy_coord_pair_list.append((xy_coord_pair_start, xy_coord_pair_end))

    xy_coord_count_dict_ = dict(zip(xy_coord_pair_list, count_list))

    return xy_coord_count_dict_


# sn_dict = {5: (100, 101), 10: (102, 103), 11: (104, 105), 12: (106, 107), 13: (108, 109)}
# n_xy_dict = {100: (1001, 1002), 101: (1003, 1004), 102: (1005, 1006), 103: (1007, 1008), 104: (1009, 1010),
#              105: (1011, 1012), 106: (1013, 1014), 107: (1015, 1016), 108: (1017, 1018), 109: (1019, 1020)}

# xy_coord_count_dict_ = xy_coord_count_dict(segment_count_dict_, sn_dict, n_xy_dict)
# print("xy_coord_count_dict: ", xy_coord_count_dict_)


def heatmap_list(best_routes, sn_dict, n_xy_dict, step=0.000005):
    segment_count_dict_ = segment_count_dict(best_routes)
    xy_coord_count_dict_ = xy_coord_count_dict(segment_count_dict_, sn_dict, n_xy_dict)

    heatmap_list_ = []
    count_list = []

    for xy_pair in xy_coord_count_dict_:
        start_2d = xy_pair[0]
        end_2d = xy_pair[1]
        count = xy_coord_count_dict_[xy_pair]

        GPS_sim_single_ = GPS_sim_single(start_2d, end_2d, step, count)
        heatmap_list_.append(GPS_sim_single_)
        count_list.append(count)

    return heatmap_list_, count_list


def color_from_count_list(count, maximum):
    """Min is the count at which blue starts
    Max is the count at which red starts"""


    # maximum = max(count_list)

    # green = Color("green")
    green = Color("#98FB98")
    colors_1 = list(green.range_to(Color("red"), maximum+1))
    # colors = [color.rgb for color in colors]
    colors_1 = [str(color) for color in colors_1]

    # red = Color("red")
    # colors_2 = list(red.range_to(Color("black"), math.ceil(n)))
    #
    # colors_2 = [str(color) for color in colors_2]
    #
    # # colors_2.pop[0]
    #
    # colors = colors_1 + colors_2

    # if count >= n/20:
    #     # count = int(math.floor(n/2))
    #     return "red"
    # else:
    return colors_1[count]





    # if count >= min and count <= max/5:
    #    return "blue"
    #
    # if count > max/5 and count <= 2*(max/5):
    #     return "lime"
    #
    # if count > 2*(max/5) and count <= 3*(max/5):
    #     return "yellow"
    #
    # if count > 3*(max/5) and count <= 4*(max/5):
    #     return "orange"
    #
    # if count > 4*(max/5) and count <= max:
    #     return "red"






# heatmap_list_ = heatmap_list(best_routes, sn_dict, n_xy_dict, step=0.05)
# print("heatmap_list: ", heatmap_list_)
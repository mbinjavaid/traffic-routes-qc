from three_routes import three_paths, three_paths_same
from three_routes import r_paths, r_paths_same
# from Graph import nx_Graph, graph
from random_car import random_car
# import numpy
import pandas as pd

# from Graph import graph, nx_Graph


# graph = graph()
# G = nx_Graph()


def three_routes_all_cars(G, graph, n, seed=False, short=False, seed_id=0):
    # n = number_of_cars

    big_three_paths_of_a_car = []

    big_export_list = []


    if short:

        for i in range(n):
            start, end = random_car(G, i + seed_id, seed)

            three_paths_of_a_car = list(three_paths_same(graph, G, start, end))

            # exporting the three routes for each car to a csv file
            export_list = [i, start, end, three_paths_of_a_car]
            big_export_list.append(export_list)

            big_three_paths_of_a_car.append(three_paths_of_a_car)

        route_dict = {j: big_three_paths_of_a_car[j] for j in range(n)}


    else:

        for i in range(n):

            start, end = random_car(G, i+seed_id, seed)

            three_paths_of_a_car = list(three_paths(graph, G, start, end))

            # exporting the three routes for each car to a csv file
            export_list = [i, start, end, three_paths_of_a_car]
            big_export_list.append(export_list)

            big_three_paths_of_a_car.append(three_paths_of_a_car)

        route_dict = {j: big_three_paths_of_a_car[j] for j in range(n)}



    # for i in range(n):
    #
    #     start, end = random_car(G, i+seed_id, seed)
    #     three_paths_of_a_car = list(three_paths(graph, G, start, end))
    #
    #     # exporting the three routes for each car to a csv file
    #
    #     export_list = [i, start, end, three_paths_of_a_car]
    #     big_export_list.append(export_list)
    #
    #     big_three_paths_of_a_car.append(three_paths_of_a_car)
    #
    # route_dict = {j: big_three_paths_of_a_car[j] for j in range(n)}

    with open('output/car_paths.csv', 'w+') as f:
        df = pd.DataFrame(big_export_list)
        df.to_csv(f, header=None, index=False)

    return route_dict




def r_routes_all_cars(G, graph, n, seed=False, short=False, seed_id=0, r=3, same_source=1, same_dest=1):
    # n = number_of_cars

    big_r_paths_of_a_car = []

    big_export_list = []

    random_start = []
    random_end = []

    if short:

        for i in range(n):
            start, end = random_car(G, i + seed_id, seed, same_source=same_source, same_dest=same_dest)

            random_start.append(start)
            random_end.append(end)

            r_paths_of_a_car = list(r_paths_same(graph, G, start, end, r))

            # exporting the three routes for each car to a csv file
            export_list = [i, start, end, r_paths_of_a_car]
            big_export_list.append(export_list)

            big_r_paths_of_a_car.append(r_paths_of_a_car)

        route_dict = {j: big_r_paths_of_a_car[j] for j in range(n)}

    else:

        for i in range(n):

            start, end = random_car(G, i+seed_id, seed, same_source=same_source, same_dest=same_dest)

            random_start.append(start)
            random_end.append(end)

            r_paths_of_a_car = r_paths(graph, G, start, end, r)

            # exporting the three routes for each car to a csv file
            export_list = [i, start, end, r_paths_of_a_car]
            big_export_list.append(export_list)

            big_r_paths_of_a_car.append(r_paths_of_a_car)

        route_dict = {j: big_r_paths_of_a_car[j] for j in range(n)}



    # for i in range(n):
    #
    #     start, end = random_car(G, i+seed_id, seed)
    #     three_paths_of_a_car = list(three_paths(graph, G, start, end))
    #
    #     # exporting the three routes for each car to a csv file
    #
    #     export_list = [i, start, end, three_paths_of_a_car]
    #     big_export_list.append(export_list)
    #
    #     big_three_paths_of_a_car.append(three_paths_of_a_car)
    #
    # route_dict = {j: big_three_paths_of_a_car[j] for j in range(n)}

    with open('output/car_paths.csv', 'w+') as f:
        df = pd.DataFrame(big_export_list)
        df.to_csv(f, header=None, index=False)

    return route_dict, [random_start, random_end]






# G = nx_Graph()
# graph = graph()
# print(three_routes_all_cars(G, graph, 10))

# print("a", three_routes_all_cars(G, graph, 3, seed=True, short=False, seed_id=0))
# print("b", r_routes_all_cars(G, graph, 3, seed=True, short=False, seed_id=0, r=5))

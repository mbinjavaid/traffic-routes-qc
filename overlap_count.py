from collections import Counter


def overlap_count(best_routes):

    flat_list = []

    for route in best_routes:
        for i in route:
            flat_list.append(i)

    overlap_dict = Counter(flat_list)

    # sum = 0
    # for i in overlap_dict:
    #     # if i != 1:
    #     sum = sum + i

    labels = list(overlap_dict)
    overlap_histogram = list(overlap_dict.values())

    # print("overlap sumuuh: ", sum)

    return labels, overlap_histogram

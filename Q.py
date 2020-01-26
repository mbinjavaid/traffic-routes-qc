import numpy as np
# from three_routes_all_cars import three_routes_all_cars
# from Graph import nx_Graph, graph
import time

# graph = graph()
#
# G = nx_Graph()
#
#
# root = three_routes_all_cars(G, graph, 10)


def noOfSegments(root, r):
    """Takes the root dictionary (which relates car ID to it's 3 possible routes),
    then gives the total number of segments that could be used."""

    maxNo = 0
    for i in range(len(root)):
        for j in range(r):

            if maxNo < max(root[i][j]):
                maxNo = max(root[i][j])

    return maxNo

# print("no of segments",noOfSegments(root))


def cost2IndexConstructor(segment, root, r):
    costList2index = np.zeros([len(root), r])

    for i in range(len(root)):
        for j in range(r):
            # print(root[i][j])
            for s in root[i][j]:
                if s == segment:
                    costList2index[i][j] = 1

    return costList2index

# print("cost2IndexConstructor: \n", cost2IndexConstructor(1))


def lembda(noOfSegments, root, r):

    sum = cost2IndexConstructor(0, root, r)
    for i in range(1, noOfSegments+1):
        sum += cost2IndexConstructor(i, root, r)
    # print("Sum\n", sum)#

    maxList = []
    for i in range(0, len(root)):
        maxList.append(np.sum(sum[i]))


    lembda_multiple = 100

    # print("SUM IS THIS:\n", sum)

    return lembda_multiple * max(maxList)


# print("lambda: ", lembda(noOfSegments(root)))

# print("lembda", lembda(11))


def I(i,j, r):
    """This function takes double index i,j and converts it to single index"""

    return r*(i-1) + j


def cost(root, segment, r):
    """Returns a matrix that is the outer product of costList1index
    where costList1index is the spaghettified /unfurled version of costList2index
    and costList2index is the output of costList2constructor()"""

    costList1index = np.zeros(r*len(root))
    costList2index = cost2IndexConstructor(segment, root, r)

    for i in range(len(root)):
        for j in range(r):
            # print("i:", i, "I", I(i,j))
            costList1index[I(i+1,j, r)] = costList2index[i][j]

    return np.outer(costList1index, costList1index)

# print("cost: \n", cost(root, 0))

def costSum(noOfSegments, root, r):
    sumCost = cost(root, 0, r)
    for i in range(1, noOfSegments+1):
        # print("i: ", i)
        sumCost += cost(root, i, r)

    # print("sum cost: ", sumCost)
    return sumCost

# print("COST SUM:\n", costSum(11))


# Takes the id of car and the constList1index and changes it's value to 1 for the given car id (i)
def constList1indexConstructor(i, root, r):
    """Returns the outer product of constList1index with itself. Return Q matrix of only the constraint for car i"""

    constList1index = np.zeros(r * len(root))

    for j in range(r*i, r*i+r):
        constList1index[j] = 1

    # without the minus sign in diagonals that comes from the -1 in the constraint definition
    outer = np.outer(constList1index, constList1index)

    # Turning the diagonal elements of the constraint Q negative:
    for i in range(0, r*len(root)):
        outer[i][i] = -outer[i][i]

    return outer

# print("constList1indexConstructor \n", constList1indexConstructor(0))


def constraints(root, lembda, r):
    """Finds the Q matrix for all constraints summed over all cars."""

    sumConst = constList1indexConstructor(0, root, r)
    for i in range(1, len(root)):
        sumConst += constList1indexConstructor(i, root, r)

    # print("constraints cost: ", lembda * sumConst)
    return lembda * sumConst


def QConstructor(root, make_csv=False, r=3):
    """Makes the holy Q. by adding cost Q and constraints Q"""
    # root is in from three_routes_all_cars import three_routes_all_cars

    start = time.clock()

    noOfSegs = noOfSegments(root, r)

    Q = costSum(noOfSegs, root, r) + constraints(root, lembda(noOfSegs, root, r), r)

    end = time.clock()

    print("Time taken in constructing Q: ", end-start)

    if make_csv:
        np.savetxt("output/Q.csv", Q, delimiter=",")

    return Q

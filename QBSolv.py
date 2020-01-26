# from dwave_qbsolv import QBSolv
import numpy as np
import time


from dwave.system.samplers import DWaveSampler
from dwave_qbsolv import QBSolv
from dwave.system.composites import EmbeddingComposite


def Q_dict(Q):
    """This function changes the Q from matrix form to Dict form usable by QBSolv"""

    keys = []
    QDist_list = []

    for i in range(len(Q[0])):
        for j in range(len(Q[0])):
            if Q[i][j] != 0:
                keys.append((i, j))
                QDist_list.append(Q[i][j])

    Qdict = {keys[i]: QDist_list[i] for i in range(len(keys))}

    return Qdict


def QBSolve_classical_solution(Qdict, print_energy=False):
    """This function use classical QBSolve to get solution dictionary"""

    start = time.clock()

    response = QBSolv().sample_qubo(Qdict)

    qb_solution = list(response.samples())

    if print_energy:
        print("energies=" + str(list(response.data_vectors['energy'])))

    end = time.clock()

    time_taken = end - start

    print("Time taken by classical QBSolv: ", time_taken)

    return qb_solution


def QBSolve_QC_solution(Qdict, token="DEV-3fd7a21d8cf1afa9655ac1d7e9cb809bc3d7f7dc", print_energy=False):
    """This function use QC to get solution dictionary"""

    endpoint = 'https://cloud.dwavesys.com/sapi'

    sampler = EmbeddingComposite(DWaveSampler(token=token, endpoint=endpoint))

    response = QBSolv().sample_qubo(Qdict, solver=sampler)

    if print_energy:
        print("energies=" + str(list(response.data_vectors['energy'])))

    qb_solution = list(response.samples())

    print("\n\nqb_solution:  ", qb_solution)

    return qb_solution


# def QBSolve_QC_solution(Qdict, print_energy=False):
#
#     endpoint = 'https://cloud.dwavesys.com/sapi'
#
#     sampler = EmbeddingComposite(DWaveSampler(solver='DW_2000Q_2_1', token='DEV-a480521d2f5ebbcfd5e032b94f38d2b9b43e0282', endpoint=endpoint))
#
#     response = QBSolv().sample_qubo(Qdict, solver=sampler)
#
#     if print_energy:
#         print("energies=" + str(list(response.data_vectors['energy'])))
#
#     qb_solution = str(list(response.samples()))
#
#     return qb_solution


def selection_rules(qb_solution, r):
    """takes the solution of QBSolve in dict form returns the selection rules telling which car takes which route"""

    one_solution_list = []
    solutions_list = []

    for i in range(len(qb_solution)):
        for j in range(len(qb_solution[i])):
            one_solution_list.append(qb_solution[i][j])
        solutions_list.append(one_solution_list)
        one_solution_list = []

    selections = []

    sliced_list_temp = []

    for i in range(len(solutions_list)):

        for j in range(0, len(solutions_list[i]), r):
            # sliced_list_temp.append([solutions_list[i][j]] + [solutions_list[i][j + 1]] + [solutions_list[i][j + 2]])

            big = []
            for k in range(r):
                big = big + [solutions_list[i][j+k]]

            sliced_list_temp.append(big)


        selections.append(sliced_list_temp)

        sliced_list_temp = []

    # print("sliced list: ", selection_rules)
    # print("sliced list len: ", len(selection_rules))

    return selections


qb_solution = [{0: 1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 0}, {0: 0, 1: 1, 2: 0, 3: 1, 4: 0, 5: 0}]
# qb_solution = [{0: 0, 1: 0, 2: 1, 3: 0, 4: 0, 5: 1}, {0: 1, 1: 0, 2: 0, 3: 1, 4: 0, 5: 0}, {0: 1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 0}, {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 1}, {0: 0, 1: 0, 2: 1, 3: 1, 4: 0, 5: 0}, {0: 0, 1: 0, 2: 1, 3: 0, 4: 1, 5: 0}, {0: 0, 1: 1, 2: 0, 3: 0, 4: 1, 5: 0}, {0: 0, 1: 1, 2: 0, 3: 0, 4: 0, 5: 1}, {0: 0, 1: 1, 2: 0, 3: 1, 4: 0, 5: 0}]

selection_rules_ = selection_rules(qb_solution, 3)
print("selection_rules_: ", selection_rules_)



def routes_from_selection_rule(root, selection_rules):
    """"This function takes the sliced list, aka selection rules for each car's routes,
    and then uses routes_pickle to find out the actual routes being proposed by looking at the selection rules."""

    all_roots_of_one_solution = []
    all_roots_of_all_solutions = []

    for number_of_solutions in range(len(selection_rules)):
        for i in range(0, len(selection_rules[number_of_solutions])):
            for j in range(0, len(selection_rules[number_of_solutions][i])):

                if (selection_rules[number_of_solutions][i][j]):
                    all_roots_of_one_solution.append(root[i][j])

        all_roots_of_all_solutions.append(all_roots_of_one_solution)
        all_roots_of_one_solution = []

    # length = 1

    count_list = []
    count = 0
    for i in range(len(all_roots_of_all_solutions)):
        for j in range(len(all_roots_of_all_solutions[i])):
            # for k in all_roots_of_all_solutions[i][j]:
            #     print("k: ", k)
            count = count+len(all_roots_of_all_solutions[i][j])
        count_list.append(count)
        count = 0

    argmin_count = np.argmin(count_list)

    return (all_roots_of_all_solutions[argmin_count])


def best_nodes(best_routes, sn_dict):
    """This function takes the best_routes in segments form and gives us the corresponding nodes"""

    nodes = []
    for i in range(len(best_routes)):
        small = []

        for j in best_routes[i]:
            # print("uh: ",inv_dict[j])
            small.append(sn_dict[j])

        nodes.append(small)

    return nodes

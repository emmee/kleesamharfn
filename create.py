import numpy as np

def createQUBO(nodes, edges):

    Q = {}

    for i in range(len(nodes)):
        for j in range(i, len(nodes)):
            Q[(i, j)] = 0

    for e in edges:
        start_node = e[0]
        end_node = e[1]
        Q[(start_node, start_node)] -= 1
        Q[(end_node, end_node)] -= 1
        Q[(start_node, end_node)] += 2

    QM = np.zeros((len(nodes), len(nodes)), dtype=object)
    for key in Q:
        r = key[0]
        c = key[1]
        v = Q[key]
        QM[r, c] = v

    np.savetxt("QUBO_Max_Cut.csv", QM, delimiter=";", fmt="%s")
    return Q
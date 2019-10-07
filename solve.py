from dwave.system.samplers import DWaveSampler
from dwave.system.composites import FixedEmbeddingComposite

import dwave_networkx as dnx
import minorminer
import dimod

def solveQUBO(sampler, Q, nodes):

    answer = sampler.sample_qubo(Q)
    print(answer)

    s = answer.first[0]
    set1 = []
    print("###############################################################")
    print("Answer: ", s)
    print("Energy: ", answer.first[1])

    for i in range(len(nodes)):
        if s[i] == 1:
            set1.append(i)

    print("Set 1:", set1)

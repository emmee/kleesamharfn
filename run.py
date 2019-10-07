import create
import solve
import dwave_networkx as dnx
import minorminer
import dimod

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import FixedEmbeddingComposite

if __name__ == "__main__":

    # macht ein Embedding von ungefähr 27 Qubits
    nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 4), (1, 5), (1,6), (2, 3), (2, 4), (3, 4), (3, 5), (3, 7), (5, 6),
             (5, 7), (6, 7), (6, 8), (7, 8)]

    Q = create.createQUBO(nodes, edges)

    base_sampler = DWaveSampler()
    G = dnx.chimera_graph(16, 16, 4)
    nodelist = G.nodes()
    edgelist = G.edges()

    source_edgelist = list(Q)
    embedding = minorminer.find_embedding(source_edgelist, edgelist)
    print(embedding)
    sampler = dimod.StructureComposite(base_sampler, nodelist, edgelist)
    new_sampler = FixedEmbeddingComposite(sampler, embedding)

    for i in range(10):
        solve.solveQUBO(new_sampler, Q, nodes)

import numpy as np
import networkx as nx
np.set_printoptions(edgeitems=20, linewidth=100000 )
import scipy.spatial.distance as dist
import matplotlib.pyplot as plt

test = np.loadtxt("day08/test08.txt", dtype=int, delimiter=",")
data = np.loadtxt("day08/input08.txt", dtype=int, delimiter=",")

def third(data, n):

    distance_mat = dist.cdist(data, data, metric="euclidean")
    idx = np.triu_indices(len(data), 1)
    idx_dist = np.column_stack((idx[0], idx[1], dist.squareform(distance_mat)))
    dist_sort = idx_dist[idx_dist[:, 2].argsort()]

    #  first
    G = nx.Graph()
    G.add_nodes_from(np.arange(len(data)))
    for i in range(n):
        u = dist_sort[i][0]
        v = dist_sort[i][1]
        G.add_edge(u, v, length = dist_sort[i, 2])

    len_of_clusters = [len(x) for x in sorted(nx.connected_components(G), key=len, reverse=True)]
    res = len_of_clusters[0] * len_of_clusters[1] * len_of_clusters[2]
    print("first: ", res)
    # nx.draw_networkx(G, node_size=10, with_labels=False)
    # plt.show()

    G1 = nx.Graph()
    G1.add_nodes_from(np.arange(len(data)))
    n_clusters = len(data)
    last = dist_sort[0]
    i = 0
    while n_clusters > 1:
        u = int(dist_sort[i][0])
        v = int(dist_sort[i][1])
        G1.add_edge(u, v, length = dist_sort[i][2])
        n_clusters = len([len(x) for x in sorted(nx.connected_components(G1), key=len, reverse=True)])
        last = [u, v]
        i += 1
    xx = data[last[0]][0] * data[last[1]][0]
    print("second:", xx)
    # nx.draw_networkx(G1, node_size=10, with_labels=False)
    # plt.show()

third(test, 10)
# third(data, 1000)

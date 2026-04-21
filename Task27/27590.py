from math import dist


def edge(cluster):  # anticenter
    res = []
    for d in cluster:
        sum_dist = sum(dist(d, dot) for dot in cluster)
        res.append([sum_dist, d])
    return max(res)[1]


with open(r'../Task27/Files/27590/27A_27590.txt') as file:
    dots_A = [list(map(int, i.replace(',', '.').split())) for i in file]

with open(r'../Task27/Files/27590/27B_27590.txt') as file:
    dots_B = [list(map(int, i.replace(',', '.').split())) for i in file]

clusters_A = []
eps = 1
while dots_A:
    cluster = [dots_A.pop()]
    for dot1 in dots_A:
        for dot2 in dots_A.copy():
            if dist(dot1, dot2) < eps:
                cluster.append(dot1)
                dots_A.remove(dot1)
    clusters_A.append(cluster)

edges_A = [edge(cluster) for cluster in clusters_A]

clusters_B = []
eps = 1
while dots_B:
    cluster = [dots_B.pop()]
    for dot1 in dots_B:
        for dot2 in dots_B.copy():
            if dist(dot1, dot2) < eps:
                cluster.append(dot1)
                dots_B.remove(dot1)
    if len(cluster) > 1:
        clusters_B.append(cluster)

edges_B = [edge(cluster) for cluster in clusters_B]

min_edge_A = edge(min(clusters_A, key=len))
max_edge_A = edge(max(clusters_A, key=len))

min_edge_B = edge(min(clusters_B, key=len))
max_edge_B = edge(max(clusters_B, key=len))

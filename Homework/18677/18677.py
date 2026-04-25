with open(r'../18677/Files/27A_18677.txt') as file:
    dots_A = [list(map(float, i.replace(',', '.').split())) for i in file]

with open(r'../18677/Files/27B_18677.txt') as file:
    dots_B = [list(map(float, i.replace(',', '.').split())) for i in file]

from math import dist


def center(cluster):
    res = []
    for d in cluster:
        sum_dist = sum(dist(d, dot) for dot in cluster)
        res.append([sum_dist, d])
    return min(res)[1]


def edge(cluster):
    res = []
    for d in cluster:
        sum_dist = sum(dist(d, dot) for dot in cluster)
        res.append([sum_dist, d])
    return max(res)[1]


eps = 2
clusters_A = []
while dots_A:
    cluster = [dots_A.pop()]
    for dot in cluster:
        for d in dots_A.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots_A.remove(d)
    clusters_A.append(cluster)

eps = 2
clusters_B = []
while dots_B:
    cluster = [dots_B.pop()]
    for dot in cluster:
        for d in dots_B.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots_B.remove(d)
    clusters_B.append(cluster)

center_A = [center(cluster) for cluster in clusters_A]
center_B = [center(cluster) for cluster in clusters_B]

Px_A = 10000 * sum(i[0] for i in center_A) / len(center_A)
Py_A = 10000 * sum(i[1] for i in center_A) / len(center_A)

Px_B = 10000 * sum(i[0] for i in center_B) / len(center_B)
Py_B = 10000 * sum(i[1] for i in center_B) / len(center_B)

print(f'Px_A: {Px_A}')
print(f'Py_A: {Py_A}')
print()
print(f'Px_B: {Px_B}')
print(f'Py_B: {Py_B}')

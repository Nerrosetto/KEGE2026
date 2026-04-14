from math import dist

with open(r'../Files/20911_files/27_A_20911.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]


def center(cluster):
    res = []
    for dot in cluster:
        dist_sum = sum(dist(dot, d) for d in cluster)
        res.append([dist_sum, dot])
    return min(res)[1]


cluster_1 = [dot for dot in dots if dot[1] < 0]
cluster_2 = [dot for dot in dots if dot[1] > 0]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

print(f'x:{(center_1[0] + center_2[0]) / 2 * 10000}')
print(f'y:{(center_1[1] + center_2[1]) / 2 * 10000}')

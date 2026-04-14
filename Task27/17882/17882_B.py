from math import dist

with open(r'../Files/27_B_17882.txt') as file:
    dots = [list(map(float, i.split())) for i in file]


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


cluster_1 = [dot for dot in dots if dot[1] < 4]
cluster_2 = [dot for dot in dots if 4 < dot[1] < 7]
cluster_3 = [dot for dot in dots if dot[1] > 7]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

print(f'x:{(center_1[0] + center_2[0] + center_3[0]) / 3 * 10000}')
print(f'x:{(center_1[1] + center_2[1] + center_3[1]) / 3 * 10000}')

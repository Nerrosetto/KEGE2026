from math import dist


def center(cluster):
    res = []
    for d in dots:
        sum_dist = sum(dist(d, dot) for dot in cluster)
        res.append([sum_dist, d])
    return min(res)[1]


with open(r'./Files/23209/27_A_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_A_1 = [d for d in dots if d[0] < 5]
cluster_A_2 = [d for d in dots if d[0] > 5]

center_A_1 = center(cluster_A_1)
center_A_2 = center(cluster_A_2)

print(f'A: x: {max(center_A_1[0], center_A_2[0]) * 10000}')
print(f'A: y: {max(center_A_1[1], center_A_2[1]) * 10000}')

with open(r'./Files/23209/27_B_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_B_1 = [d for d in dots if d[1] < 10]
cluster_B_2 = [d for d in dots if 10 < d[1] < 21]
cluster_B_3 = [d for d in dots if 21 < d[1] < 28]

# center_B_1 = center(cluster_B_1)
# center_B_2 = center(cluster_B_2)
# center_B_3 = center(cluster_B_3)
#
# print(f'Qx: {(center_B_1[0] - center_B_3[0]) * 10000}')
# print(f'Qy: {(center_B_1[1] - center_B_3[1]) * 10000}')

clusters_B = [cluster_B_1, cluster_B_2, cluster_B_3]

max_cluster = center(max(clusters_B, key=len))
min_cluster = center(min(clusters_B, key=len))

print((max_cluster[0] - min_cluster[0]) * 10_000)
print((max_cluster[1] - min_cluster[1]) * 10_000)

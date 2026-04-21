from math import dist


def center(cluster):
    res = []
    for d in cluster:
        sum_dist = sum(dist(d, dot) for dot in cluster)
        res.append([sum_dist, d])
    return min(res)[1]


with open(r'../Task27/Files/21599/27_A_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

# y = k * x + b
cluster_A1 = [dot for dot in dots if dot[1] < -6]
cluster_A2 = [dot for dot in dots if dot[1] > 10 * dot[0] / 12 - 10]
cluster_A3 = [dot for dot in dots if -6 < dot[1] < 10 * dot[0] / 12 - 10]

clusters = [cluster_A1, cluster_A2, cluster_A3]
centers = [center(cluster) for cluster in clusters]

print(sum(c[0] for c in centers) / len(centers) * 10000)
print(sum(c[1] for c in centers) / len(centers) * 10000)

with open(r'../Task27/Files/21599/27_B_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_B_1 = [d for d in dots if d[1] < -2 * d[0] - 26]
cluster_B_2 = [d for d in dots if -2 * d[0] - 26 < d[1] and d[0] < -10]
cluster_B_3 = [d for d in dots if -10 < d[0] and 2 * d[0] + 14 < d[1]]
cluster_B_4 = [d for d in dots if d[0] < d[1] < 2 * d[0] + 14]
cluster_B_5 = [d for d in dots if -5 < d[1] < d[0]]
cluster_B_6 = [d for d in dots if d[1] < -5]

clusters = [cluster_B_1, cluster_B_2, cluster_B_3, cluster_B_4, cluster_B_5, cluster_B_6]

centers = [center(cluster) for cluster in clusters]
print(sum(c[0] for c in centers) / len(centers) * 10_000)
print(sum(c[1] for c in centers) / len(centers) * 10_000)

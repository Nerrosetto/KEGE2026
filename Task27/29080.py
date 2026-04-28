from math import dist


def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]


with open(r'../Task27/Files/29080/27_A_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] == '3' and data[0] == 'L':
            stars.append(dots[-1])

cluster1 = [d for d in dots if d[1] > 8]
cluster2 = [d for d in dots if d[1] < 8]
min_len_center = center(min(cluster1, cluster2, key=len))
max_len_center = center(max(cluster1, cluster2, key=len))
print(max(dist(min_len_center, d2) for d2 in stars) * 10000)
print(max(dist(max_len_center, d2) for d2 in stars) * 10000)
print()

with open(r'../Task27/Files/29080/27_B_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L':
            stars.append(dots[-1])

cluster_B1_1 = [d for d in dots if d[1] < 16]
cluster_B1_2 = [d for d in dots if 16 < d[1] < 23]
cluster_B1_3 = [d for d in dots if d[1] > 23]

max_len_center = center(max(cluster_B1_1, cluster_B1_2, cluster_B1_3, key=len))
min_len_center = center(min(cluster_B1_1, cluster_B1_2, cluster_B1_3, key=len))
print(dist(max_len_center, min_len_center) * 10000)

cluster1 = [d for d in stars if d[1] < 16]
cluster2 = [d for d in stars if 16 < d[1] < 23]
cluster3 = [d for d in stars if d[1] > 23]
max_len_center = center(max(cluster1, cluster2, cluster3, key=len))
min_len_center = center(min(cluster1, cluster2, cluster3, key=len))

distances = []
for s1 in cluster1:
    for s2 in cluster2:
        distances.append(dist(s1, s2))
for s2 in cluster2:
    for s3 in cluster3:
        distances.append(dist(s3, s2))
for s1 in cluster1:
    for s3 in cluster3:
        distances.append(dist(s1, s3))

print(max(distances) * 10000)

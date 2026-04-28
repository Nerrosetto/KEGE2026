from math import dist


def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]


with open(r'../Task27/Files/29079/27_A_29079.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'N' and data[-2:] == 'IV':
            stars.append(dots[-1])

cluster1 = [d for d in dots if d[1] > 8]
cluster2 = [d for d in dots if d[1] < 8]

center1 = center(cluster1)
center2 = center(cluster2)

A1 = []
for d in stars:
    if d not in cluster1:
        A1.append(dist(d, center1))

for d in stars:
    if d not in cluster2:
        A1.append(dist(d, center2))

print(min(A1) * 10000)
print(max(A1) * 10000)

with open(r'../Task27/Files/29079/27_B_29079.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'J' and data[-1] == 'V':
            stars.append(dots[-1])

cluster1 = [d for d in stars if d[1] < 16]
cluster2 = [d for d in stars if 16 < d[1] < 23]
cluster3 = [d for d in stars if d[1] > 23]
max_len_center = max(cluster1, cluster2, cluster3, key=len)
min_len_center = min(cluster1, cluster2, cluster3, key=len)

maximal = 0
for i in max_len_center:
    if i[0] > maximal:
        maximal = i[0]

minimal = 10 ** 10
for i in min_len_center:
    if i[1] < minimal:
        minimal = i[1]

print(maximal * 10000)
print(minimal * 10000)

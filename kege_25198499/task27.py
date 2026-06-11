from math import dist


def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]


with open(r'../kege_25198499/files/27_A_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[2:] == 'VII':
            stars.append(list(map(float, [x, y])))

cluster1 = [i for i in dots if i[1] > 8]
cluster2 = [i for i in dots if i[1] < 8]

center1 = center(cluster1)
center2 = center(cluster2)

max_dist = 0
for i in stars:
    if i in cluster1:
        max_dist = max(max_dist, dist(center1, i))
    else:
        max_dist = max(max_dist, dist(center2, i))

min_dist = 10 ** 10
for i in stars:
    if i in cluster1:
        min_dist = min(dist(i, center1), min_dist)
    else:
        min_dist = min(dist(i, center2), min_dist)

print(max_dist * 10000, min_dist * 10000)

with open(r'../kege_25198499/files/27_B_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] == '8':
            stars.append(list(map(float, [x, y])))

cluster1 = [i for i in dots if i[1] > 24]
cluster2 = [i for i in dots if 16 < i[1] < 24]
cluster3 = [i for i in dots if i[1] < 16]

maxi = 0
for i in stars:
    if i in cluster1:
        maxi = max([dist(i, t) for t in stars if t in cluster1])
    elif i in cluster2:
        maxi = max([dist(i, t) for t in stars if t in cluster2])
    else:
        maxi = max([dist(i, t) for t in stars if t in cluster3])

mini = 10 ** 10
for i in stars:
    if i in cluster1:
        mini = min([dist(i, t) for t in stars if t in cluster1 and dist(i, t) != 0])
    elif i in cluster2:
        mini = min([dist(i, t) for t in stars if t in cluster2 and dist(i, t) != 0])
    else:
        mini = min([dist(i, t) for t in stars if t in cluster3 and dist(i, t) != 0])

print(maxi * 10000, mini * 10000)

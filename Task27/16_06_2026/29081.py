from math import dist
from string import printable as pri


def centre(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, o) for o in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'Files/29081/27_A_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data == 'VII':
            stars.append([float(x), float(y)])

cluster_1 = [i for i in dots if i[1] < 8]
cluster_2 = [i for i in dots if i[1] > 8]

stars_1 = [i for i in stars if i[1] < 8]
stars_2 = [i for i in stars if i[1] > 8]

centre_1 = centre(cluster_1)
centre_2 = centre(cluster_2)

A = []
for s in stars_1:
    A.append(dist(centre_1, s))

for s in stars_2:
    A.append(dist(centre_2, s))

print(int(min(A) * 10000), int(max(A) * 10000))

with open(r'Files/29081/27_B_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data[1] in pri[:10] and int(data[1]) >= 8:
            stars.append([float(x), float(y)])

cluster_1 = [i for i in dots if i[1] > 22]
cluster_2 = [i for i in dots if 15 < i[1] < 22]
cluster_3 = [i for i in dots if i[1] < 15]

stars_1 = [i for i in stars if i[1] > 22]
stars_2 = [i for i in stars if 15 < i[1] < 22]
stars_3 = [i for i in stars if i[1] < 15]

centre_1 = centre(cluster_1)
centre_2 = centre(cluster_2)
centre_3 = centre(cluster_3)

B = []
for dot in stars_1:
    for o in stars_2 + stars_3:
        B.append(dist(dot, o))
for dot in stars_2:
    for o in stars_3:
        B.append(dist(dot, o))
B1 = 10000 * min(B)

B2 = []
for dot in stars_1:
    for o in stars_1:
        if dot != o:
            B2.append(dist(dot, o))

for dot in stars_2:
    for o in stars_2:
        if dot != o:
            B2.append(dist(dot, o))

for dot in stars_3:
    for o in stars_3:
        if dot != o:
            B2.append(dist(dot, o))

print(int(B1 * 10000), int(sum(B2) / len(B2) * 10000))

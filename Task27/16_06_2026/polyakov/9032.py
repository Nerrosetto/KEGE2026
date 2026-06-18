from math import dist


def centre(cluster):
    ans = []
    for i in cluster:
        sum_dist = sum(dist(i, o) for o in cluster)
        ans.append([sum_dist, i])
    return min(ans)[1]


with open(r'Files/9032/27-122a.txt') as file:
    dots = []
    stars = []
    for inf in file:
        x, y, data = inf.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if int(data[1]) == 3 and data[0] == 'L':
            stars.append([float(x), float(y)])

cluster1 = [dot for dot in dots if dot[1] < 10]
cluster2 = [dot for dot in dots if dot[1] > 10]

stars1 = [dot for dot in stars if dot[1] < 10]
stars2 = [dot for dot in stars if dot[1] > 10]

min_len = min([cluster1, cluster2], key=len)
min_centre = centre(min_len)

A1 = 0
for i in stars:
    A1 = max(A1, dist(i, min_centre))
print(A1 * 10000)

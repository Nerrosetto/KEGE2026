# from itertools import combinations
from math import dist


def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]


with open(r'../Task27/Files/29081/27_A_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[2:] == 'VII':
            stars.append(dots[-1])

cluster1 = [d for d in dots if d[1] > 8]
cluster2 = [d for d in dots if d[1] < 8]

center1 = center(cluster1)
center2 = center(cluster2)

stars1 = [d for d in stars if d[1] > 8]
stars2 = [d for d in stars if d[1] < 8]
#
# ans = []
# for s in stars1:
#     ans.append(dist(center1, s))
# for s in stars2:
#     ans.append(dist(center2, s))
#
# print(min(ans)*10000)
# print(max(ans)*10000)
# print()
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

cluster1 = [[d for d in dots if d[1] > 8],
            [d for d in stars if d[1] > 8]]
cluster2 = [[d for d in dots if d[1] < 8],
            [d for d in stars if d[1] < 8]]
clusters = [cluster1, cluster2]

A1 = min(dist(center(cl[0]), s) for cl in clusters for s in cl[1])
A2 = max(dist(center(cl[0]), s) for cl in clusters for s in cl[1])
print(A1 * 10000)
print(A2 * 10000)
print()

with open(r'../Task27/Files/29081/27_B_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if int(data[1]) >= 8:
            # if data[1] not in [str(i) for i in range(1, 8)]:
            # if data[1] in '89':
            # if data[1] >= '8':
            stars.append(dots[-1])

stars1 = [d for d in stars if d[1] < 16]
stars2 = [d for d in stars if 16 < d[1] < 23]
stars3 = [d for d in stars if d[1] > 23]
stars = [stars1, stars2, stars3]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# B1 = []
# for s1 in stars1:
#     for s2 in stars2:
#         B1 += [dist(s1, s2)]
#
# for s1 in stars1:
#     for s3 in stars2:
#         B1 += [dist(s1, s3)]
#
# for s3 in stars3:
#     for s2 in stars2:
#         B1 += [dist(s3, s2)]
# print(min(B1) * 10000)
#
# stardist1 = [dist(d1, d2) for d1 in stars1 for d2 in stars1 if d1 != d2]
# stardist2 = [dist(d1, d2) for d1 in stars2 for d2 in stars2 if d1 != d2]
# stardist3 = [dist(d1, d2) for d1 in stars3 for d2 in stars3 if d1 != d2]
# stardist = stardist1+stardist2+stardist3
# B2 = sum(stardist) / len(stardist)
# print(B2 * 10000)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# B1 = min([dist(s1, s2) for cl1, cl2 in combinations(stars, 2) for s1 in cl1 for s2 in cl2]) * 10000
# B2 = [dist(s1, s2) for cl in stars for s1, s2 in combinations(cl, 2)]
# print(B1)
# print(sum(B2) / len(B2) * 10000)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# B1, B2 = [], []
# for s1, s2 in combinations(stars, 2):
#     u = any(s1 in cl and s2 in cl for cl in stars)
#     d = dist(s1, s2)
#     if u: B2.append(d)
#     else: B1.append(d)
#
# print(min(B1) * 10_000, sum(B2) / len(B2) * 10_000)

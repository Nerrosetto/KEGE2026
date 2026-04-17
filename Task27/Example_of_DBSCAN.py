# eps = 1
# clusters = []
# while dots:
#     cluster = [dots.pop()]
#     for dot in cluster:
#         for d in dots.copy():
#             if dist(dot, d) < eps:
#                 cluster.append(d)
#                 dots.remove(d)
#     clusters.append(cluster)
#
# print([len(cluster) for cluster in clusters])
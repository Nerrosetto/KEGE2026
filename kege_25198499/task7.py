# h, w = 1024, 120
# V = 210 * 2 ** 13 / 2
#
# ans = 0
# for i in range(1, 1000):
#     if h * w * i < V:
#         ans = i
# print(2 ** ans)
print(2 ** (210 * 2 ** 13 / (1024 * 120) - 1))

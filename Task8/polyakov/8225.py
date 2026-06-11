from itertools import product as pro
from string import printable as pri

cnt = 0
# for i in pro(pri[:12], repeat=5):
#     if i[0] != '0':
#         i = ''.join(i)
#         for t in pro(pri[1:12:2], repeat=2):
#             i = i.replace(''.join(t), '*')
#         if i.count(i) <= 2:
#             cnt += 1
# print(cnt)

for i in pro(pri[:12], repeat=5):
    if i[0] != '0':
        i = ''.join(i)
        for t in pri[1:12:2]:
            i = i.replace(t, '*')
        if sum([i[0] == i[1] == '*' for i in zip(i, i[1:])]) <= 2:
            cnt += 1
print(cnt)

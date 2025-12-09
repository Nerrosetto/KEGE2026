from itertools import product as pro

cnt = 0
for i in range(5, 8):
    for val in pro(sorted('БЕРСК'), repeat=i):
        cnt += 1
print(cnt)

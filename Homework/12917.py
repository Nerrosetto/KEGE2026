from itertools import permutations as per

cnt = 0
for i in set(per('ПРОСТО')):
    i = ''.join(i)
    if 'ОО' not in i:
        cnt += 1
print(cnt)

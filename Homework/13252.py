from itertools import permutations as per

cnt = 0
for val in set(per('КИДАЛА', r=5)):
    val = ''.join(val)
    if 'АА' not in val:
        cnt += 1
print(cnt)

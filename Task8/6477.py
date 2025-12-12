from itertools import permutations as per

cnt = 0
for val in set(per('ЛЕВИОСА')):
    val = ''.join(val)
    for i in 'ЕИОА':
        val = val.replace(i, '*')
    for i in 'ЛВС':
        val = val.replace(i, '+')
    if val[0] != '*' and val[len(val) // 2] != '+':
        cnt += 1
print(cnt)

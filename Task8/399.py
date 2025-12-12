from itertools import permutations as per

cnt = 0
for val in set(per('ВОРОТА', r=6)):  # множество работает на permutations, не на слова которые оно генерирует.
    res = []
    val = ''.join(val)
    for i in 'ОА':
        val = val.replace(i, '*')
    if '**' not in val:
        cnt += 1
print(cnt)

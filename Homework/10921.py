from itertools import permutations as per

cnt = 0
for val in set(per('ДЖАВАСКРИПТ')):
    sumi = 0
    val = ''.join(val)
    for t in range(len(val)):
        if val[t] in 'АИ':
            sumi += t + 1
    if sumi == 11:
        cnt += 1
print(cnt)

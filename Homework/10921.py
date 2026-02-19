from itertools import permutations as per

alph = 'ДЖАВАСКРИПТ'
cnt = 0
d = 'АИ'
for i in set(per(alph)):
    i = ''.join(i)
    cnt_g = 0
    for t in d:
        for v in range(len(i)):
            if t == i[v]:
                cnt_g += 1
    if cnt_g == 11:
        cnt += 1
print(cnt)

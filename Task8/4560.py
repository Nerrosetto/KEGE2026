from itertools import permutations as per, product as pro

alph = sorted(set('ТИХОРЕЦК'))
cnt = 0
ans = 'ТИХО'
for x in per(alph, 4):
    x = ''.join(x)
    cnt2 = 0
    cnt1 = 0
    for i in 'ИОЕ':
        if i in x:
            cnt1 += 1
    if cnt1 == 2:
        for t in range(0, 4):
            if ans[t] == x[t]:
                cnt2 += 1
        if cnt2 == 2:
            cnt += 1
print(cnt)

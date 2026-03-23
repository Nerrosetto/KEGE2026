from itertools import permutations as per

alph = per(sorted('АБИКОЛУН'), r=8)
cnt = 0
for i in set(alph):
    i = ''.join(i)
    for p in 'АИОУ':
        i = i.replace(p, '!')
    for t in 'БКЛН':
        i = i.replace(t, '_')
    if '__' not in i and '!!' not in i:
        cnt += 1
print(cnt)

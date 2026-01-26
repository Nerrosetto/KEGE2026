from itertools import permutations as pro

alph = sorted('КАЙФ')
cnt = 0
for val in pro(alph):
    val = ''.join(val)
    if val[-1] != 'Й' and 'КФ' not in val:
        cnt += 1
print(cnt)

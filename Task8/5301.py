from itertools import product as pro

cnt = 0
alph = 'леся_'
for val in pro(alph, repeat=5):
    val = ''.join(val)
    val = val.replace('я', '*').replace('е', '*').replace('л', '+').replace('с', '+')
    if val.count('_') == 1 and val[-1] != '_' and val[0] != '_' and '**' not in val and '++' not in val:
        cnt += 1
print(cnt)

from itertools import product as pro

cnt = 0
for val in pro('ПСКАЛЬ', repeat=4):
    val = ''.join(val)
    if val[0] != 'Ь' and 'ЬЬ' not in val:
        cnt += 1
print(cnt)

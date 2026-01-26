from itertools import product as pro

alph = sorted('НОРМАЛЬЕ')
cnt = 0
pos_1 = [0, False]
pos_2 = [0, False]
check = False
for pos, val in enumerate(pro(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[:4] == 'НОРМ' and pos_1[1] == False:
        pos_1 = [pos, True]
    elif val == 'НЕНОРМ' and pos_2[1] == False:
        pos_2 = [pos, True]
print(pos_1[0] - pos_2[0] - 1)

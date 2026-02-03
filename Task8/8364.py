from itertools import product as pro

flag1 = False
flag2 = False
alph = sorted(set('КРАТЕР'))
for num, val in enumerate(pro(alph, repeat=6), start=1):
    val = ''.join(val)
    if val == 'КАРЕТА' and flag1 == False:
        flag1 = num
    if val == 'РАКЕТА' and flag2 == False:
        print(num - flag1 - 1)
        break

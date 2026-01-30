from itertools import product as pro

alph = sorted('АЕКНС')
for num, val in enumerate((pro(alph, repeat=6)), start=1):
    val = ''.join(val)
    if val == 'СЕНЕКА':
        print(num)
        break

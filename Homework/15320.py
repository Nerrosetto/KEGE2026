from itertools import product as pro

flag = False
for num, val in enumerate(pro(sorted('ПАРУС'), repeat=5), start=1):
    val = ''.join(val)
    a = 0
    if val.count('У')  <= 1 and 'АА' not in val:
        a = num
        break
print(a)

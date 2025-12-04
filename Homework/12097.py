from itertools import product as pro

res = []
al = sorted('ГИРЛЯНДА')
for pos, num in enumerate(pro(al, repeat=6), start=1):
    num = ''.join(num)
    if num[0] != 'Я' and num.count('Д') == 3 and pos % 2 == 0:
        res.append(pos)
print(res[-1])

from itertools import product as pro

res = []
al = sorted('АОЖПЮЗ')
for pos, num in enumerate(pro(al, repeat=6), start=1):
    num = ''.join(num)
    if num[0] == 'А' and num.count('З') >= 2 and pos % 2 == 0:
        res.append(pos)
print(len(res))

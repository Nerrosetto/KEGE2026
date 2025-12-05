from itertools import product as pro

cnt = 0
for val in pro('НИЧЬЯ', repeat=7):
    val = ''.join(val)
    for i in 'ИЯ':
        val = val.replace(i, '*')
    if val.count('*') == 2 and '**' not in val:
        cnt += 1
print(cnt)

from itertools import product as pro

cnt = 0
for val in pro('ПИТОН', repeat=4):
    val = ''.join(val)
    for i in 'ИО':
        val = val.replace(i, '*')
    for i in 'ПТН':
        val = val.replace(i, '!')
    if '**' not in val and '!!' not in val:
        cnt += 1
print(cnt)

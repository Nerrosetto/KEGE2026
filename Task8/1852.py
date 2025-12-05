from itertools import product as pro

cnt = 0
for val in pro('ГЕПАРД', repeat=5):
    val = ''.join(val)
    if val.count('Г') == 1 and val[0] != 'А' and val[-1] != 'Е':
        cnt += 1
print(cnt)

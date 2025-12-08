from itertools import product as pro

cnt = 0
for val in pro('ПОЛИНА', repeat=8):
    cnt_s = 0
    cnt_g = 0
    val = ''.join(val)
    for i in 'ПЛН':
        cnt_s += val.count(i)
    for i in 'ОИА':
        cnt_g += val.count(i)
    if cnt_s > cnt_g:
        cnt += 1
print(cnt)

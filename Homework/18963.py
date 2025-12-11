from itertools import product as pro

cnt = 0
for val in pro(sorted('КОТБУС'), repeat=8):
    val = ''.join(val)
    if 'КОТ' in val and val[0] not in ['О', 'У']:
        cnt += 1
print(cnt)

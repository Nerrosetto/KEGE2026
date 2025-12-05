from itertools import product as pro

cnt = 0
for val in pro('ЗЕРКАЛО', repeat=6):
    val = ''.join(val)
    if 0 < val.count('К') <= 4:
        val = val.replace('К', '')
        if len(val) == len(set(val)):
            cnt += 1
print(cnt)

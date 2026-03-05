from itertools import product as pro
from string import printable as pri

ans = set()
for a in pro(pri[:5], repeat=5):
    a = ''.join(a)
    for b in pro(pri[:5], repeat=5):
        b = ''.join(b)
        for c in pro(pri[:5], repeat=5):
            c = ''.join(c)
            if int(a, 5) > int(b, 5) and int(c, 5) == int(a, 5) - int(b, 5):
                ans |= {1}
print(len(ans))

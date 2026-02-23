from itertools import product as pro

d = []
for i in range(4, 100):
    d.append(str(3 ** i))
t = []
for i in pro('123456789', repeat=6):
    t = ''.join(i)
    if sum(map(int, i)) % 113 == 0 and int(str(i)) % 2 != 0:
        if str(i) in d:
            print(i, d.index(str(i)))

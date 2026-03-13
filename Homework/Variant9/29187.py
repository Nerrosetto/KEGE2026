from itertools import product as pro, permutations as per

def f(x, y, z, w):
    return (w <= y) and (not y == x) and (x or z)

for i in pro((0, 1), repeat=6):
    table = [
        (i[0], 1, 1, 1),
        (1, 1, i[1], i[2]),
        (i[3], i[4], i[5], 1)
    ]
    if len(set(table)) == len(table):
        for p in per('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(*p, sep='')
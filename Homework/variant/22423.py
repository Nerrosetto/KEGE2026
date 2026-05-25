from itertools import product as pro, permutations as per


def f(x, y, z, w):
    return ((z <= x) and (x <= y)) or (w == (z or x))


for i in pro((0, 1), repeat=7):
    table = [
        (i[0], 1, i[1], i[2]),
        (i[3], i[4], 1, 1),
        (i[5], 1, i[6], 1)
    ]
    for p in per('xyzw'):
        if len(set(table)) == len(table):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(*p)

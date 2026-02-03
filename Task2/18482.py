from itertools import product as pro, permutations as per


def f(x, y, z, w):
    return (x == (y <= (z or x))) and w


for i in pro((0, 1), repeat=5):
    table = [(1, 0, 1, i[0]),
             (0, i[1], i[2], 0),
             (1, 0, i[3], i[4])
             ]
    if len(set(table)) == len(table):
        for t in per('xyzw'):
            if [f(**dict(zip(t, p))) for p in table] == [1, 1, 1]:
                print(*t, sep='')

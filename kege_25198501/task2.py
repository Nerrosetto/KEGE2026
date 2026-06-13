from itertools import permutations as per, product as pro


def f(x, y, z, w):
    return (z <= (not (y <= x))) or w


for i in pro((0, 1), repeat=7):
    table = [
        (i[0], 1, i[1], i[2]),
        (i[3], i[4], 0, 0),
        (i[5], 0, 1, i[6])
    ]
    for p in per('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
            print(*p)

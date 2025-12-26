from itertools import product as pro, permutations as per


def f(x, y, z):
    return not (x == (y <= z))


table = [
    (0, 0, 1),
    (0, 1, 1)
]
for p in per('xyz'):
    if [f(**dict(zip(p, t))) for t in table] == [1, 0]:
        print(*p, sep='')

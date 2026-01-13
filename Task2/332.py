from itertools import permutations as pro


def f(x, y, z, w):
    return (x or y and not z) and not w


tabl = (
    (1, 0, 0, 0),
    (0, 0, 1, 0),
    (0, 1, 0, 1,),
)
cnt = 0
for i in pro('xyzw'):
    if [f(**dict(zip(i, t))) for t in tabl] == [1, 1, 0]:
        cnt += 1
print(cnt)

from string import printable as pri


def f(x, sys):
    a = ''
    for i in x:
        a += str(pri.index(i))
    return int(a)


for p in range(1, 999999):
    num = f('kot', p) + f('golodni', p)
    if num == f('meeow', p) * f('100', p) - 20194023088:
        print(f('purr', p))
        break

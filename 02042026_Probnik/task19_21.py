def f(x, move):
    if x <= 15:
        return (move - 1) % 2
    if move == 0:
        return False
    h = [
        f(x - 3, move - 1),
        f(x - 8, move - 1),
        f(x // 3, move - 1),
    ]
    return any(h) if (move - 1) % 2 == 0 else any(h)


print('19)', min(i for i in range(600, 17, -1) if f(i, 2)))
# print('20)', *sorted(i for i in range(600, 17, -1) if f(i, 3) and not f(i, 1))[:2])
# print('21)', min(i for i in range(600, 17, -1) if f(i, 4) and not f(i, 2)))

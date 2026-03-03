def f(x1, x2, s):  # x1- первая куча, x2- вторая куча, s-ходы
    if x1 + x2 >= 259:
        return s % 2 == 0
    if s == 0:
        return False
    h = [f(x1 + 1, x2, s - 1),
         f(x1 * 2, x2, s - 1),
         f(x1, x2 + 1, s - 1),
         f(x1, x2 * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h) # any, если 19)


# print('19)', min(*[x for x in range(1, 242) if f(17, x, 2)]))
print('20)', *[x for x in range(1, 242) if f(17, x, 3) and not f(17, x, 1)][:2])
print('21)', min(*[x for x in range(1, 242) if f(17, x, 4) and not f(17, x, 2)]))

def f(x1, x2, s):
    if x1 + x2 >= 77:
        return s % 2 == 0

    if s == 0:
        return False

    h = [f(x1 + 3, x2, s - 1),
         f(x1, x2 + 3, s - 1),
         f(x1 * 3, x2, s - 1),
         f(x1, x2 * 3, s - 1)
         ]
    return any(h) if (s - 1) % 2 == 0 else all(h)


print('19)', min(*[x for x in range(1, 65) if f(x, 12, 2)]))
# print('20)', *[x for x in range(1, 65) if f(x, 12, 3) and not f(x, 12, 1)])
# print('21)', *[x for x in range(1, 65) if f(x, 12, 4) and not f(x, 12, 2)])

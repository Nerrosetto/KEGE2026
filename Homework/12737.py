def f(x1, x2, s):  # x1- первая куча, x2- вторая куча, s-ходы
    if x1 + x2 >= 385:
        return s % 2 == 0
    if s == 0:
        return False
    h = [f(x1 + 5, x2, s - 1),
         f(x1 * 2, x2, s - 1),
         f(x1, x2 + 5, s - 1),
         f(x1, x2 * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)


# print('19)', min(*[x for x in range(1, 55) if f(8, x, 2)]))
print('20)', min(*[x for x in range(1, 55) if f(8, x, 3) and not f(8, x, 2)]),
      max(*[x for x in range(1, 55) if f(8, x, 3) and not f(8, x, 2)]))
print('20)', min(*[x for x in range(1, 55) if f(8, x, 4) and not f(8, x, 3)]))

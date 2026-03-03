def f(x1, x2, s):
    if x1 + x2 >= 65:
        return s % 2 == 0
    if s == 0:
        return False
    h = [f(x1 + 1, x2, s - 1),
         f(x1 * 3, x2, s - 1),
         f(x1, x2 + 1, s - 1),
         f(x1, x2 * 3, s - 1)
         ]
    return any(h) if (s - 1) % 2 == 0 else any(h)


print(min(*[x for x in range(1, 59) if f(6, x, 2)]))

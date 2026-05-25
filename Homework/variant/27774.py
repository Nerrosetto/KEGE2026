def f(x1, x2, s):
    if x1 + x2 >= 207:
        return s % 2 == 0
    if s == 0:
        return False
    h = [f(x1 + 1, x2, s - 1),
         f(x1 * 2, x2, s - 1),
         f(x1, x2 + 1, s - 1),
         f(x1, x2 * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', min(*[x for x in range(1, 190) if f(17, x, 2)]))

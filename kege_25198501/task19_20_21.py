def f(a, b, s):
    if a + b >= 77:
        return s % 2 == 0
    if s == 0:
        return False
    h = [
        (a + 3, b, s - 1),
        (a, b + 3, s - 1),
        (a * 3, b, s - 1),
        (a, b * 3, s - 1)
    ]
    return all(h) if (s - 1) % 2 == 0 else all(h)


print('19)', min(x for x in range(1, 65) if f(12, x, 2)))
print('20)', sorted([x for x in range(1, 65) if f(12, x, 3) and not f(12, x, 1)])[:2])
print('21)', min(x for x in range(1, 65) if f(12, x, 4) and not f(12, x, 2)))

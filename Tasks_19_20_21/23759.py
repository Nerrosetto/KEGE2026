def f(x, s):
    if x <= 30:
        return s % 2 == 0
    if s == 0:
        return False
    h = [f(x - 3, s - 1),
         f(x - 5, s - 1),
         f(x // 4, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)


print('19)', min(*[x for x in range(31, 1000) if f(x, 2) and not f(x, 1)]))
print('20)', *sorted([*[x for x in range(31, 1000) if f(x, 3) and not f(x, 1)]])[:2])
print('21)', min(*[x for x in range(31, 1000) if f(x, 4) and not f(x, 2)]))

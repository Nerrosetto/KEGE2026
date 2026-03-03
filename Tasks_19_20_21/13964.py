def f(x1, x2, s):
    if x1 + x2 <= 108:
        return s % 2 == 0
    if s == 0:
        return False
    h = [f(x1, x2 - 2, s - 1),
         f(x1 - 2, x2, s - 1),
         ]
    if x1 % 2 == 0:
        h += [f(x1 // 2, x2, s - 1)]
    else:
        h += [f(x1 // 2 + 1, x2, s - 1)]

    if x2 % 2 == 0:
        h += [f(x1, x2 // 2, s - 1)]
    else:
        h += [f(x1, x2 // 2 + 1, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)


#print('19)', max(*[x for x in range(49, 1000) if f(x, 60, 2)]))
print('20)', min(*[x for x in range(49, 1000) if f(x, 60, 3) and not f(x, 60, 1)]),
      max(*[x for x in range(49, 1000) if f(x, 60, 3) and not f(x, 60, 1)]))
print('21)', max(*[x for x in range(49, 1000) if f(x, 60, 4) and not f(x, 60, 2)]))

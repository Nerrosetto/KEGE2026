def f(x1, x2, s):
    if x1 + x2 <= 100:
        return s % 2 == 0
    if s == 0:
        return False
    h = [f(x1-3, x2 - 3, s - 1),]
    if x1 % 2 == 0:
        h += [f(x1 // 2, x2, s - 1)]
    else:
        h += [f(x1 // 2 - 1, x2, s - 1)]

    if x2 % 2 == 0:
        h += [f(x1, x2 // 2, s - 1)]
    else:
        h += [f(x1, x2 // 2 - 1, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)


# print('19)', min(*[x for x in range(53, 1000) if f(x, 48, 2)])) # 59)
print('20)', min(*[x for x in range(53, 1000) if f(x, 48, 3) and not f(x, 48, 1)]),
      max(*[x for x in range(53, 1000) if f(x, 48, 3) and not f(x, 48, 1)]))
print('21)', min(*[x for x in range(53, 1000) if f(x, 48, 4) and not f(x, 48, 2)]))

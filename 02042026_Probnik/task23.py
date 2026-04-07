def f(s, e, t=''):
    if s < e:
        return 0
    if s == e:
        return 1
    return f(s - 1, e, t + 'A') + f(s - 4, e, t + 'B') + f(s // 3, e, t + 'C')


print(f(19, 2) - f(19, 7) - f(19, 13))
print(f(19, 12) * f(14, 6) * f(5, 2))

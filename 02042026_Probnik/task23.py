def f(s, e, t=''):
    if s == e:
        return 1
    if s < e or s == 7:
        return 0
    return f(s - 1, e, t + 'A') + f(s - 4, e, t + 'B') + f(s // 3, e, t + 'C')


print(f(19, 13) * f(13, 2))

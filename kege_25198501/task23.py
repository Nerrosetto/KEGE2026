def f(a, b):
    if a == b:
        return 1
    if a < b or a == 24:
        return 0
    h = [
        f(a - 1, b),
        f(a - 6, b),
        f(a // 2, b),
    ]
    return sum(h)


print(f(34, 29) * f(29, 19) * f(19, 6))

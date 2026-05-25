def f(x):
    h = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            h |= {i, x // i}
    return h if len(h) == 4 else 0


for i in range(178965, 178983):
    F = f(i)
    if F:
        print(sorted(F, reverse=True))

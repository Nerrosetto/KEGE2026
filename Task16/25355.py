from functools import lru_cache


def f(n):  # нет cache, так как функция делает до тысячи шагов.
    return f(n - 4) + 3580 if n >= 19 else 6 * (g(n - 7) - 36)


@lru_cache(None)
def g(n):
    return n / 20 + 28 if n >= 248045 else g(n + 9) - 4


for i in range(250000)[::-1]:
    g(i)
print(f(673))

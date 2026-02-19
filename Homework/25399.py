from functools import lru_cache


@lru_cache(None)
def g(n):
    return g(n + 8) / 2 - 109 if n <= 303728 else n - 15


@lru_cache(None)
def f(n):
    return f(n - 5) + 1092 if n >= 128 else 5 * g(n - 7) + 29


for i in range(2050):
    f(i)

print(f(2049))

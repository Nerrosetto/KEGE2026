from functools import lru_cache


def f(n):
    return 3 * (g(n - 2) + 5)


@lru_cache(None)
def g(n):
    return g(n - 3) + 2 if n >= 8 else 3 * n


for i in range(12346):
    g(i)
print(f(12345))

from functools import lru_cache


@lru_cache(None)
def G(n):
    return G(n - 2) + 1 if n >= 10 else 2 * n


@lru_cache(None)
def F(n):
    return 2 * (G(n - 3) + 8)


for i in range(0, 15549):
    F(i)
print(F(15548))

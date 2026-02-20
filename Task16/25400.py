from functools import lru_cache

@lru_cache(None)
def f(n):
    return 3 * (g(n - 2) - 15) if n >= 31054 else f(n + 4) + 3020


@lru_cache(None)
def g(n):
    return g(n - 5) - 15 if n >= 28 else 3 * n - 4

for i in range(31_100):
    g(i)
for i in range(31100, 0, -1):
    f(i)
print(f(15))

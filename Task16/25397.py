from functools import lru_cache


@lru_cache(None)
def f(n):
    return f(n - 4) + 3020 if n > 40 else 3 * (g(n - 2) - 15)


@lru_cache(None)
def g(n):
    return 10 * n + 50 if n >= 301208 else g(n + 7) - 21


for i in range(301209)[::-1]:
    g(i)
for i in range(301209):
    f(i)
print(f(2026))

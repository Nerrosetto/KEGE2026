from functools import lru_cache


@lru_cache(None)
def f(n):
    return 1 if n == 1 else n * f(n - 1)


for n in range(1, 3001):
    f(n)
print((f(2024) - 5 * f(2023)) / f(2022))

from functools import lru_cache


@lru_cache(None)
def f(n):
    return n if n >= 2025 else n * 2 + f(n + 2)


for i in range(2026)[::-1]:
    f(i)
print(f(82) - f(81))

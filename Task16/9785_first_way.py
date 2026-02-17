from functools import lru_cache


@lru_cache(None)
def F(n):
    return n + 1 + F(n - 2) if n >= 7 else 7


for i in range(0, 2025):
    F(i)

print(F(2024) - F(2020))

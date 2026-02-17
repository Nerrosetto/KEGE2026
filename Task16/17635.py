from functools import lru_cache


@lru_cache(None)
def F(n):
    return (n + 1) * F(n - 1) if n > 1 else 1


for i in range(0, 2025):
    F(i)
print((F(2024) - 3 * F(2023)) / F(2022))

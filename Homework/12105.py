from functools import lru_cache


@lru_cache(None)
def F(n):
    return n if n <= 5 else 2 * n - 8 + F(n - 2) + F(n - 1) // 8


print(F(163))

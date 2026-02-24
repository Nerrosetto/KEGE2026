from functools import lru_cache


@lru_cache(None)
def F(n):
    if n == 0:
        return 0
    return n + F(n - 3) if n % 3 == 0 and n > 0 else n + F(n - n % 3)


for i in range(23):
    F(i)
print(F(22))

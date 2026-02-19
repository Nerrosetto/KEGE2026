from functools import lru_cache


@lru_cache(None)
def f(n):
    return f(n - 8) + 2 ** n if n >= 10 else n + 10


for i in range(4001):
    f(i)
print((f(4000) + 2 * f(3992)) / f(3984))

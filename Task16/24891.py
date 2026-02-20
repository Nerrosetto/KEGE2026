from functools import lru_cache


@lru_cache(None)
def f(n):
    return n - 7 + f(n - 21) if n > 10 else n


for i in range(185735):
    f(i)
print((f(185734) - f(185650)) / f(40))

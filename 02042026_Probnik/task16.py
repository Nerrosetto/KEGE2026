from functools import lru_cache


@lru_cache(None)
def F(n):
    return 3 * (G(n - 2) + 5)


@lru_cache(None)
def G(n):
    return 3 * n if n < 8 else G(n - 3) + 2


for i in range(12343):
    G(i)

for i in range(2, 12346):
    F(i)

print(F(12345))

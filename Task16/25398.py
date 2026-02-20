from functools import lru_cache


@lru_cache(None)
def f(n):
    return f(n - 6) + 2048 if n > 30 else 3 * (g(n - 5) + 13)


@lru_cache(None)
def g(n):
    return 2 * n + 50 if n >= 221337 else g(n + 11) - 48


for i in range(221338)[::-1]:
    g(i)
for i in range(221338):
    f(i)
print(f(5078))

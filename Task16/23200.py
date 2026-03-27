from functools import lru_cache


@lru_cache(None)
def f(n):
    return 3 * n + f(n - 3) if n >= 10 else n


for i in range(6250):
    f(i)

print(int((f(6250) + 2 * f(6244)) / f(6238)))

print('#' * 30)

F = [0] * 6400
for n in range(6400):
    if n < 10:
        F[n] = n
    else:
        F[n] = 3 * n + F[n - 3]

print(int((F[6250] + 2 * F[6244]) / F[6238]))

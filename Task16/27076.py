from functools import lru_cache


@lru_cache(None)
def F(n):
    return G(n + 4) if n < 43 else 2 * F(n - 2) - F(n - 4) + 2


@lru_cache(None)
def G(n):
    return G(n + 3) + 2 if n < 11240 else Q(n)


@lru_cache(None)
def Q(n):
    return n + 4 if n < 21 else Q(n - 4) + 2


for i in range(19, 11240):
    Q(i)

for i in range(46, 11241)[::-1]:
    G(i)

for i in range(2027):
    F(i)

print(F(2026))

print('#' * 30)

F = [0] * 11500
G = [0] * 11500
Q = [0] * 11500

for n in range(11500):
    if n < 21:
        Q[n] = n + 4
    else:
        Q[n] = Q[n - 4] + 2

for n in range(11500)[::-1]:
    if n < 11240:
        G[n] = G[n + 3] + 2
    else:
        G[n] = Q[n]

for n in range(11500):
    if n < 43:
        F[n] = G[n + 4]
    else:
        F[n] = 2 * F[n - 2] - F[n - 4] + 2

print(F[2026])

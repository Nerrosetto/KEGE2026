def Bel(n, m):
    return n % m == 0


def f(x):
    return Bel(x, A) or (Bel(x, 23) <= (x not in range(50, 71)))


for A in range(1, 1001)[::-1]:
    if all(f(x) for x in range(1, 1001)):
        print(A)
        break

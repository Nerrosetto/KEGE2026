def DEL(n, m):
    return n % m == 0


def f(x, A):
    return ((DEL(A, 45)) and (DEL(750, x) <= (not DEL(A, x) <= (not DEL(120, x)))))


a = False
for A in range(1, 10000):
    if a:
        break
    for x in range(1, 10000):
        if f(x, A):
            print(A)
            a = True
            break

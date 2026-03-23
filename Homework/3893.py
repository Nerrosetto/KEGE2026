def DEL(x, i):
    return x % i == 0


def f(x, A):
    return (DEL(A, 25)) and ((DEL(x, 24) and DEL(x, 75)) <= (DEL(x, A)))


cnt = 0
for A in range(1, 999):
    if all(f(x, A) for x in range(1, 999)):
        cnt += 1
print(cnt)

def DEL(x, A):
    return x % A == 0


def f(x, A):
    return (DEL(A, 25)) and ((DEL(x, 24) and DEL(x, 75)) <= (DEL(x, A)))


cnt = 0
for A in range(-1000, 1001):
    if A and all(f(x, A) for x in range(-1000, 1001)):
        cnt += 1
print(cnt)

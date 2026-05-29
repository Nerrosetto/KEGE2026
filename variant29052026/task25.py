def prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def f(x):
    h = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0 and prime(i):
            h |= {i}
        if x % i == 0 and prime(x // i):
            h |= {x // i}
    if len(h) < 2:
        return 0
    else:
        M = max(h) + min(h)
        if str(M) == str(M)[::-1]:
            if M > 60000:
                return M
            else:
                return 0
        else:
            return 0


cnt = 0
for i in range(5400001, 10 ** 10):
    if M := f(i):
        cnt += 1
        print(i, M)
        if cnt == 5:
            break

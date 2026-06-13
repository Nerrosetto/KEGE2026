def f(x):
    if x <= 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def m(x):
    d = set()
    u2 = True
    for v in range(2, int(x ** 0.5) + 1):
        if x % v == 0:
            if f(v):
                d |= {v}
    if len(d) == 2:
        for i in range(min(d) + 1, max(d)):
            if f(i):
                u2 = False
    if u2:
        return sum(d)


cnt = 0
for t in range(3700001, 10 ** 10):
    if cnt == 5:
        break
    if M := f(t):
        print(t, M)
        cnt += 1

def f(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    for t in sorted(d):
        if t % 10 == 9 and t != 9:
            return t
    return 0


cnt = 0
for i in range(800001, 10 ** 10):
    if cnt == 5:
        break
    if M := f(i):
        print(i, M)
        cnt += 1

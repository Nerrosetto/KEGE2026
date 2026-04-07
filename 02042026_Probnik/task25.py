from math import ceil


def f(x):
    h = set()
    cnt = 0
    for i in range(2, ceil(x ** 0.5) + 1):
        if x % i == 0 and i != 11:
            h |= {i}
    for i in h:
        if i % 100 == 11 and i != x:
            cnt += 1
    return min(h) if cnt >= 1 else 0


cnt = 0
for i in range(1350050, 2 ** 45):
    if M := f(i):
        print(i, M)
        cnt += 1
    if cnt == 5:
        break

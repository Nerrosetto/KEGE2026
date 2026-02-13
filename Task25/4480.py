from math import prod as pr


def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if sum(d) % 2 != 0 and pr(d) % 2 != 0:
            if len(d) > 10:
                return len(d)
    return 0


cnt = 0
for i in range(800001, 10 ** 15):
    if M := f(i):
        print(i, M)
        cnt += 1
        if cnt == 6:
            break

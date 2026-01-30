def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    for i in sorted(d):
        if len(d) > 1:
            return min(d) + max(d)
    return 0


cnt = 0
for i in range(700001, 10 ** 15):
    M = f(i)
    if M % 10 == 4:
        cnt += 1
        print(i, M)
        if cnt == 5:
            break

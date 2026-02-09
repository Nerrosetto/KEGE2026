def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i}
    if len(d) > 1:
        M = min(d) + max(d)
        if str(M)[-1] == '4':
            return M
    return 0


cnt = 0
for i in range(800000, 10**20):
    M = f(i)
    if M:
        cnt += 1
        print(i, M)
        if cnt == 5:
            break

def sy(num):
    d = set()
    for t in range(2, int(num ** 0.5) + 1):
        if num % t == 0:
            d |= {t, num // t}
    if len(d) > 1:
        if max(d) % 7 == 0:
            return max(d)
    return 0


cnt = 0
for q in range(10 ** 9, 10 ** 20):
    if str(q) == str(q)[::-1]:
        if m := sy(q):
            print(q, m)
            cnt += 1
            if cnt == 5:
                break

def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    return sum(map(int, d)) // len(d) if len(d) > 0 else 0


a = []
cnt = 0
for i in range(700000)[::-1]:
    M = f(i)
    if str(M)[-3:] == '313':
        cnt += 1
        print(i, M)
        if cnt == 7:
            break

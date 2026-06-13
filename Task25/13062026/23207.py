def f(x):
    d = []
    while x % 2 == 0:
        d += [2]
        x //= 2
    i = 3
    while i <= int(x ** 0.5):
        while x % i == 0:
            d += [i]
            x //= i
        i += 1
    if x > 1:
        d += [x]
    if len(d) == 2:
        if str(d[0]).count('5') == 1 and str(d[1]).count('5') == 1:
            return max(d)


cnt = 0
for i in range(1324728, 10 ** 10):
    if cnt == 5:
        break
    if M := f(i):
        print(i, M)
        cnt += 1

def f(x):
    d = []
    while x % 2 == 0:
        d += [2]
        x //= 2
    i = 3
    while i ** 2 <= x:
        while x % i == 0:
            d += [i]
            x //= i
        i += 2
    if x > 1:
        d += [x]
    return d


cnt = 0
for i in range(6086056, 10 ** 15):
    M = f(i)
    if all(str(x).count('6') == 1 for x in set(M)) and len(M) == 2:
        print(i, M[-1])
        cnt += 1
        if cnt == 5:
            break

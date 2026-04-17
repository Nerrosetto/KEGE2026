def fact(x):
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
for N in range(3600001, 10 ** 13):
    M = fact(N)
    if len(M) == 3 and all('3' in str(i) and '5' in str(i) for i in M):
        print(N, max(M))
        cnt += 1
        if cnt == 5:
            break

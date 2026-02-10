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


def f(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) % 90 == 0:
        return True
    return False


cnt = 0
for i in range(5200001, 10 ** 20):
    d = fact(i)
    if len(d) == 9 and f(i):
        print(i, d[-1])
        cnt += 1
        if cnt == 5:
            break

def not_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) > 1:
        return max(d) - min(d)
    return 0


cnt = 0
for N in range(3333338, 10 ** 15):
    M = f(N)

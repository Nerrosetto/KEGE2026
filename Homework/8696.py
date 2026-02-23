def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True


def f(num):
    if is_prime(num):
        return 0
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i}
        if num // i % i == 0:
            d |= {num // i}
    M = sum(map(int, d))
    return M

cnt = 0
for i in range(1273547, 10**20):
    if is_prime(i % 100000) and f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break

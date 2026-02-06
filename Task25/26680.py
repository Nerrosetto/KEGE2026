def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i ** 2 < num:  # Изначально было i < int(num**.5), возвели в квадрат.
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]
    return d


a = []
cnt = 0
for i in range(5000001, 10 ** 25, 2):
    d = fact(i)
    if len(d) == len(set(d)) == 2:
        if is_prime(d[1] - d[0]):
            cnt += 1
            print(i, d[1])
            if cnt == 5:
                break

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def f_1(num):
    d = set()
    if num < 2:
        return 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i):
                d |= {i}
            if is_prime(num // i):
                d |= {num // i}
    return min(d) + max(d) if len(d) > 1 else 0


cnt = 0
for i in range(5400001, 10 ** 10):
    if cnt == 5:
        break
    if M := f_1(i):
        if M > 60000 and str(M) == str(M)[::-1]:
            print(i, M)
            cnt += 1

print('-' * 30)


def f_2(num):
    d = set()
    if num < 2:
        return 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i):
                d |= {i}
            if is_prime(num // i):
                d |= {num // i}
    if len(d) > 1:
        M = max(d) + min(d)
        if M > 60000 and str(M) == str(M)[::-1]:
            return M
    return 0


cnt = 0
for i in range(5400001, 10 ** 10):
    if cnt == 5:
        break
    if M := f_2(i):
        print(i, M)
        cnt += 1

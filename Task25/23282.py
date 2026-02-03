def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True


def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i):
                d |= {i}
            if is_prime(num // i):
                d |= {num // i}
    if len(d) > 1:
        M = min(d) + max(d)
        if M > 60000 and str(M)[::-1] == str(M):
            return M
    return 0


cnt = 0
for num in range(5_400_001, 10 ** 20):
    if M := f(num):
        cnt += 1
        print(num, M)
        if cnt == 5:
            break

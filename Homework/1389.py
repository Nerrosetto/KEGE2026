def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True


def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(num):
                d |= {num}
            if is_prime(i):
                d |= {i}
    return sum(d) if sum(d) != 0 and sum(d) % 17 == 0 else False


cnt = 0
for N in range(250000 + 1, 10 ** 20):
    if M := f(N):
        cnt += 1
        print(N, M)
        if cnt == 5:
            break

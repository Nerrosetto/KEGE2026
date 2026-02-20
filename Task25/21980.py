def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def f(x):
    d = set()
    a = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if is_prime(i):
                if str(i)[-1] == '7':
                    d |= {i}
            if is_prime(x // i):
                if str(x // i)[-1] == '7':
                    d |= {x // i}
    return sum(d) // len(d) if d else 0


cnt = 0
for i in range(111, 750000)[::-1]:
    if m := f(i):
        if m % 111 == 0:
            print(i, m)
            cnt += 1
            if cnt == 5:
                break

# или
print('-' * 10)


def fa(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if i % 10 == 7 and is_prime(i): d |= {i}
            if num // i % 10 == 7 and is_prime(num // i): d |= {num // i}
    if d:
        return sum(d) // len(d)
    return 0


cnt = 0
for N in range(750_000, 0, -1):
    M = fa(N)
    if M and M % 111 == 0:
        print(N, M)
        cnt += 1
        if cnt == 5:
            break

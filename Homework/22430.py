def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True


def f(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    cnt = 0
    for z in sorted(d)[::-1]:
        if is_prime(z):
            cnt += 1
    for i in sorted(d)[::-1]:
        if i % 114 == 39:
            return i
    if cnt < 4:
        return 0


ans = []
cnt = 0
for i in range(456790, 10 ** 15):
    if M := f(i):
        cnt += 1
        ans.append([i, M])
        if cnt == 5:
            break
for i in sorted(ans)[::-1]:
    print(*i)

from fnmatch import fnmatch as fnm

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    for t in sorted(d):
        if t % 10 == 7 and t != 7:
            return t
    return 0


cnt = 0
for N in range(700001, 10 ** 15):
    M = f(N)
    if M:
        print(N, M)
        cnt += 1
        if cnt == 5:
            break

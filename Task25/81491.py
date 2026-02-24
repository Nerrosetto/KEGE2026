def simple(x):
    if x < 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def f(x):
    d = set()
    summi = 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if simple(x // i):
                d |= {x // i}
            if simple(i):
                d |= {i}
    if 0 <= len(d) < 2:
        return 0
    return min(d) + max(d) if str(min(d) + max(d))[-2:] == '13' else 0


ans = []
cnt = 0
for i in range(7000001, 10 ** 15):
    M = f(i)
    if M:
        ans.append(i)
        cnt += 1
        if cnt == 5:
            break
for i in sorted(ans):
    print(i)

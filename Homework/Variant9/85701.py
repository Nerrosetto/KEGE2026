def f(x):
    s = set()
    for y in range(1, int(x ** 0.5) + 1):
        if x % y == 0:
            s |= {x // y, y}
    return len(s)


count = 0
for i in range(999999999)[::-1]:
    M = f(i)
    if (i - M) % 23 == 0:
        count += 1
        print(i)
    if count == 5:
        break
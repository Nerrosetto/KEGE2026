def fact(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    if len(d) == 3:
        return max(d)
    return 0


for i in range(int(106732567 ** 0.5), int(152673836 ** 0.5)):
    if M := fact(i ** 2):
        print(i ** 2, M)

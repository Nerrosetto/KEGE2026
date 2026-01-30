def f(x):
    return ((405 % x == 0) <= (81 % x == 0)) or (A - x > 162)


for A in range(1, 10000):
    if all(f(x) for x in range(1, 1001)):
        print(A)
        break
